import datetime
import termcolor
from logging import LOG_LEVELS

LOG_LEVELS_COLORS = {
    "info": "info",
    "error": "error",
    "fatal": "fatal"
}


# TODO: better

class ConsoleLogger(object):
    def __init__(self, verbose=True):
        self._verbose = verbose

    def color_text_by_level(self, text, level):
        if level == LOG_LEVELS["info"]:
            return text

        if level == LOG_LEVELS["error"]:
            return termcolor.colored(text, 'red')

        if level == LOG_LEVELS["fatal"]:
            return termcolor.colored(text, 'red', attrs=['reverse', 'blink'])

    def log(self, msg, who="", level=LOG_LEVELS["info"]):
        if not self._verbose:
            return
        if len(who) > 0:
            msg = "{} | {}".format(who, msg)
        time_msg = datetime.datetime.now().strftime("%y.%m.%d %H:%M:%S")
        msg = "{} | {} | {}".format(msg, level, time_msg)

        print self.color_text_by_level("{}  {}  {}".format("*" * 3, msg, "*" * 3), level)

    def info(self, msg):
        self.log(msg, LOG_LEVELS["info"])

    def error(self, msg):
        self.log(msg, LOG_LEVELS["error"])

    def fatal(self, msg):
        self.log(msg, LOG_LEVELS["fatal"])