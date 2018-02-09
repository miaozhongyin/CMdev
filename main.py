#!/opt/python2.7/bin/python2.7
# -*- coding: UTF-8 -*-

from  monitoring.service.yarn.checkJobHeath import YarnApplication


if __name__ == "__main__":
    yarn = YarnApplication()
    yarn.checkHeath()