

# *******************************************************************************************
# killLongRunningImpalaQueries.py
##
# Kills Long Running Impala Queries
# as we all know the status of impala query has seven type :CREATED, INITIALIZED, COMPILED, RUNNING, FINISHED, EXCEPTION, and UNKNOWN.
# in general,we think the queries has a status of EXCEPTION is bad ,and need our manually cancel.
# yet some time we find there is some queries which has been running a long time than a user-defined threshold.
# therefor, we also think this queries is bad ,so we need to cancel this queries manually.
##
# This script provides an example of using Cloudera Manager's Python API Client to programmatically
# list and/or kill Impala queries that have been running longer than a user-defined threshold.
# It may be useful in shops where poorly formed queries run for too long and consume too many cluster resources,
# and an automated solution for killing such queries is desired.
##
# Usage: ./killLongRunningImpalaQueries.py  queryRunningSeconds [KILL]
##
# Set queryRunningSeconds to the threshold considered "too long"
# for an Impala query to run, so that queries that have been running
# longer than that will be identifed as queries to be killed
##
# The second argument "KILL" is optional
# Without this argument, no queries will actually be killed, instead a list
# of queries that are identified as running too long will just be print(ed to the console
# If the argument "KILL" is provided a cancel command will be issues for each selcted query
##
# CM versions <= 5.4 require Full Administrator role to cancel Impala queries
##
# Set the CM URL, Cluster Name, login and password in the settings below
##
# This script assumes there is only a single Impala service per cluster
##
# *******************************************************************************************


# ** imports *******************************

import sys
import pytz
from datetime import datetime, timedelta
from cm_api.api_client import ApiResource

# ** Settings ******************************

# Cloudera Manager Host
cm_host = "192.168.13.130"
cm_port = "7180"

# Cloudera Manager login with Full Administrator role
cm_login = "admin"

# Cloudera Manager password
cm_password = "admin"

# Cluster Name
cluster_name = "cluster"

# *****************************************
fmt = '%Y-%m-%d %H:%M:%S %Z'


def printUsageMessage():
    print( "Usage: killLongRunningImpalaQueries.py <queryRunningSeconds>  [KILL]")
    print( "Example that lists queries that have run more than 10 minutes:")
    print( "./killLongRunningImpalaQueries.py 600")
    print( "Example that kills queries that have run more than 10 minutes:")
    print( "./killLongRunningImpalaQueries.py 600 KILL")

# ** Validate command line args *************


if len(sys.argv) == 1 or len(sys.argv) > 3:
    printUsageMessage()
    quit(1)

queryRunningSeconds = sys.argv[1]

if not queryRunningSeconds.isdigit():
    print( "Error: the first argument must be a digit (number of seconds)")
    printUsageMessage()
    quit(1)

kill = False

if len(sys.argv) == 3:
    if sys.argv[2] != 'KILL':
        print( "the only valid second argument is \"KILL\"")
        printUsageMessage()
        quit(1)
    else:
        kill = True

impala_service = None

# Connect to CM
print( "\n***********************************current date is " + str(datetime.now()) + "**************************************")
print( "\nConnecting to Cloudera Manager at " + cm_host + ":" + cm_port)
api = ApiResource(server_host=cm_host, server_port=cm_port,
                  username=cm_login, password=cm_password)

# Get the Cluster
cluster = api.get_cluster(cluster_name)

# Get the IMPALA service
service_list = cluster.get_all_services()
for service in service_list:
    # print( service.name +"  "+service.type
    if service.type == "IMPALA":
        impala_service = service
        print( "Located Impala Service: " + service.name)
        break

if impala_service is None:
    print( "Error: Could not locate Impala Service")
    quit(1)

# A window of one day assumes queries have not been running more than 24 hours
tz = pytz.timezone('Asia/Shanghai')
now = datetime.now()
start = now - timedelta(hours=24)
print( "Looking for Impala queries running more than " + str(queryRunningSeconds) + " seconds")

if kill:
    print( "Queries will be killed")

filterStr = 'query_duration > ' + queryRunningSeconds + 's'
print( "startTime: " + str(start) + " endTime: " + str(now))
impala_query_response = impala_service.get_impala_queries(
    start_time=start, end_time=now, filter_str=filterStr, limit=1000)
queries = impala_query_response.queries

longRunningQueryCount = 0

for i in range(0, len(queries)):
    query = queries[i]
    # if the queryState is EXCEPTION and query.endTime is equal to None, which meams this query is run for a long time and consume too much cluster resources.
    # so we should cancle those query and release resouces manully.
    if query.queryState == 'EXCEPTION' and query.endTime == 'None':

        longRunningQueryCount = longRunningQueryCount + 1
        if longRunningQueryCount == 1:
            print( '-- long running queries -------------')

        print( "queryState : " + query.queryState)
        print( "queryId: " + query.queryId)
        print( "endTime: " + str(query.endTime))
        print( "startTime: " + (query.startTime + timedelta(hours=8)).strftime(fmt))
        query_duration = now - query.startTime
        print( "query running time (hour): " + str((query_duration.seconds - 28800) / 3600))
        print( "SQL: " + query.statement)
        if kill:
            print( "Attempting to kill query...")
            impala_service.cancel_impala_query(query.queryId)

        print( '-------------------------------------')

print( longRunningQueryCount)
if longRunningQueryCount == 0:
    print( "No queries found")

print( "done")
