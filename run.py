from src import visdom_vis
import argparse
import os




parser = argparse.ArgumentParser()
parser.add_argument("--dir", type=str, default='/home/inhee/VCL/insect_recon',#os.getcwd(), 
                        help='Top directory to visualize, default: cwd')
parser.add_argument("--single_env", type=bool, default=True, 
                        help='Use single environment, default: True')
parser.add_argument("--update_period", type=int, default=5, 
                        help='updating plot period (minute), default: 5')
parser.add_argument("--port", type=int, default=8097, 
                        help='Port of Visdom server')
parser.add_argument("--username", type=str, default='root',
                        help='username of visdom server')
parser.add_argument("--passwd", type=str, default='1234',
                        help='passwd of visdom server')
                
args = parser.parse_args()

print("code is running")
AUS = visdom_vis.AutoUpate_Server(arg = args)
AUS.auto_update(args.update_period)