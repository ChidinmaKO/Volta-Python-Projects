from flask import Blueprint, current_app, redirect, render_template, request
from isodate import parse_duration
import requests


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    videos = list()
    if request.method == 'POST':

        video_ids = list()
        search_params = {
            'key': current_app.config['YOUTUBE_API_KEY'],
            'q': request.form.get('query'),
            'part': 'snippet',
            'maxResults': 9,
            'type': 'video',
        }

        try:
            search_results = requests.get(search_url, params=search_params).json()['items']
        except:
            return None
        
        for result in search_results:
            video_ids.append(result['id']['videoId'])

        if request.form.get('submit') == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={video_ids[0]}')


        video_params = {
            'key': current_app.config['YOUTUBE_API_KEY'],
            'id': ','.join(video_ids),
            'part': 'snippet,contentDetails',
            'maxResults': 9,
        }

        try:
            video_results = requests.get(video_url, params=video_params).json()['items']
        except:
            return None

        for result in video_results:
            video_data = {
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={result["id"]}',
                'thumbnail': result['snippet']['thumbnails']['high']['url'],
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'title': result['snippet']['title'],
            }

            videos.append(video_data)

    return render_template('index.html', videos=videos)