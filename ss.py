import sys
from mss import mss
import time

"""
Takes screenshot of screen according
to command

Takes two argument, 'command' and 'n'

Commands:
    1. sched - take a ss aftr n seconds
    2. loop_inf - takes ss at n sec interval (n>=3)
    3. loop_fini - inputs another number x
        takes x ss at n sec interval 
"""

if(len(sys.argv) != 3):
    print('Invalid Argument')
    sys.exit()
command = sys.argv[1]
n = int(sys.argv[2])
if(command == 'sched'):
    time.sleep(n)
    with mss() as sct:
        sct.shot()

elif(command == 'loop_inf'):
    if(n<3):
        print('too short period')
        sys.exit()
    i = 1
    with mss() as sct:
        while(True):
            time.sleep(n)
            sct.shot(output='{}.png'.format(i))
            i = i +1
elif(command == 'loop_fini'):
    rng = int(input('how many shots?: '))
    if(n<3):
        print('too short period')
        sys.exit()
    with mss() as sct:
        for i in range(rng):
            time.sleep(n)
            sct.shot(output='{}.png'.format(i+1))
    
