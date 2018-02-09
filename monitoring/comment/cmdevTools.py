#!/opt/python3/bin/python3
# -*- coding: UTF-8 -*-

__doc__ = "check spark job heathy state"
__author__ = "bigdata supprot zhongyin.miao with l3 team"

import json,os
from cm_api.api_client import ApiResource
from monitoring.comment.comment import *


class CMTools:

    def getcmInfo(self,key):
        path = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.split(os.path.split(path)[0])[0]
        source_path = os.path.join(root_dir, "resource/cminfo.json")
        #source_path = "C:\\project\\python\\CMdev\\resource\\cminfo.json"
        print(source_path)
        with  open(source_path,"r") as f:
            context = json.loads(f.read())
            items = context["items"]
            if key in items.keys():
                return items[key]
            else:
               return None

    def getApiClient(self,cminfo):
        if cminfo is None:
            exit(1)
        else:
            #print(cminfo["cm_host"])
            cm_client = ApiResource(server_host=cminfo['cm_host'], server_port=cminfo['cm_port'],username=cminfo['cm_user'], password=cminfo['cm_passwd'])
            cluster = cm_client.get_cluster(CLASTER_NAME)
            return cluster

    def getServer(self,cluster,service_name):
        service_list = cluster.get_all_services()
        server_name = SERVICE_NAME.get(service_name)
        if server_name is not None:
            for service in service_list:
                if server_name == service.name:
                    cm_server = service
                    return cm_server
        else:
            return None

