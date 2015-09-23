#!/usr/bin/env python3
import sys
import json
import time
import csv
import requests


# https://google-developers.appspot.com/events/event-markers.public   parameters tag start end
# https://developers.google.com/events/event-markers.public   parameters tag start end
# link= "https://developers.google.com/events/feed/json?start=%s&end=%s%s" % (now,end,group)
linkparm = "https://developers.google.com/events/feed/json?start=%s&end=%s%s"

group=''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--link", help="link to use to get data")
parser.add_argument("--group", help="group number to constrain search")
args = parser.parse_args()
#print(args)
#print(args.link)
# sys.exit(1)

# if len(sys.argv) > 1:
#     #print (sys.argv[1])
#     group='&group=%s'%sys.argv[1]
#     #pass
#sys.exit(1)

if args.group != None:
    group='&group=%s'%args.group
#print(group)
if args.link != None:
    linkparm=args.link+'?start=%s&end=%s%s'
# sys.exit(1)


now=(int(time.time())+(300*24*60*60))
realnow=(int(time.time()))-(100*24*60*60)
list1=[]

while now > 0:
    # subtract 16 weeks
    #print (now)
    end = now
    now = now - (60*60*24*7*16)
    # link= "https://developers.google.com/events/feed/json?start=%s&end=%s%s" % (now,end,group)
    link= linkparm % (now,end,group)
    r = requests.get(link)
    print (link,file=sys.stderr)
    # json.dump(sys.stdout,r.json())
    # print(type(r.json()))
    print (now,len(r.json()),file=sys.stderr)
    list1 += [r.json()]
    if len(r.json()) == 0 and now < realnow:
        break
    # sys.exit(1)
print(json.dumps(list1))
