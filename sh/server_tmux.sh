echo "Your dataset directory: $1"
echo "Your ID: $2"
echo "Your PASSWD: $3"
sudo apt-get -y install tmux
tmux new-session -d -s visdom 'visdom -port 8097 -enable_login';
sleep 5
tmux send "$2" ENTER;
tmux send "$3" ENTER;
tmux send '1234' ENTER;
tmux split-window;
tmux send "python run.py --dir $1" ENTER;