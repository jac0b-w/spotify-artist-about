import urllib.request
from html.parser import HTMLParser
import json

def get_html(link):
    fp = urllib.request.urlopen(link)
    mybytes = fp.read()
    html = mybytes.decode("utf8")
    fp.close()
    
    return html

def artist_about(artist_id, remove_bio_tags = True):
    link = f'https://open.spotify.com/artist/{artist_id}/about'

    data_array = []
    class parser(HTMLParser):
        def handle_data(self, encountered_data):
            data_array.append(encountered_data)

    obj = parser()
    obj.feed(get_html(link))

    data = data_array[-4]
    data = data[data.find('Spotify.Entity = {')+17:-(data[::-1].find('}'))]
    data = json.loads(data)

    if remove_bio_tags:
        data['insights']['biography'] = remove_tags(data['insights']['biography'])

    return data

def remove_tags(text):
    bio = []
    class parser(HTMLParser):
        def handle_data(self, data):
            bio.append(data)

    obj = parser()
    obj.feed(text)

    string = ''
    for section in bio:
        string += section
    return string

def print_keys(dic,offset = 0):
    if type(dic) == dict:
        for key in dic:
            print(str(' '*offset*3)+str(key))
            print_keys(dic[key],offset = offset+1)