#!/usr/bin/env python3

## #!/usr/bin/env python

import sys
import json
import csv
import time
from datetime import datetime

jsonresult=json.load(sys.stdin)
csvwriter=csv.writer(sys.stdout)

file=open("idlog.txt","w")
#csvwriter2=csv.writer(open("idlog.csv","w"))

tag="tag"
if len(sys.argv) > 1:
    tag=sys.argv[1]


# print type(jsonresult)

# first pass to get all headers
firsttime=True
headers=['tag']
rows=[tag]
for item in jsonresult:
    #print item
    if isinstance(jsonresult[item],list):
        for item2 in jsonresult[item]:
            # print 'list',len(item2)
            for item3 in item2:
                #print (item3,item2[item3])
                #rows+=[str(item2[item3])]
                if not item3 in headers:
                    #print ("adding", item3)
                    headers+=[item3]
            #csvwriter.writerow(rows)
            #rows=[]
            #firsttime=False

# list1=['utc_offset','rsvp_limit','announced','how_to_find_us','name','visibility','waitlist_count','description','yes_rsvp_count','maybe_rsvp_count','updated','id','why','rating','event_url','venue','headcount','group','time','status','fee','photo_url','created','duration']

# simpler list
list1=['name','yes_rsvp_count','event_url','time','status','description']
# csvwriter.writerow(headers)
headerlist1=['tag']+list1

# Write header
csvwriter.writerow(headerlist1)

rows=[tag]
map1={}
for item in jsonresult:
    #print item
    if isinstance(jsonresult[item],list):
        for item2 in jsonresult[item]:
            # print 'list',len(item2)
            for item3 in item2:
                #print (item3,item2[item3])
                #rows+=[str(item2[item3])]
                if item3 in ['id']:
                    print(item2[item3],file=file)

                if item3 in ['time','updated','created']:
                    #map1[item3]=datetime.strftime(time.gmtime(int(item2[item3])/1000),'%m/%d/%Y %I:%M:%S %p')
                    map1[item3]=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(int(item2[item3])/1000))
                    #'%Y-%m-%dT%H:%M:%SZ'
                else:
                    map1[item3]=str(item2[item3]).replace('\n',' ').replace('\r',' ')

            # for item4 in headers:
# use hardcoded list from all meetup groups.  the union of all the column names, we hope.
            for item4 in list1:
                if item4 in map1:
                    rows+=[map1[item4]]
                else:
                    rows+=['']

            csvwriter.writerow(rows)
            rows=[tag]
            map1={}

