#!/opt/python3/bin/python3
# -*- coding: UTF-8 -*-
__doc__ = "check spark job heathy state"
__author__ = "bigdata supprot zhongyin.miao with l3 team"


from datetime import datetime, timedelta
from monitoring.comment.CMdevTools import CMTools
from monitoring.service.spark import ApplicationState
from monitoring.service.email.SendEmail import *

class YarnApplication:

    def getYarnApps(self):
        CM_INFO = "cminfo"
        server_name = "yarn"
        cm_tools = CMTools()
        cm_info = cm_tools.getcmInfo(CM_INFO)
        cm_client = cm_tools.getApiClient(cm_info)
        cm_server = cm_tools.getServer(cm_client,server_name)
        yarn_server = cm_server
        if yarn_server is not None:
            end = datetime.now()
            start = end - timedelta(hours=24)
            yarn_response = yarn_server.get_yarn_applications(start_time=start, end_time=end, limit=100,offset=0)
            applications = yarn_response.applications
            app_list = [];
            for item in applications:
                #print(item.name + "  "+item.applicationId+" "+str(item.startTime)+" "+str(item.endTime)+" "+item.state)
                app_state = ApplicationState.ApplicationState(id=item.applicationId,name=item.name,start_time=item.startTime,state=item.state)
                app_state.end_time = item.endTime
                app_list.append(app_state)
            return app_list
        else:
            exit(1)


######################
if __name__== "__main__":
    yarn = YarnApplication()
    app_list = yarn.getYarnApps()
    describe = "-------------------------------yarn application info list-------------------------------------------\n\n"
    info_list = [describe]
    for item in app_list:
        app_info = "|app_id :{id} | app_name:{name} | start_time:{start_time} | item_state:{state}|".format(id=item.id,name=item.name,start_time=item.start_time,state=item.state)
        #app_info = item.id+"     "+item.name + "    "+str(item.start_time)+"    "+item.state
        print app_info
        info_list.append(app_info)
    context = "".join(tuple(info_list))
    smtp_config = SmtpConfig(host="smtp.qq.com",port=465,user="853945306@qq.com",passwd="qyrdbvgcjngrbcaa",sender="853945306@qq.com",receivers=["853945306@qq.com"])
    messageinfo = MessageInfo(mine=context,sender="starbucks CDH platform",receiver="starbucks team",subject="starbucks cdh platform")
    messages = messageinfo.set_message()
    sendEmail(smtp_config, messages)




