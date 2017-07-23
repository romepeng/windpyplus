import platform, os
import time
from datetime import datetime, timedelta


def run_Task():
    os_platform = platform.platform()
    #print(os_platform)
    if os_platform.startswith('Darwin'):
        print('This is mac os system.')
        os.system('ls')
    elif os_platform.startswith('Windows'):
        print('This is Windows system.')
        os.system('dir')

def timerFunc(sched_Timer):
    flag=0
    while True:
        now = datetime.now()
        #print(now)
        if now == sched_Timer:
            run_Task()
            flag = 1
        else:
            if flag == 1:
                sched_Timer = sched_Timer + timedelta(minutes=1)
                print(sched_Timer)
                flag=0

if __name__ == '__main__':
    sched_Timer = datetime(2017, 7, 6, 19, 40, 10)
    print('run the timer task at {}'.format(sched_Timer))
    timerFunc(sched_Timer)








