from visdom import Visdom
import numpy as np
from tqdm import tqdm

test_name_sets = [
    "env1_env2_env3",
    "env1_env2",
    "env1_env4_env3",
    "env2_env3_env4_env5"
]


RAND_SIZE = 64
N_img = 30


def rand_img(size = RAND_SIZE):
    img = np.random.rand(3,size,size)

    return img

def check_env_setting(viz):
    for env in tqdm(test_name_sets):
        for i in range(N_img):
            img = rand_img()
            img_name = "test_%02d"%(i)

            viz.image(img, env = env, opts = dict(title = img_name))


if __name__ == '__main__':
    viz = Visdom()
    check_env_setting(viz)
    pass
