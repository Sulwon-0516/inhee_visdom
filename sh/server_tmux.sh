if [ $# -eq 0]
    then 
        echo "No argument"
        echo "Your dataset directory: current working directory"
        echo "Your ID: root"
        echo "Your PASSWD: 1234"

        sudo apt-get -y install tmux
        tmux new-session -d -s visdom 'visdom -port 8097 -enable_login';
        sleep 5
        tmux send "root" ENTER;
        tmux send "1234" ENTER;
        tmux send '1234' ENTER;
        tmux split-window;
        tmux send "python run.py" ENTER;
fi

if [ $# -eq 1]
    then 
        echo "One argument"
        echo "Your dataset directory : $1"
        echo "Your ID: root"
        echo "Your PASSWD: 1234"

        sudo apt-get -y install tmux
        tmux new-session -d -s visdom 'visdom -port 8097 -enable_login';
        sleep 5
        tmux send "root" ENTER;
        tmux send "1234" ENTER;
        tmux send '1234' ENTER;
        tmux split-window;
        tmux send "python run.py" ENTER;
fi

if [ $# -eq 2]
    then 
        echo "One argument"
        echo "Your dataset directory : $1"
        echo "Your ID: root"
        echo "Your PASSWD: $2"

        sudo apt-get -y install tmux
        tmux new-session -d -s visdom 'visdom -port 8097 -enable_login';
        sleep 5
        tmux send "root" ENTER;
        tmux send "$2" ENTER;
        tmux send '1234' ENTER;
        tmux split-window;
        tmux send "python run.py" ENTER;
fi

if [ $# -eq 3]
    then
        echo "Two argument"
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
fi



if [ $# -gt 3]
    then
        echo "Too many arugments"
        echo "Use less than 3 arguments here"
