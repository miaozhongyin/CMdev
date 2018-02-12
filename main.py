#!/opt/python2.7/bin/python2.7
# -*- coding: UTF-8 -*-


from monitoring.service.yarn.checkJobHeath import YarnApplication
from monitoring.service.scheduler.yarnScheduler import get_app_state
import time


if __name__ == "__main__":
    yarn = YarnApplication()
    yarn.checkHeath()
    result = get_app_state()
    time.sleep(60*60*24*15)
