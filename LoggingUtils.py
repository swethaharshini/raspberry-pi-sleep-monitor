from datetime import datetime
import logging
import os.path
from ProcessProtocolUtils import TerminalEchoProcessProtocol

def log(msg):
    tnow = datetime.now()
    logging.info('%s: %s' % (tnow.isoformat(), msg))

def setupLogging():
    logFormatter = logging.Formatter("%(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    if os.path.exists('/home/pi'):
        tnow = datetime.now()
        fileName = tnow.strftime('/home/pi/sleep-monitor-%Y-%m-%d-%H-%M-%S.log')
        fileHandler = logging.FileHandler(fileName)
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

class LoggingProtocol(TerminalEchoProcessProtocol):
    def __init__(self, prefix):
        TerminalEchoProcessProtocol.__init__(self)
        self.prefix = prefix

    def outLineReceived(self, line):
        txt = '%s: %s' % (self.prefix, line)
        log(txt)

    def errLineReceived(self, line):
        txt = '%s: ERROR: %s' % (self.prefix, line)
        log(txt)
