import glob
import matplotlib.pyplot as plt
import os
import os.path as path
from visdom import Visdom
import schedule
import datetime
import time

img_types = ['.png', '.PNG', '.jpg', '.jpeg', '.JPG', '.JPEG', '.tif', 'tiff', '.TIF', '.TIFF']


MASTER_DIR = '/mnt/g/SNU_VCL'


class AutoUpate_Server():
    def __init__(self, arg):
        self.flists = []
        self.use_single_env = arg.single_env
        self.top = path.abspath(arg.dir)
        self.n_top = len(self.top.split("/"))

        # initialize server
        self.viz = Visdom(
            port = arg.port,
            username = arg.username,
            password = arg.passwd
        )

        # get initial flists
        self.last_update = time.mktime(datetime.datetime.today().timetuple())
        fl_1, fl_2 = self.get_flist()
        self.flists = fl_1 + fl_2

        # intial plotting
        self.wind_ids = {}
        self.add_plot(self.flists)

    def auto_update(self, min = 5):
        schedule.every(min).minutes.do(self.update)

        while True:
            schedule.run_pending()
            time.sleep(1)


    def get_flist(self):
        '''
        return lists of imgs files, under the file.
        
        '''
        # get all imgs
        flists = []
        new_flists = []
        for root, dirs, files in os.walk(self.top, topdown=False):
            for name in files:
                extension = path.splitext(name)[1]
                if extension in img_types:
                    img_path = path.join(root, name)

                    if path.getmtime(img_path) > self.last_update or path.getctime(img_path) > self.last_update:
                        new_flists.append(img_path)
                    else:
                        flists.append(img_path)
        
        print("There are %d images in "%(len(flists)), self.top)

        return flists, new_flists


    def update(self):
        '''
        update the images
        '''
        flists, new_flist = self.get_flist()
        remove_list = [f for f in self.flists if f not in flists]

        self.rm_plot(remove_list)
        self.add_plot(new_flist)
        self.flists = list(self.wind_ids.keys())
        self.last_update = time.mktime(datetime.datetime.today().timetuple())


    def add_plot(self, new_list):
        '''
        Add some images
        '''
        for f in new_list:
            img = plt.imread(f)
            title = path.splitext(f)[0]
            if img.shape[-1] == 4:
                # in case of RGBA
                img = img[:,:,0:3]

            if img.shape[-1] == 3:
                img = img.transpose(2,0,1) # visdom gets image as C x W x H

            if self.use_single_env:
                env_name = 'main'
            else:
                dirs = f.split('/')
                if len(dirs) <= (self.n_top + 1):
                    env_name = 'top'
                else:
                    env_name = dirs[self.n_top+1]
                
            wind_id = self.viz.image(img, env = env_name, opts = dict(title = title))
            self.wind_ids[f] = (wind_id, env_name)

    def rm_plot(self, remove_list):
        '''
        Remove some images
        '''
        for f in remove_list:
            wind_id = self.wind_ids.pop(f, None)

            if isinstance(wind_id, type(None)):
                print("error on window id <> file list")
                assert(0)

            self.viz.close(win = wind_id[0], env = wind_id[1])
        


