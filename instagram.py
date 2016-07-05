import requests
import json
from operator import itemgetter

client_id = 'b2ad1e4397e74a01bebe074f03d59a55'
client_secret = 'cf9f078c478848bcaaaea4d802073d2e'
access_token = '1604585272.26f8b10.0e5c88deb944408e8ec7976c0c696d26'
tag_search_url = 'https://api.instagram.com/v1/tags/search?q={tag}&access_token={access_token}'

def find_optimal_tag(tag_list):
    """Find top 10 most used related hashtags for each tag in tag_list

    :return List of optimal tags
    """
    optimal_tag = ''
    for arg in tag_list:
        r= requests.get(tag_search_url.format(tag=arg, access_token=access_token))
        jdata = json.loads(r.text)['data']
        sorted_list = sorted(jdata, key=itemgetter('media_count'), reverse=True)
        for c in sorted_list[0:10]:
            optimal_tag += ' #' + c['name']

    return optimal_tag
