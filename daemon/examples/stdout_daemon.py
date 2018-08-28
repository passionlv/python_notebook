import daemon
import time
import sys

#out = open("~/tmp/stdout", "a+")
#err = open("~/tmp/stderr", "a+")
# 如果设定为标准输出，那么关闭终端窗口，退出守护进程。
# Ctrl+c 不会退出进程
# 关闭终端窗口，退出守护进程

def do_main_program():
    print("start the main program...")
    while True:
        time.sleep(1)
        print('another second passed')


context = daemon.DaemonContext()

context.stdout =  sys.stdout
context.stderr = sys.stderr



with context:
    print("start the main program")
    do_main_program()

print("end ")