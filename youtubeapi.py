
from apiclient.discovery import build
from apiclient.errors import HttpError
import re
import django
from datetime import date
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contents.settings")
django.setup()
from youtube.models import Youtube
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyD0aUxTY3pv4zs6KgOZeJmcrpXG0Z4IGKo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.videos().list(
        part="id,snippet",
        maxResults=10,
        chart="mostPopular",
        regionCode='kr'
    ).execute()

    url = []
    categori = []
    name = []
    thumbnail= []
    channel=[]
    you='youtube.com/watch='
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    print(search_response.get("items", [])[0])

    for search_result in search_response.get("items", []):
        thumbnail.append(search_result['snippet']['thumbnails']['default']['url'])
        name.append(search_result['snippet']['title'])
        channel.append(search_result['snippet']['channelTitle'])
    
        categori.append(search_result['snippet']['categoryId'])
        url.append(you+search_result['id'])
        
    
    contents=list(zip(url,categori,name,thumbnail,channel))
    for i in contents:
        print(i)
        print()
    return contents

def db_save(contents):
    for url,categori,name,thumbnail,channel in contents:
        obj=Youtube(name=name,url=url,image=thumbnail,category=categori,channel=channel)
        obj.save()


contents=youtube_search()
db_save(contents)

