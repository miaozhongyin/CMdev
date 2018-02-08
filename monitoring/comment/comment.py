#!/opt/python3/bin/python3
# -*- coding: UTF-8 -*-
__doc__ = "check spark job heathy state"
__author__ = "bigdata supprot zhongyin.miao with l3 team"

"""         """

CLASTER_NAME="Cloudera QuickStart"

SERVICE_TYPE = {
  'SQOOP':'SQOOP',
  'ZOOKEEPER':'ZOOKEEPER',
  'HUE':'HUE',
  'IMPALA':'IMPALA',
  'OOZIE':'OOZIE',
  'HDFS':'HDFS',
  'SOLR':'SOLR',
  'HBASE':'HBASE',
  'YARN':'YARN',
  'SPARK_ON_YARN':'SPARK_ON_YARN',
  'HIVE':'HIVE',
  'SQOOP_CLIENT':'SQOOP_CLIENT',
  'FLUME':'FLUME',
  'KAFKA':'KAFKA',
  'SPARK2_ON_YARN':'SPARK2_ON_YARN'
}

SERVICE_NAME = {
    'sqoop': 'sqoop',
    'zookeeper': 'zookeeper',
    'hue': 'hue',
    'impala': 'impala',
    'oozie': 'oozie',
    'hdfs': 'hdfs',
    'solr': 'solr',
    'hbase': 'hbase',
    'yarn': 'yarn',
    'spark_on_yarn': 'spark_on_yarn',
    'hive': 'hive',
    'sqoop_client': 'sqoop_client',
    'flume': 'flume',
    'kafka': 'kafka',
    'spark2_on_yarn': 'spark2_on_yarn'
}


