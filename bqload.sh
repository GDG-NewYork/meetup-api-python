#!
bq --project YOUR-BIGQUERY-GOOGLE-PROJECT-HERE load --skip_leading_rows 1 gdg.meetup $1  tag:string,utc_offset:string,rsvp_limit:integer,announced:string,how_to_find_us:string,name:string,visibility:string,waitlist_count:integer,description:string,yes_rsvp_count:integer,maybe_rsvp_count:integer,uptimestampd:timestamp,id:string,why:string,rating:string,event_url:string,venue:string,headcount:integer,group:string,time:timestamp,status:string,fee:string,photo_url:string,created:timestamp,duration:integer

