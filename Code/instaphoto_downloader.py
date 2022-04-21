import requests
import re

#Get the response for the request
def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})

#Take the instagram user input
url = input("Enter Instgram URL: ")
response = get_response(url)

#Match the pattern to get the URLs
vid_matches = re.findall('"video_url":"([^"]+)"', response)
pic_matches = re.findall('"display_url":"([^"]+)"', response)


vid_urls = prepare_urls(vid_matches)
pic_urls = prepare_urls(pic_matches)

#Print a list of URLs
if vid_urls:
    print('Detected Videos:\n{0}'.format('\n'.join(vid_urls)))

if pic_urls:
    print('Detected Pictures:\n{0}'.format('\n'.join(pic_urls)))

if not (vid_urls or pic_urls):
    print('Could not recognize the media in the provided URL.')