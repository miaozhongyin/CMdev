#!/opt/python3/bin/python3
# -*- coding: UTF-8 -*-

__doc__ = "check spark job heathy state"
__author__ = "bigdata supprot zhongyin.miao with l3 team"

import json, os,platform
from cm_api.api_client import ApiResource
from monitoring.comment.comment import *
from monitoring.comment.log.logger import Log


class CMTools:

    delimiter = '\\' if platform.system() == "Windows" else '/'
    log = Log("CMTools")

    def getcmInfo(self, key):
        """
        read cminfo.json file  and return  cluster's information
        :param key: cminfo
        :return:    json
        """
        path = os.path.dirname(os.path.realpath(__file__))
        root_dir = os.path.split(os.path.split(path)[0])[0]
        source_path = os.path.join(root_dir, "resource"+ self.delimiter+ "cminfo.json")
        self.log.logger.info("resource path:"+ source_path)
        # source_path = "C:\\project\\python\\CMdev\\resource\\cminfo.json"
        with open(source_path, "r") as f:
            context = json.loads(f.read())
            items = context["items"]
            if key in items.keys():
                return items[key]
            else:
                self.log.logger.info("can not open file" + source_path)
                return None

    def getApiClient(self, cminfo):
        """
        get cluster object by cluster's information
        :param cminfo: cluster's information
        :return: cluster object
        """
        if cminfo is None:
            self.log.logger.info("cluster information is useless")
            exit(1)
        else:
            # print(cminfo["cm_host"])
            cm_client = ApiResource(server_host=cminfo['cm_host'], server_port=cminfo['cm_port'],
                                    username=cminfo['cm_user'], password=cminfo['cm_passwd'])
            cluster = cm_client.get_cluster(cminfo["cluster_name"])
            return cluster

    def getServer(self, cluster, service_name):
        """
        get specific service object
        :param cluster:
        :param service_name:
        :return:
        """
        service_list = cluster.get_all_services()
        server_name = SERVICE_NAME.get(service_name)
        if server_name is not None:
            for service in service_list:
                if server_name == service.name:
                    cm_server = service
                    return cm_server
        else:
            self.log.logger.info("can not find "+server_name+" please check you input....")
            return None
