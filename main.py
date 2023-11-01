from argparse import ArgumentParser, Namespace
import time

parser = ArgumentParser()

parser.add_argument("start", help="starts the pomodoro timer")

args: Namespace = parser.parse_args()

def start(t, i):
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer,end="\r") 
        time.sleep(1)
        t -= 1

    while i:
        mins, secs = divmod(i, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer,end="\r") 
        time.sleep(1)
        i -= 1
      
    print('Fire in the hole!!')

# args
if args.start:
    start(int(input("Enter work time: ")), int(input("Enter break time: ")))
else:
    pass
