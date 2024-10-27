import requests
from bs4 import BeautifulSoup

TMOVIES_URL = 'https://letterboxd.com/films/ajax/popular/genre/tamil/'
BASE_URL = 'https://letterboxd.com'
# this function get all tamil movie urls.
def get_tmovie_links():
    movie_links = []
    tmovie_Page = requests.get(TMOVIES_URL)
    soup = BeautifulSoup(tmovie_Page.text, 'html.parser')
    
    # getting all movie urls
    for a_tag in soup.find_all('a', class_='frame has-menu'):
        movie_links.append(BASE_URL + a_tag['href'])
    
    return movie_links

def scrape_movie_data(movie_url):
    # this fun is uded to get all the individual tamil movies data and reviews

    tmovie_data = {}
    tmovie_page = requests.get(movie_url)
    soup = BeautifulSoup(tmovie_page.text, 'html.parser')
    
    # Extract metadata
    tmovie_data['title'] = soup.find('span', class_="name js-widont prettify").text.strip()
    tmovie_data['originalname'] = soup.find('h2', class_="originalname").text.strip()
    tmovie_data['rating'] = soup.find('a', class_="tooltip display-rating").text.strip()
    tmovie_data['genre'] = [genre.text for genre in soup.find_all('a', class_='text-slug')]
    
    # Extract reviews (this will vary depending on the structure of Letterboxd's review section)
    reviews = []
    for review_div in soup.find_all('div', class_='collapsed-text'):
        reviews.append({
            'review_text': review_div.find('p').text.strip(),
            'user_likes': review_div.find('a', class_='count').text.strip() if review_div.find('span', class_='rating') else None # if we don't find any review then do nothing.
        })
    
    tmovie_data['reviews'] = reviews
    
    return tmovie_data

def scrape_all_movie_data_reviews():
    all_movie_data = []
    
    for movie_url in movie_links:
        movie_data = scrape_movie_data(movie_url)
        all_movie_data.append(movie_data)
    
    return all_movie_data

movie_links = get_tmovie_links()
# Start scraping process
movies = scrape_all_movie_data_reviews()
print(movies)