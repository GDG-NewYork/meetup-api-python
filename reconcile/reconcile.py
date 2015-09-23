#!/usr/bin/env python3
import sys
import csv
import time
from datetime import datetime

csvwriter = csv.writer(sys.stdout)

if len(sys.argv) < 2:
    print ('usage: file1 file2')
    sys.exit(100)


#time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime(int(item2[item3])/1000))
# 2015-03-12 18:00:00-04:00 GDG New York Android Study Jam 
# 2015-03-12T22:00:00Z

# assume groups are run one at a time!!!
# for example, gdg-nyc is the only data passed in
TAG='missing-tag'
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['time'],row['tag'],row['name'])
        #print(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime(row['time'],'%Y-%m-%dT%H:%M:%SZ')),row['tag'],row['name'],row['yes_rsvp_count'],row['event_url'])
        TAG=row['tag']
        csvwriter.writerow([time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime(row['time'],'%Y-%m-%dT%H:%M:%SZ')),row['tag'],row['name'],row['yes_rsvp_count'],row['event_url']])

with open(sys.argv[2]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['start'],row['title'])
        #print(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime((row['start'])[:-6],'%Y-%m-%d %H:%M:%S')),'DEV-SITE',row['title'],row['participantsCount'],row['url'])
        # csvwriter.writerow([time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime((row['start'])[:-6],'%Y-%m-%d %H:%M:%S')),'%s:DEV-SITE'%TAG,row['title'],row['participantsCount'],row['url']])
        #print((row['start'])[:-3])
        #print((row['start'])[-2:])
        #print('%s%s' % ((row['start'])[:-3],(row['start'])[-2:]))
        # csvwriter.writerow([time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time.mktime(time.strptime(('%s%s' % ((row['start'])[:-3],(row['start'])[-2:])),'%Y-%m-%d %H:%M:%S%z')))),'%s:DEV-SITE'%TAG,row['title'],row['participantsCount'],row['url']])
# =======
        try:
            csvwriter.writerow([time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime((row['start'])[:-6],'%Y-%m-%d %H:%M:%S')),'%s:DEV-SITE'%TAG,row['title'],row['participantsCount'],row['url'],row['url2']])
        except Exception as e:
            try:
                csvwriter.writerow([time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime((row['start']),'%Y-%m-%d %H:%M:%S')),'%s:DEV-SITE'%TAG,row['group'],row['timezoneName']])
            except Exception as e:
                print ('issue:',sys.argv[0],e)
                pass

