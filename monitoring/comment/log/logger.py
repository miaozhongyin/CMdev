#!/opt/python2.7/bin/python2.7
# -*- coding: UTF-8 -*-



import time
import logging
import platform, os
from monitoring.comment.basetools import BaseTools


class Log:
    log_date = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
    delimiter = '\\' if platform.system() == "Windows" else '/'

    def __init__(self, name):
        self.path = BaseTools.get_root_dir() + self.delimiter + "log" + self.delimiter
        self.filename = self.path + Log.log_date + '.log'
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)

        self.console = logging.StreamHandler()
        self.console.setFormatter(Log.log_format)
        self.console.setLevel(logging.INFO)

        self.file = logging.FileHandler(self.filename, 'a+')
        self.file.setFormatter(Log.log_format)
        self.file.setLevel(logging.INFO)

        self.logger.addHandler(self.console)
        self.logger.addHandler(self.file)


class CustomError(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        if self.msg:
            return self.msg
        else:
            return "no message.....";
