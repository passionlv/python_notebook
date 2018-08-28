import signal
import time

def signal_handler(signum, frame):
    print('Received signal: ', signum)
    # print(frame)
print("%i"%signal.SIGTSTP)

n = 1
while True:
    signal.signal(signal.SIGHUP, signal_handler)  # 1
    # 点击 jupyter 中的 停止按钮触发 2 信号。  
    signal.signal(signal.SIGINT, signal_handler)  # 2
    signal.signal(signal.SIGQUIT, signal_handler)  # 3
    signal.signal(signal.SIGALRM, signal_handler)  # 14
    signal.signal(signal.SIGTERM, signal_handler)  # 15
    signal.signal(signal.SIGCONT, signal_handler)  # 18

    # 5 秒后自动触发 signal.SIGALRM 信号。 signal.SIGALRM 为 14
    signal.alarm(5)

    while True:
        print('waiting %s s ' % n)
        time.sleep(1)
        n = n + 1
        if n > 10:
            break
            # raise NotImplementedError