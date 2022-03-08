import requests
from pprint import pprint
import os

from model import Watch_list

my_api_key = os.environ['API_KEY']



api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'

def search_movie(search_query):
    '''SEARCHES FOR A MOVIE'''

    endpoint_path = f'/search/movie'
    print(f'Okay, searching for {search_query}')
    endpoint = f'{api_base_url}{endpoint_path}?api_key={my_api_key}&query={search_query}'
    r=requests.get(endpoint)



    if r.status_code in range(200,299):
        data=r.json()
        results= data['results']
        if len(results) > 0:
            print(results[0].keys())
            movies_info = []
            for result in results:
                _id = result['id']
                title =result['title']
                movies_info.append({
                    'id': _id,
                    'title': title
                })
            return movies_info
        else: #results are not greater than 0
            return []
    else:
        return(f'{r.status_code} status code')

def get_movie_name_by_id(id):
    '''Gets a movie from the watch_list given its ID.'''
    endpoint_path = f'/movie/{id}'
    #https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
    endpoint = f'{api_base_url}{endpoint_path}?api_key={my_api_key}'
    r=requests.get(endpoint)

    if r.status_code in range(200,299):
        data=r.json()
        return {'title' :data['title'], 'id': data['id'], 'overview': data['overview']}
    else:
        return(f'{r.status_code} status code')





