# Result plotting server w/ Visdom 
## Disclaimer
Here I share a simple visdom server. 
I hope this code will help us share our progress and experiment results.

## Simple Introduction
What `Visdom` do is basically same as `Tensorboard`.
`Visdom` support plotting graph, scatter, geometries with 2D images. 

### Cons

However, unlike `Tensorboard`, `Visdom` doesn't save the content of server in a file (in default).
Easily, the content is volatile. 
It's why I only using `Visdom` to showing saved images rather than plotting the loss-function or intermediate output
Also `Visdom` is quite slow, so I basically recommend `Tensorboard` to manage experiments. 


### My server

You should input **["top directory"]** you want to plot images. 
Then it plots ALL **png** / **jpg** / **jpeg** / **tiff** images in the directory.


Also it updates the content every 5 minutes when...
- file name changed
- file is moved / removed


### Application Guide
Each image has their title, and the title is "absolute path" of the image
You can find search-bar on the top right corner of screen. 
You can filtering the content to be shown with search-bar. 

```
[keyword1].*[keyword2].*[keyword3]
```
Like above example, Visdom support `.*` as similar as regex. 
(Just use `.*` as `*` in shell, which means "0 or more of any character")


## Requirements
You shoud install visdom & schedule, matplotlib
(you also need `beautifulsoup4` and `lxml`, but they aren't essential.)

```
pip install visdom schedule matplotlib
```

### Issues with conda
If you are using conda environment, I recommend you install python requirements on "base" environment. 
Instead you can modify shell script to activate conda environment before launching server.



## Quick start
you can simply start program with following commands.
you should type passwd at beginning (install tmux)

```
./sh/server_tmux.sh [YOUR_DB_DIR] [YOUR_ID] [YOUR_PASSWD]
```
(It will turn off a tmux session whose name is "visdom" as initialization)

You can run the code with 0~3 arguments
- default setting: 
    - DIR : Current working directory
    - ID : root
    - PASSWD : 1234
- 1 argument: [DB_directory] 
- 2 arguments : [DB_directory] [YOUT_PASSWD]




## Run manually
You can also run server manually. 
### 1. run visdom server
You should run visdom server in background continuously. 
I recommend you use `screen` or `tmux` to run visdom server in background.

```
visdom -port 8097 -enable_login
```

- `-port 8097` : binding to port 8097
- `-enable_login` : Only people knowing ID/PASSWD can access the content.

You should set ID/PASSWD when you boot your server.

### 1. run my image plotting server
My image plotter plot all image files in the given directory.
It updates the images every 5 minute (default)
You should run the code in background similar as visdom server.

```
python run.py --dir YOUR_DIR --update_period 5
```

- You can change refractory period of update with `--update_period` whose unit is minute.
- `--single_env` options is not fully implemented yet. Default : True



## Issues with port
The default port is `8097`. 
You can access the server anywhere with following address

```
https://[YOUR_IP_ADDRESS]:8097
```

If it's not working (like responding TIME_OUT), you should check your firewall. 

```
sudo apt-get install iptables
sudo iptables -nL | grep [YOUR_PORT, default 8097]
```

If there's no result, you need to add additional rule

```
sudo iptables -I INPUT 1 -p tcp --dport [YOUR_PORT, default 8097] -j ACCEPT
```

This command allow TCP input with that port.


## Guide
- It automatically checks file and folder removed / created.
- Changing file or dirname would be treated as removed and created again.
- Visdom server holds ALL IMAGES on RAM. It would be super heavy and slow down your machine extremely if you try to plot tons of images.


## Update plan

- Currently, Only single directory is allowed. support of Multiple direcotry will be update it soon
- Supporting short videos and **gif**


## Some examples

- When you launched program & attached to tmux session

![Screenshot from 2022-07-15 19-06-11](https://user-images.githubusercontent.com/65122489/179206746-92310792-5b89-401e-933e-9b6e1f9eadf1.png)

- Example 1

![Screenshot from 2022-07-15 19-32-23](https://user-images.githubusercontent.com/65122489/179206987-93eef03c-6897-47a3-8bef-b61d5e37c6f6.png)


- Example 2 (filtered with keyword **"beetle"**)

![Screenshot from 2022-07-15 19-33-20](https://user-images.githubusercontent.com/65122489/179207470-f9fb8c76-91e2-439e-b25a-5a2c6b739e15.png)
