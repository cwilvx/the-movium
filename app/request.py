import urllib.request,json
from .models import Movie,Genres

api_key = None
base_url = None
similar_url = None
genres_url = None
genre_movies_url = None
collection_url = None

def configure_request(app):
    global api_key,base_url,similar_url,genres_url,genre_movies_url,collection_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    similar_url = app.config['SIMILAR_URL']
    genres_url = app.config['GENRES_URL']
    genre_movies_url = app.config['GENRE_MOVIES_URL']
    # collection_url = app.config['COLLECTION_URL']

def get_genres():
    get_genres_url = genres_url.format(api_key)
    with urllib.request.urlopen(get_genres_url) as url:
        get_genres_data = url.read()
        get_genres_response = json.loads(get_genres_data)
        
        genres_results = None
        
        if get_genres_response['genres']:
            genres_results_list = get_genres_response['genres']
            genres_results = process_genres_results(genres_results_list)
        
    return genres_results
def process_genres_results(genres_results_list):
    genres_results = []
    for genre_item in genres_results_list:
        id = genre_item.get('id')
        name = genre_item.get('name')
        genre_object = Genres(id,name)
        genres_results.append(genre_object)
    return genres_results

def get_movies(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

def get_similar_movies(id):
    get_movies_url = similar_url.format(id,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')
            genres = movie_details_response.get('genres')
            backdrop = movie_details_response.get('backdrop_path')
            collection = movie_details_response.get('belongs_to_collection')
            budget = movie_details_response.get('budget')
            homepage = movie_details_response.get('homepage')
            date = movie_details_response.get('release_date')
            languages = movie_details_response.get('spoken_languages')
            status = movie_details_response.get('status')
            tag = movie_details_response.get('tagline')
            revenue = movie_details_response.get('revenue')
            f_revenue = f"{revenue:,.2f}"
            f_budget = f"{budget:,.2f}"
            b_collection = collection
            
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count,genres,backdrop,budget,collection,homepage,date,languages,status,tag,revenue,f_revenue,f_budget,b_collection)

    return movie_object

def get_genre_movies(id):
    get_genre_movies_url = genre_movies_url.format(api_key,id)
    with urllib.request.urlopen(get_genre_movies_url) as url:
        genre_movies_data = url.read()
        genre_movies_response = json.loads(genre_movies_data)

        genre_movies_results = None

        if genre_movies_response['results']:
            genre_movies_list = genre_movies_response['results']
            genre_movies_results = process_results(genre_movies_list)
            
    return genre_movies_results
    
# def get_collection(id):
#     get_collection_url = collection_url.format(id,api_key)
#     with urllib.request.urlopen(get_collection_url) as url:
#         collection_movies_data = url.read()
#         collection_movies_response = json.loads(collection_movies_data)
        
#         collection_movies_result = None
        
#         if collection_movies_response['results']:
#             collection_movies_list = collection_movies_response['results']
#             collection_movies_result = process_collections(collection_movies_list)
#     return collection_movies_result

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results

def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        genres = movie_item.get('genres')
        backdrop = movie_item.get('backdrop_path')
        budget = movie_item.get('budget')
        collection = movie_item.get('belongs_to_collection')
        homepage = movie_item.get('homepage')
        date = movie_item.get('release_date')
        languages = movie_item.get('spoken_languages')
        status = movie_item.get('status')
        tag = movie_item.get('tagline')
        revenue = movie_item.get('revenue')
        f_revenue = 'revenue'
        f_budget = 'budget'
        b_collection = collection
        
        if backdrop:

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count,genres,backdrop,budget,collection,homepage,date,languages,status,tag,revenue,f_revenue,f_budget,b_collection)
            movie_results.append(movie_object)

    return movie_results

# def process_collections(movie_list):
