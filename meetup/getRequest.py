import requests
#url = 'https://api.meetup.com/2/events?key=573a542e312d45534327c1a592f16c&group_urlname=ny-tech&sign=true'
#resp = requests.get(url)
#if resp.status_code != 200:
#    print (":(")

r = requests.get('https://api.meetup.com/2/events?offset=0&format=json&limited_events=False&group_urlname=ny-tech&page=200&fields=&order=time&desc=false&status=upcoming&sig_id=217552102&sig=14f182e3a6ebb409a5dd7c16aa2411ec3dea2f94')
print r.json()
