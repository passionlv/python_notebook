import daemon
import logging
import time
import signal
import threading
import os
import sys
import lockfile

logfilename = '/home/xiaopeng/tmp/testdaemon.log'
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s:%(levelname)s:%(message)s',
    '%Y-%m-%d %H:%M:%S')
handler = logging.FileHandler(logfilename)
handler.setFormatter(formatter)
logger.addHandler(handler)
print(daemon.__file__ )
def initial_program_setup():
    logger.info('daemon started')

def do_main_program():
    logger.info("In the main programe: %s, which ppid: %s" % (os.getpid(), os.getppid()))
    n = 0
    while True:
        time.sleep(1)
        print("In the main programe: %s, which ppid: %s, n=%r" % (os.getpid(), os.getppid(), n ))
        logger.info("In the main programe: %s, which ppid: %s, n=%r" % (os.getpid(), os.getppid(), n ))
        n = n + 1
        if n > 10:
            #pass
            #raise NotImplementedError
            #sys.exit(0)
            break;
        #logger.info("In the main program")
        #logger.info('another second passed')

def program_cleanup(signum, frame):
    logger.info('daemon stops')
    context.terminate(signum, frame)

def reload_program_config(signum, frame):
    logger.info('reloading config')

pidfile= lockfile.FileLock('/home/xiaopeng/tmp/example1.pid')
# 如果设定了stdout，stderr,
# context = daemon.DaemonContext(stdout=sys.stdout,
#                                 stderr=sys.stderr)

context = daemon.DaemonContext(pidfile=pidfile)

context.signal_map = {
    signal.SIGTERM: program_cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_program_config,
    }


context.files_preserve = [handler.stream]

initial_program_setup()

logger.info("In the first process: %s, which ppid: %s" %(os.getpid(), os.getppid()))

with context:
    logger.info("In context: %s, which ppid: %s" % (os.getpid(), os.getppid()))
    logger.info("enter the main program")

    do_main_program()
    logger.info("exit the main program")