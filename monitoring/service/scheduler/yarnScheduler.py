#!/opt/python2.7/bin/python2.7
# -*- coding: UTF-8 -*-

"""
    yarn scheduler

"""
from monitoring.service.yarn.checkJobHeath import YarnApplication
from monitoring.comment.log.logger import Log
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
log = Log("yarnScheduler")


def get_app_state():
    yarn = YarnApplication()
    scheduler.add_job(yarn.checkHeath, "cron", month="2-3", day="*", hour="10", minute="37")
    try:
        scheduler.start()
        log.logger.info("start run get_app_state job")
        return True
    except (KeyboardInterrupt, SystemExit)as e:
        log.logger.inf(e)
        return False
