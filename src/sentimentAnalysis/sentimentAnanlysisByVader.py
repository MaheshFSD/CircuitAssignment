from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# loading environment to access variables
load_dotenv(find_dotenv())
password = os.environ.get('MONGODB_PWD')
url="mongodb+srv://mahagn118:{}@moviecluster.sdfmk.mongodb.net/moviedb?retryWrites=true&w=majority&appName=moviecluster".format(password)

# MongoDB connection setup
client = MongoClient(url)

db = client['moviedb']
collection = db['tmovie']


# movies = []
# # Assigning movie data to movies
# for mov in collection.find({"language": 'tamil'}):
#     movies.append(mov)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# fetching movies from db to movies
def fetch_movies():
    movies = collection.find({"language": "tamil"}).to_list(length=None)
    return movies

# calculates avg sentiment
def analyze_sentiment(movie):
    reviews = movie.get('review', [])
    total_score = sum(analyzer.polarity_scores(review)['compound'] for review in reviews)
    avg_sentiment = total_score / len(reviews) if reviews else 0
    movie['avg_sentiment'] = avg_sentiment
    return movie

# ranks all the movies based on it sentiment  and sorts them from assending to descending 
def rank_movies():
    # Step 1: Fetch movies
    movies = fetch_movies()
    # print("-------------- inside rank movies -------------")
    # Step 2: Perform sentiment analysis concurrently
    ranked_movies =[analyze_sentiment(movie) for movie in movies]

    # Step 3: Sort movies by average sentiment score in descending order
    ranked_movies = sorted(ranked_movies, key=lambda x: x['avg_sentiment'], reverse=True)
    
    # Output the ranked movies
    for movie in ranked_movies:
        print(f"Title: {movie['title']}, Avg Sentiment Score: {movie['avg_sentiment']:.2f}")

rank_movies()
