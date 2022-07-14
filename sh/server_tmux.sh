sudo apt-get -y install tmux
tmux new-session -d -s visdom 'visdom -port 8097 -enable_login';
sleep 5
tmux send 'inhee' ENTER;
tmux send '1234' ENTER;
tmux send '1234' ENTER;
tmux split-window;
tmux send 'python run.py' ENTER;