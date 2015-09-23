#!
DEVSITEID=$1
MEETUPID=$2
NOW=`date +%Y-%m-%d`
./getdata1.py --group $DEVSITEID | ./process2_developersgoogle.py > reconcile_${MEETUPID}_DEVSITE.csv

# this will take some time since event-markers.public does not seem to support the group parameter
#./getdata1.py --link https://developers.google.com/events/event-markers.public --group $DEVSITEID | ./process2_developersgoogle.py >> reconcile_${MEETUPID}_DEVSITE.csv
# or use a stored version
cat alltags.json| ./process2_developersgoogle.py --group $DEVSITEID --style tags >> reconcile_${MEETUPID}_DEVSITE.csv

./getmetrics.sh  $MEETUPID |./parsejson.py $MEETUPID > reconcile_${MEETUPID}_MEETUP.csv
./reconcile.py reconcile_${MEETUPID}_MEETUP.csv reconcile_${MEETUPID}_DEVSITE.csv |sort  |tee reconcile_${MEETUPID}_REPORT_$NOW.csv

