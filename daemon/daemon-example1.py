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
    logger.info("Main start: %s, which ppid: %s" % (os.getpid(), os.getppid()))
    n = 0
    while True:
        time.sleep(1)
        #print("In the main programe: %s, which ppid: %s, n=%r" % (os.getpid(), os.getppid(), n ))
        logger.info("mian loop: %s, which ppid: %s, n=%r" % (os.getpid(), os.getppid(), n ))
        n = n + 1
        if n > 10:
            raise NotImplementedError
            #sys.exit(0)
    logger.info("Main End: %s, which ppid: %s" % (os.getpid(), os.getppid()))


def program_cleanup(signum, frame):
    logger.info('daemon stops')
    context.terminate(signum, frame)

def reload_program_config(signum, frame):
    logger.info('reloading config')

def program_interrupt(signum, frame):
    logger.info("daemon want to interrupt, but not interrupt ")

pidfile= lockfile.FileLock('/home/xiaopeng/tmp/example1.pid')
# 如果设定了stdout，stderr,
#context = daemon.DaemonContext(stdout=sys.stdout,
#                                 stderr=sys.stderr)

context = daemon.DaemonContext(pidfile=pidfile)

# context.signal_map = {
#     signal.SIGINT: program_interrupt,
#     signal.SIGTERM: program_cleanup,
#     signal.SIGHUP: program_interrupt,
#     signal.SIGUSR1: reload_program_config,
#     }

def run_main():
    #import ipdb;ipdb.set_trace()
    logger.info("First process: %s, which ppid: %s" % (os.getpid(), os.getppid()))

    context.files_preserve = [handler.stream]
    initial_program_setup()

    with context:
        logger.info("Daemon start: %s, which ppid: %s" % (os.getpid(), os.getppid()))
        while True:
            try:
                do_main_program()
            except Exception as e:
                logger.info("Exception: %r "%e)
                # 5 秒后重启 main 程序
                time.sleep(5)

run_main()