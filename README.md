# Inhee's visdom template
## Disclaimer
Here I share a simple visdom server. 
I hope this code could be helpful to share our progress and experiment results.

## Simple Introduction
What visdom does is basically same as Tensorboard.



## Requirements
You shoud install visdom & schedule, matplotlib
(you also need `beautifulsoup4` and `lxml`, but they aren't essential.)

```
pip install visdom schedule matplotlib
```

## How to Run
### run simply
you can simply start program with following commands.
you should type passwd at beginning (install tmux)

```
./sh/server_tmux.sh
```
(It will turn of a tmux session whose name is "visdom" as initialization)

You can also run the server manually with following instruction.

### run visdom server
You should run visdom server in background continuously. 
I recommend you use `screen` or `tmux` to run visdom server in background.

```
visdom -port 8097 -enable_login
```

- `-port 8097` : binding to port 8097
- `-enable_login` : Only people knowing ID/PASSWD can access the content.

You should set ID/PASSWD when you boot your server.

### run my image plotter
My image plotter plot all image files in the given directory.
It updates the images every 5 minute (default)
You should run the code in background similar as visdom server.


```
python run.py --dir YOUR_DIR --single_env True --update_period 5
```

## About my code


## Guide
It automatically checks file and folder removed / created.
Changing file or dirname would be treated as removed and created again.



