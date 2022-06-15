URL="<your discord webhook url>"
#command syntax example: ./discord-notif.sh Todd "Garage opening"


USERNAME=$1
CONTENT=$2

JSON_STRING=$( jq -n \
                  --arg username "$USERNAME" \
                  --arg content "$CONTENT" \
                  '{username: $username, content: $content}' )



echo $JSON_STRING | \
python -m json.tool  | \
curl -X POST -d @- -H 'Content-Type: application/json' $URL
