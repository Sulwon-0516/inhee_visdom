import glob
import matplotlib.pyplot as plt
import os
import os.path as path
import numpy as np
from visdom import Visdom

viz = Visdom()
IMGNET1k = '/home/inhee/VCL/insect_recon/EDA/Imagenet1k/sample_imgs'
INATURAL = '/home/inhee/VCL/insect_recon/EDA/iNaturalist'
INATURAL_SAMPLE = '/home/inhee/VCL/insect_recon/EDA/iNaturalist/sample_imgs'

SAMPLE_DATASET = '/home/inhee/VCL/insect_recon/EDA/sample_datasets'

DIR_LIST = [IMGNET1k, INATURAL, INATURAL_SAMPLE]


def plot_img(img, env_name, title):
    if img.shape[0] != 3:
        img = np.transpose(img, (2,0,1))
    viz.image(img, env = env_name,opts=dict(title = title))


def plot_folder(dir, env_name = None):
    f_list = glob.glob(path.join(dir,'*.png'))
    f_list_jpg = glob.glob(path.join(dir,'*.JPEG'))
    f_list.extend(f_list_jpg)

    if env_name == None:
        env_name = path.basename(dir)
    else:
        env_name += path.basename(dir)

    if len(f_list) == 0:
        print('no file to plot')
        return
    
    
    for file in f_list:
        img = plt.imread(file)
        if img.shape[-1] == 4:
            img = img[:,:,0:3]

        f_n = path.basename(file)
        f_n = path.splitext(f_n)[0]
        plot_img(img, env_name, f_n)



if __name__ == '__main__':
    sample_dir = os.listdir(SAMPLE_DATASET)
    for dir_ in sample_dir:
        dir = path.join(SAMPLE_DATASET, dir_)
        plot_folder(dir, env_name="SAMPLE")

    for i, dir in enumerate(DIR_LIST):
        if i==0:
            en = "Imgnet_"
        elif i==2:
            en = "INat_"
        else:
            en = ""
        
        plot_folder(dir, env_name=en)

    



