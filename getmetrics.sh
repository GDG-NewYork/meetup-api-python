#!
# KEY=PUT-YOUR-MEETUP-APIKEY-HERE
#  see https://secure.meetup.com/meetup_api/key/

if [ -z "$KEY" ]; then
    echo You must set API KEY
    exit
fi
curl "https://api.meetup.com/2/events?status=past%2Cupcoming&order=time&limited_events=False&group_urlname=$1&desc=false&offset=0&photo-host=public&format=json&page=200&fields=&key=$KEY"
