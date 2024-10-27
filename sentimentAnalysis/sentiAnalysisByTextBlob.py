from textblob import TextBlob
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

# loading environment to access variables
load_dotenv(find_dotenv())
password = os.environ.get('MONGODB_PWD')
url="mongodb+srv://mahagn118:{}@moviecluster.sdfmk.mongodb.net/moviedb?retryWrites=true&w=majority&appName=moviecluster".format(password)
# MongoDB connection setup
client = MongoClient(url)
# print(client, ' -----------')
db = client['moviedb']
collection = db['tmovie']

movies = []
for mov in collection.find({"language": 'tamil'}):
    movies.append(mov)

def analyze_review_sentiment(review_text):
    analysis = TextBlob(review_text)
    return analysis.sentiment.polarity  # Polarity: -1 (negative) to 1 (positive) and 0 is neutral

def rank_movies(movies):
    ranked_movies = []

    for movie in movies:
        total_sentiment = 0
        review_count = 0
        for review in movie['review']:
            sentiment = analyze_review_sentiment(review)
            total_sentiment += sentiment
            review_count += 1

        # Calculate the average sentiment score
        avg_sentiment = total_sentiment / review_count if review_count > 0 else 0
        ranking_score = avg_sentiment
        # we can consider user ratings also here. we can divide user ratings by 10 and add it to the avg_sentiment.

        movie['ranking_score'] = ranking_score
        ranked_movies.append(movie)

    # Sort movies based on ranking score (highest first)
    ranked_movies.sort(key=lambda x: x['ranking_score'], reverse=True)

    return ranked_movies

# Rank the movies based on reviews and print the top-ranked ones
ranked_movies = rank_movies(movies) #  we consume this time to show in Front end.

for movie in ranked_movies:
    print(f"Title: {movie['title']}, Avg Sentiment Score: {movie['ranking_score']:.2f}")