#!/opt/python2.7/bin/python2.7
# -*- coding: UTF-8 -*-

import os


class BaseTools:

    @staticmethod
    def get_root_dir():
        path = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.split(os.path.split(path)[0])[0]
        return root_dir

