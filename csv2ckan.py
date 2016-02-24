import csv
from datetime import datetime
import json
import urllib2

with open('/home/deploy/bin_script/statistics/stats.csv', 'rb') as f:
    reader = csv.reader(f)
    csvarray = list(reader)
auth_key = 'xxxx'

i = datetime.now()
date=i.strftime('%Y/%m/%d %H:%M:%S')


#'{"resource": {"package_id": "{PACKAGE-ID}"}, "fields": [ {"id": "a"}, {"id": "b"} ], 
#"records": [ { "a": 1, "b": "xyz"}, {"a": 2, "b": "zzz"} ]}'

url = "http://www.odaa.dk/api/3/action/"
datastore_structure="{\"resource_id\":\"39e34b41-b1e6-42b3-9899-084ad17cabdf\",\"force\":\"true\"}"

headers = {'content-type': 'application/json', 'Authorization': auth_key}
ds = json.loads(datastore_structure)
req = urllib2.Request(url + 'datastore_delete',data=json.dumps(ds),  headers=headers)
try:
        response = urllib2.urlopen(req)
except urllib2.URLError as e:
        pass
#finally:
#       response.close()

datastore_structure = """{"resource_id": "39e34b41-b1e6-42b3-9899-084ad17cabdf",
                      "fields":[{"id": "date"},{"id":"dataset_id"}, {"id": "name"}, {"id": "total"}, {"id": "recent"}],
                      "records":["""    
for y in range(1, len(csvarray)):
        datastore_structure +="""{"date": "%s","dataset_id":"%s", "name": "%s", "total": "%s", "recent": "%s"},""" % (date,csvarray[y][0],csvarray[y][1],csvarray[y][2],csvarray[y][3])
datastore_structure = datastore_structure[:-1]
datastore_structure +="""],"force":"true"}"""
ds = json.loads(datastore_structure)

headers = {'content-type': 'application/json', 'Authorization': auth_key}
req = urllib2.Request(url + 'datastore_create', data=json.dumps(ds), headers=headers)
response = urllib2.urlopen(req)
