from src import visdom_vis
import argparse
import os




parser = argparse.ArgumentParser()
parser.add_argument("--dir", type=str, default=os.getcwd(), 
                        help='Top directory to visualize, default: cwd')
parser.add_argument("--single_env", type=bool, default=True, 
                        help='Use single environment, default: True')
parser.add_argument("--update_period", type=int, default=5, 
                        help='updating plot period (minute), default: 5')
args = parser.parse_args()

print("code is running")
AUS = visdom_vis.AutoUpate_Server(top = args.dir, use_single_env = args.single_env)
AUS.auto_update(args.update_period)