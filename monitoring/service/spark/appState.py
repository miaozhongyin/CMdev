#!/opt/python3/bin/python3
# -*- coding: UTF-8 -*-
__doc__ = "check spark job heathy state"
__author__ = "bigdata supprot zhongyin.miao with l3 team"


class ApplicationState(object):

    def __init__(self,id,name,start_time,state):
        self.name = name
        self.id = id
        self.start_time = start_time
        self.state = state



