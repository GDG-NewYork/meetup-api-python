#!
NAME=meetup-gdg-data-`date +%Y%m%d`.csv
echo tag,utc_offset,rsvp_limit,announced,how_to_find_us,name,visibility,waitlist_count,description,yes_rsvp_count,maybe_rsvp_count,updated,id,why,rating,event_url,venue,headcount,group,time,status,fee,photo_url,created,duration >$NAME
./runit.sh  GDG-Google-Developer-Group-Schaumburg >> $NAME
./runit.sh  NYC-GDG >> $NAME
./runit.sh  gdg-silicon-valley >> $NAME
./runit.sh  gdg-boston >> $NAME
./runit.sh  gdg-paris >> $NAME
