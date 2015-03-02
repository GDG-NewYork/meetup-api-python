#!/usr/bin/env python3

import sys
import json
import csv
import time

jsonresult=json.load(sys.stdin)
csvwriter=csv.writer(sys.stdout)

tag="tag"
if len(sys.argv) > 1:
    tag=sys.argv[1]

rows=[tag]

# list of all column names that we know about from meetup api.  feel free to add more.

list1=['utc_offset','rsvp_limit','announced','how_to_find_us','name','visibility','waitlist_count','description','yes_rsvp_count','maybe_rsvp_count','updated','id','why','rating','event_url','venue','headcount','group','time','status','fee','photo_url','created','duration']
headerlist1=['tag']+list1
rows=[tag]
map1={}

for item in jsonresult:
    if isinstance(jsonresult[item],list):
        for item2 in jsonresult[item]:
            for item3 in item2:

                if item3 in ['time','updated','created']:
                    map1[item3]=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(int(item2[item3])/1000))
                else:
                    map1[item3]=str(item2[item3]).replace('\n',' ').replace('\r',' ')

            for item4 in list1:
                if item4 in map1:
                    rows+=[map1[item4]]
                else:
                    rows+=['']

            csvwriter.writerow(rows)
            rows=[tag]
            map1={}

