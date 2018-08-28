import daemon
import time
import os

def do_main_program():
    print("start the main program...")
    while True:
        time.sleep(1)
        print('another second passed')



context = daemon.DaemonContext()

with context :
    print("start the main program")
    do_main_program()

print("end ")