#!/usr/bin/env python3
import sys
import json
import csv
import datetime

objectin = json.load(sys.stdin)
csvwriter = csv.writer(sys.stdout)
MISSING_participantsCount=-1

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--style", help="print style 'tags' or default")
parser.add_argument("--group", help="group number")
args = parser.parse_args()
#print(args)
#print(args.link)
# sys.exit(1)

# if len(sys.argv) > 1:
#     #print (sys.argv[1])
#     group='&group=%s'%sys.argv[1]
#     #pass
#sys.exit(1)
style='default'
if args.style != None:
    style=args.style
group=None
if args.group != None:
    group=args.group

# header
csvwriter.writerow( ['group','start','timezoneName', 'participantsCount','id','url', 'title','url2'])

for item in objectin:
    #print (type(item), len(item))
    for item2 in item:
        #print (type(item2), len(item2))
        # print (item2)
        # sys.exit(1)
#       {
#           'description': 'Catch up session for Week 1 ',
#           'title': 'GDGHV [Android Study Jam] Session 1 @Hangout',
#           'percentWomen': 1,
#           'link': '/events/5921030836060160/',
#           'participantsCount': 8,
#           'temporalRelation': 'past',
#           'start': '08 Feb 2015 21:00 -0500',
#           'timezoneName': 'America/New_York',
#           'id': '5921030836060160',
#           'iconUrl': '/_static/images/gdg-icon.png',
#           'location': 'Beacon, NY, United States',
#           'end': '08 Feb 2015 22:00 -0500',
#           'group': '116637480947982055865'
#       }
#       {
#          "tags" : [
#             "cloudplatform",
#             "gdg",
#             "bigquery"
#          ],
#          "timezone_name" : "US/Eastern",
#          "latlng" : {
#             "lng" : -74.003128,
#             "lat" : 40.741254
#          },
#          "organizers" : [
#             {
#                "first_name" : "Ralph",
#                "display_name" : "Ralph Yozzo",
#                "last_name" : "Yozzo",
#                "plusone_url" : "https://plus.google.com/+RalphYozzo"
#             }
#          ],
#          "percentWomen" : 10,
#          "group" : "102033742326416578905",
#          "location" : "Google, Ninth Avenue, New York, NY, United States",
#          "start" : 1437741900,
#          "name" : "Google Cloud Platform Fundamentals Training (Invite-Only GDG Session)",
#          "end" : 1437745500,
#          "gplusEventUrl" : "",
#          "participantsCount" : 113,
#          "description" : "http://www.meetup.com/NYC-GDG/events/223919361/",
#          "defaultEventUrl" : "/events/6282154198171648/",
#          "registration_link" : null
#       },
        # 'start': '08 Feb 2015 21:00 -0500',
        start = 'MISSING-start'

        try: 
            start = ( datetime.datetime.strptime(item2['start'], "%d %b %Y %H:%M %z"))
        except Exception as e:
            try:
                start = datetime.datetime.strftime(datetime.datetime.fromtimestamp(item2['start']),"%Y-%m-%d %H:%M:%S")
            except Exception as e:
                print ('issue',e)
                pass
        # sys.exit(1)

        if style=='tags':
            try:
                if group:
                    if group == item2['group']:
                        csvwriter.writerow([ item2['group'],start,item2['tags']])
                else:
                    csvwriter.writerow([ item2['group'],start,item2['tags']])
            except Exception as e:
                pass

        else:
            try:
                csvwriter.writerow([ item2['group'],start,item2['timezoneName'], item2['participantsCount'],item2['id'],'https://developers.google.com/events/manage/%s/postevent/' % item2['id'], item2['title'], 'https://developers.google.com/events/editevent/%s/' % item2['id']])
            except Exception as e:
                try:
                    # print '222',item2['group'],start,item2['timezoneName'], "MISSING"
                    if 'group' not in item2:
                        csvwriter.writerow( ['MISSING-group',start,'','',item2['id'],'https://developers.google.com/events/manage/%s/postevent/' % item2['id'], item2['title']])
                    elif 'participantsCount' in item2 and 'timezoneName' not in item2:
                        csvwriter.writerow( [item2['group'],start,'MISSING-timezoneName',item2['participantsCount'],item2['id'],'https://developers.google.com/events/manage/%s/postevent/' % item2['id'], item2['title']])
                    elif 'participantsCount' not in item2 and 'timezoneName' in item2:
                        csvwriter.writerow( [item2['group'],start,item2['timezoneName'], MISSING_participantsCount,item2['id'],'https://developers.google.com/events/manage/%s/postevent/' % item2['id'], item2['title']])
                    elif 'participantsCount' not in item2 and 'timezoneName' not in item2:
                        csvwriter.writerow( [item2['group'],start,'MISSING-timezoneName', MISSING_participantsCount,item2['id'],'https://developers.google.com/events/manage/%s/postevent/' % item2['id'], item2['title']])
                    else:
                        # both participantsCount and timezoneName are present
                        csvwriter.writerow([ item2['group'],start,item2['timezoneName'], item2['participantsCount'],item2['id'],'https://developers.google.com/events/manage/%s/postevent/' % item2['id'], item2['title']])
                except Exception as e:
                    try: 
                        csvwriter.writerow( [item2['group'], 'QQQ: issue:',e,item2 ])
                        #print 'QQQ: issue:',e,item2
                    except Exception as e:
                        csvwriter.writerow( ['QQQ: issue:',e,item2 ])


