import daemon
import logging
import time
import signal
import threading

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
    while True:
        time.sleep(1)
        logger.info('another second passed')

def program_cleanup(signum, frame):
    logger.info('daemon stops')
    context.terminate(signum, frame)

def reload_program_config(signum, frame):
    logger.info('reloading config')

context = daemon.DaemonContext()

context.signal_map = {
    signal.SIGTERM: program_cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_program_config,
    }

context.files_preserve = [handler.stream]

initial_program_setup()

with context:
    do_main_program()