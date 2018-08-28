import daemon
import time
import sys


def do_main_program():
    print("start the main program...")
    while True:
        time.sleep(1)
        print('another second passed')


context = daemon.DaemonContext()

context.stdout =  open("/home/xiaopeng/tmp/outfile", "a+")
#context.stderr = sys.stderr

with context:
    print("start the main program")
    do_main_program()

print("end ")