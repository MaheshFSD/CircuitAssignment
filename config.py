from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
import mongoengine as db

load_dotenv(find_dotenv())
password = os.environ.get('MONGODB_PWD')
url="mongodb+srv://mahagn118:{}@moviecluster.sdfmk.mongodb.net/moviedb?retryWrites=true&w=majority&appName=moviecluster".format(password)
client = MongoClient(url)
db = client['moviedb']
movie=db['tmovie']

movie_mock = [
   {
      "id":1,
      "title":"Planes: Fire & Rescue",
      "image_url":"http://dummyimage.com/203x100.png/cc0000/ffffff",
      "genre":"Adventure|Animation|Comedy",
      "language":"tamil",
      "ratings":3.2,
      "release_date":2003,
      "review":[
         "A total waste of time."
      ]
   },
   {
      "id":2,
      "title":"Investigating Sex (a.k.a. Intimate Affairs)",
      "image_url":"http://dummyimage.com/194x100.png/ff4444/ffffff",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":2.7,
      "release_date":2005,
      "review":[
         "This was one of the worst films I've ever seen.",
         "The plot was confusing and poorly executed."
      ]
   },
   {
      "id":3,
      "title":"Camarón: When Flamenco Became Legend",
      "image_url":"http://dummyimage.com/208x100.png/cc0000/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.1,
      "release_date":2012,
      "review":[
         "Boring and lifeless.",
         "The acting was just terrible.",
         "Felt like a waste of time."
      ]
   },
   {
      "id":4,
      "title":"Carne de gallina (Chicken Skin)",
      "image_url":"http://dummyimage.com/212x100.png/5fa2dd/ffffff",
      "genre":"Comedy",
      "language":"tamil",
      "ratings":1.2,
      "release_date":2011,
      "review":[
         "Not worth watching at all.",
         "Absolutely dreadful.",
         "I want my money back."
      ]
   },
   {
      "id":5,
      "title":"Elena and Her Men (Paris Does Strange Things) (Elena et les hommes)",
      "image_url":"http://dummyimage.com/194x100.png/dddddd/000000",
      "genre":"Comedy|Drama|Romance",
      "language":"tamil",
      "ratings":2.4,
      "release_date":2010,
      "review":[
         "The storyline was a mess.",
         "One of the worst movies this year."
      ]
   },
   {
      "id":6,
      "title":"Halfmoon (Paul Bowles - Halbmond)",
      "image_url":"http://dummyimage.com/246x100.png/ff4444/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":3.4,
      "release_date":2009,
      "review":[
         "Couldn't wait for it to end."
      ]
   },
   {
      "id":7,
      "title":"Star!",
      "image_url":"http://dummyimage.com/126x100.png/5fa2dd/ffffff",
      "genre":"Musical",
      "language":"tamil",
      "ratings":3,
      "release_date":2004,
      "review":[
         "The plot was absurd.",
         "It was a snooze fest."
      ]
   },
   {
      "id":8,
      "title":"Drona",
      "image_url":"http://dummyimage.com/135x100.png/dddddd/000000",
      "genre":"Action|Adventure|Fantasy|Musical",
      "language":"tamil",
      "ratings":2.4,
      "release_date":2013,
      "review":[
         "This movie was painful to watch."
      ]
   },
   {
      "id":9,
      "title":"Faces",
      "image_url":"http://dummyimage.com/104x100.png/ff4444/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.7,
      "release_date":2011,
      "review":[
         "The dialogue was cheesy and unbelievable.",
         "Poorly made in every sense."
      ]
   },
   {
      "id":10,
      "title":"Garlic Is As Good As Ten Mothers",
      "image_url":"http://dummyimage.com/133x100.png/ff4444/ffffff",
      "genre":"(no genres listed)",
      "language":"tamil",
      "ratings":2.3,
      "release_date":2019,
      "review":[
         "I can't believe I watched the whole thing."
      ]
   },
   {
      "id":11,
      "title":"Spider-Man 2",
      "image_url":"http://dummyimage.com/224x100.png/ff4444/ffffff",
      "genre":"Action|Adventure|Sci-Fi|IMAX",
      "language":"tamil",
      "ratings":4.8,
      "release_date":2009,
      "review":[
         "It was almost funny how bad it was.",
         "Nothing made any sense."
      ]
   },
   {
      "id":12,
      "title":"Warm Water Under a Red Bridge (Akai hashi no shita no nurui mizu)",
      "image_url":"http://dummyimage.com/134x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":3.9,
      "release_date":2011,
      "review":[
         "Flat characters and uninspired story."
      ]
   },
   {
      "id":13,
      "title":"Thanks for Sharing",
      "image_url":"http://dummyimage.com/184x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":3.9,
      "release_date":2017,
      "review":[
         "Overhyped and underwhelming.",
         "Expected so much more from it."
      ]
   },
   {
      "id":14,
      "title":"Flavor of Green Tea Over Rice (Ochazuke no aji)",
      "image_url":"http://dummyimage.com/161x100.png/cc0000/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":4.5,
      "release_date":0,
      "review":[
         "Poor execution of a promising concept.",
         "The cast did their best, but the story failed them."
      ]
   },
   {
      "id":15,
      "title":"King of Thorn (King of Thorns) (Ibara no O)",
      "image_url":"http://dummyimage.com/216x100.png/5fa2dd/ffffff",
      "genre":"Adventure|Animation|Horror|Sci-Fi|Thriller",
      "language":"tamil",
      "ratings":2.1,
      "release_date":2013,
      "review":[
         "Predictable and clichéd."
      ]
   },
   {
      "id":16,
      "title":"Vai~E~Vem",
      "image_url":"http://dummyimage.com/131x100.png/cc0000/ffffff",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":4.1,
      "release_date":2016,
      "review":[
         "Unmemorable and bland.",
         "No emotional depth whatsoever."
      ]
   },
   {
      "id":17,
      "title":"Your Vice is a Locked Room and Only I Have the Key",
      "image_url":"http://dummyimage.com/175x100.png/cc0000/ffffff",
      "genre":"Horror|Mystery|Thriller",
      "language":"tamil",
      "ratings":1.2,
      "release_date":2005,
      "review":[
         "A complete disappointment."
      ]
   },
   {
      "id":18,
      "title":"Reckless",
      "image_url":"http://dummyimage.com/210x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Fantasy",
      "language":"tamil",
      "ratings":1.9,
      "release_date":2006,
      "review":[
         "Just another mediocre movie."
      ]
   },
   {
      "id":19,
      "title":"By the Sea",
      "image_url":"http://dummyimage.com/121x100.png/ff4444/ffffff",
      "genre":"Comedy",
      "language":"tamil",
      "ratings":1.7,
      "release_date":2020,
      "review":[
         "Could have been good, but missed the mark.",
         "Some scenes were nice, but overall a letdown."
      ]
   },
   {
      "id":20,
      "title":"Execution of P, The (Kinatay)",
      "image_url":"http://dummyimage.com/106x100.png/ff4444/ffffff",
      "genre":"Crime|Thriller",
      "language":"tamil",
      "ratings":4.8,
      "release_date":2016,
      "review":[
         "It was okay, nothing to write home about."
      ]
   },
   {
      "id":21,
      "title":"Superman/Shazam!: The Return of Black Adam (DC Showcase Original Shorts Collection)",
      "image_url":"http://dummyimage.com/104x100.png/cc0000/ffffff",
      "genre":"Action|Adventure|Animation",
      "language":"tamil",
      "ratings":4.4,
      "release_date":2014,
      "review":[
         "Had a couple of decent moments.",
         "A forgettable movie overall."
      ]
   },
   {
      "id":22,
      "title":"Professional, The (Le professionnel)",
      "image_url":"http://dummyimage.com/106x100.png/cc0000/ffffff",
      "genre":"Action|Drama|Thriller",
      "language":"tamil",
      "ratings":1.1,
      "release_date":2009,
      "review":[
         "An average movie, watchable if you’re bored.",
         "Good visuals, weak storyline."
      ]
   },
   {
      "id":23,
      "title":"X: The Man with the X-Ray Eyes",
      "image_url":"http://dummyimage.com/203x100.png/dddddd/000000",
      "genre":"Sci-Fi|Thriller",
      "language":"tamil",
      "ratings":3.1,
      "release_date":2016,
      "review":[
         "Enjoyable in parts, but not something I'd recommend."
      ]
   },
   {
      "id":24,
      "title":"Mummy's Curse, The",
      "image_url":"http://dummyimage.com/186x100.png/ff4444/ffffff",
      "genre":"Horror",
      "language":"tamil",
      "ratings":4.8,
      "release_date":2019,
      "review":[
         "Some fun moments, but the story didn’t hold up."
      ]
   },
   {
      "id":25,
      "title":"Love That Boy",
      "image_url":"http://dummyimage.com/159x100.png/ff4444/ffffff",
      "genre":"Comedy|Romance",
      "language":"tamil",
      "ratings":3.9,
      "release_date":2017,
      "review":[
         "Had potential, but ultimately fell flat."
      ]
   },
   {
      "id":26,
      "title":"Paths of Hate",
      "image_url":"http://dummyimage.com/105x100.png/5fa2dd/ffffff",
      "genre":"Action|Animation|Drama|War",
      "language":"tamil",
      "ratings":2.8,
      "release_date":2014,
      "review":[
         "Good in parts, but forgettable.",
         "Predictable ending."
      ]
   },
   {
      "id":27,
      "title":"Under Capricorn",
      "image_url":"http://dummyimage.com/173x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":4.6,
      "release_date":2004,
      "review":[
         "Enjoyable enough for a lazy weekend."
      ]
   },
   {
      "id":28,
      "title":"La vérité si je mens !",
      "image_url":"http://dummyimage.com/216x100.png/dddddd/000000",
      "genre":"Comedy",
      "language":"tamil",
      "ratings":4.3,
      "release_date":2005,
      "review":[
         "A bit slow, but had a good finish.",
         "Some great visuals but lacking in plot."
      ]
   },
   {
      "id":29,
      "title":"Wreck of the Mary Deare, The",
      "image_url":"http://dummyimage.com/163x100.png/5fa2dd/ffffff",
      "genre":"Drama|Thriller",
      "language":"tamil",
      "ratings":4.7,
      "release_date":2017,
      "review":[
         "Not bad, but not very memorable."
      ]
   },
   {
      "id":30,
      "title":"Smashed",
      "image_url":"http://dummyimage.com/184x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":3,
      "release_date":2010,
      "review":[
         "It was fine for a casual watch.",
         "Could have used better direction."
      ]
   },
   {
      "id":31,
      "title":"Cosmopolis",
      "image_url":"http://dummyimage.com/102x100.png/dddddd/000000",
      "genre":"Drama",
      "language":"tamil",
      "ratings":2.2,
      "release_date":2019,
      "review":[
         "Watchable but won’t stay with you."
      ]
   },
   {
      "id":32,
      "title":"Frozen, The",
      "image_url":"http://dummyimage.com/132x100.png/ff4444/ffffff",
      "genre":"Horror|Thriller",
      "language":"tamil",
      "ratings":1.8,
      "release_date":2020,
      "review":[
         "Decent acting but needed a stronger plot."
      ]
   },
   {
      "id":33,
      "title":"Ernest & Célestine (Ernest et Célestine)",
      "image_url":"http://dummyimage.com/169x100.png/cc0000/ffffff",
      "genre":"Adventure|Animation|Children|Comedy|Drama|Romance",
      "language":"tamil",
      "ratings":2,
      "release_date":2014,
      "review":[
         "A few great scenes, but that’s it."
      ]
   },
   {
      "id":34,
      "title":"People, Places, Things",
      "image_url":"http://dummyimage.com/168x100.png/dddddd/000000",
      "genre":"Comedy",
      "language":"tamil",
      "ratings":2.6,
      "release_date":2004,
      "review":[
         "A bit predictable, but enjoyable.",
         "Solid for a one-time watch."
      ]
   },
   {
      "id":35,
      "title":"Click",
      "image_url":"http://dummyimage.com/248x100.png/cc0000/ffffff",
      "genre":"Adventure|Comedy|Drama|Fantasy|Romance",
      "language":"tamil",
      "ratings":3.5,
      "release_date":2012,
      "review":[
         "Good for background noise.",
         "Nothing groundbreaking, but still fun."
      ]
   },
   {
      "id":36,
      "title":"Carless Love",
      "image_url":"http://dummyimage.com/143x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":4.7,
      "release_date":2014,
      "review":[
         "Had some good moments.",
         "An okay film with some charm."
      ]
   },
   {
      "id":37,
      "title":"Being John Malkovich",
      "image_url":"http://dummyimage.com/146x100.png/cc0000/ffffff",
      "genre":"Comedy|Drama|Fantasy",
      "language":"tamil",
      "ratings":3.6,
      "release_date":2012,
      "review":[
         "Some scenes were really well done.",
         "Could have been tighter in pacing."
      ]
   },
   {
      "id":38,
      "title":"First Man Into Space",
      "image_url":"http://dummyimage.com/165x100.png/dddddd/000000",
      "genre":"Drama|Horror|Sci-Fi",
      "language":"tamil",
      "ratings":1.5,
      "release_date":2010,
      "review":[
         "Decent movie with some surprises.",
         "Better than expected."
      ]
   },
   {
      "id":39,
      "title":"Sucker Punch",
      "image_url":"http://dummyimage.com/156x100.png/cc0000/ffffff",
      "genre":"Action|Fantasy|Thriller|IMAX",
      "language":"tamil",
      "ratings":3.7,
      "release_date":2004,
      "review":[
         "An enjoyable film with a few minor flaws."
      ]
   },
   {
      "id":40,
      "title":"Guys, The",
      "image_url":"http://dummyimage.com/247x100.png/ff4444/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":4.7,
      "release_date":2017,
      "review":[
         "Better than I thought it would be.",
         "A nice surprise overall."
      ]
   },
   {
      "id":41,
      "title":"Erendira",
      "image_url":"http://dummyimage.com/194x100.png/dddddd/000000",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.8,
      "release_date":2009,
      "review":[
         "I liked the characters.",
         "Good performances made it worthwhile."
      ]
   },
   {
      "id":42,
      "title":"Original Sin",
      "image_url":"http://dummyimage.com/194x100.png/dddddd/000000",
      "genre":"Drama|Romance|Thriller",
      "language":"tamil",
      "ratings":2.3,
      "release_date":2020,
      "review":[
         "Pretty entertaining.",
         "Great visuals kept me engaged."
      ]
   },
   {
      "id":43,
      "title":"Take the Lead",
      "image_url":"http://dummyimage.com/130x100.png/dddddd/000000",
      "genre":"Drama",
      "language":"tamil",
      "ratings":2.2,
      "release_date":2012,
      "review":[
         "Good story, but a bit slow in parts."
      ]
   },
   {
      "id":44,
      "title":"Dawn of the Dead",
      "image_url":"http://dummyimage.com/111x100.png/cc0000/ffffff",
      "genre":"Action|Drama|Horror",
      "language":"tamil",
      "ratings":3.5,
      "release_date":2010,
      "review":[
         "The humor worked for me.",
         "Decent film with a fun vibe."
      ]
   },
   {
      "id":45,
      "title":"I Am David",
      "image_url":"http://dummyimage.com/155x100.png/cc0000/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":2.3,
      "release_date":2008,
      "review":[
         "Fun and well-acted.",
         "It had its flaws but still a good watch."
      ]
   },
   {
      "id":46,
      "title":"Three Musketeers, The",
      "image_url":"http://dummyimage.com/231x100.png/ff4444/ffffff",
      "genre":"Action|Adventure|Comedy",
      "language":"tamil",
      "ratings":2.7,
      "release_date":2003,
      "review":[
         "I enjoyed it, though it wasn’t perfect."
      ]
   },
   {
      "id":47,
      "title":"Age of Ignorance, The (a.k.a. Days of Darkness) (L'âge des ténèbres)",
      "image_url":"http://dummyimage.com/190x100.png/ff4444/ffffff",
      "genre":"Comedy|Drama|Fantasy",
      "language":"tamil",
      "ratings":4.5,
      "release_date":2015,
      "review":[
         "A solid movie.",
         "Enjoyed it from start to finish."
      ]
   },
   {
      "id":48,
      "title":"Coming Down the Mountain",
      "image_url":"http://dummyimage.com/165x100.png/dddddd/000000",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.6,
      "release_date":2015,
      "review":[
         "Really fun and enjoyable.",
         "Would recommend to friends."
      ]
   },
   {
      "id":49,
      "title":"7th Cavalry (Seventh Cavalry)",
      "image_url":"http://dummyimage.com/241x100.png/cc0000/ffffff",
      "genre":"Western",
      "language":"tamil",
      "ratings":2.8,
      "release_date":2010,
      "review":[
         "Some nice twists.",
         "A decent film overall."
      ]
   },
   {
      "id":50,
      "title":"Island at War",
      "image_url":"http://dummyimage.com/240x100.png/ff4444/ffffff",
      "genre":"Drama|War",
      "language":"tamil",
      "ratings":2.3,
      "release_date":2015,
      "review":[
         "Good acting, decent story."
      ]
   },
   {
      "id":51,
      "title":"Hair Show",
      "image_url":"http://dummyimage.com/227x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Romance",
      "language":"tamil",
      "ratings":2.6,
      "release_date":2013,
      "review":[
         "Well-made and engaging."
      ]
   },
   {
      "id":52,
      "title":"To Kill a Priest",
      "image_url":"http://dummyimage.com/181x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.2,
      "release_date":2008,
      "review":[
         "A good balance of action and humor."
      ]
   },
   {
      "id":53,
      "title":"The Butterfly Effect",
      "image_url":"http://dummyimage.com/202x100.png/cc0000/ffffff",
      "genre":"Drama|Sci-Fi|Thriller",
      "language":"tamil",
      "ratings":4.4,
      "release_date":2009,
      "review":[
         "An enjoyable watch, worth checking out."
      ]
   },
   {
      "id":54,
      "title":"ZMD: Zombies of Mass Destruction",
      "image_url":"http://dummyimage.com/169x100.png/cc0000/ffffff",
      "genre":"Comedy|Horror",
      "language":"tamil",
      "ratings":1.7,
      "release_date":2020,
      "review":[
         "Impressive cinematography.",
         "Strong performances throughout."
      ]
   },
   {
      "id":55,
      "title":"Passion Flower",
      "image_url":"http://dummyimage.com/219x100.png/dddddd/000000",
      "genre":"Drama",
      "language":"tamil",
      "ratings":3.6,
      "release_date":2004,
      "review":[
         "Solid story and a well-rounded cast."
      ]
   },
   {
      "id":56,
      "title":"Bio Zombie (Sun faa sau si)",
      "image_url":"http://dummyimage.com/195x100.png/cc0000/ffffff",
      "genre":"Comedy|Horror",
      "language":"tamil",
      "ratings":4,
      "release_date":2004,
      "review":[
         "Better than expected.",
         "Would definitely recommend."
      ]
   },
   {
      "id":57,
      "title":"Strangers When We Meet",
      "image_url":"http://dummyimage.com/157x100.png/ff4444/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.8,
      "release_date":2004,
      "review":[
         "A feel-good movie."
      ]
   },
   {
      "id":58,
      "title":"Machine Gun Kelly",
      "image_url":"http://dummyimage.com/142x100.png/ff4444/ffffff",
      "genre":"Action|Crime",
      "language":"tamil",
      "ratings":3.6,
      "release_date":0,
      "review":[
         "A few plot holes, but overall very entertaining."
      ]
   },
   {
      "id":59,
      "title":"Dracula's Daughter",
      "image_url":"http://dummyimage.com/129x100.png/cc0000/ffffff",
      "genre":"Drama|Horror",
      "language":"tamil",
      "ratings":3.1,
      "release_date":2012,
      "review":[
         "Great pacing and acting.",
         "Thoroughly enjoyable."
      ]
   },
   {
      "id":60,
      "title":"Sullivan's Travels",
      "image_url":"http://dummyimage.com/100x100.png/dddddd/000000",
      "genre":"Adventure|Comedy|Romance",
      "language":"tamil",
      "ratings":2.8,
      "release_date":2016,
      "review":[
         "Enjoyable and engaging throughout."
      ]
   },
   {
      "id":61,
      "title":"Beyond the Valley of the Dolls",
      "image_url":"http://dummyimage.com/203x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Horror",
      "language":"tamil",
      "ratings":4,
      "release_date":2011,
      "review":[
         "Fun and memorable movie.",
         "Had a great time watching."
      ]
   },
   {
      "id":62,
      "title":"We Are What We Are (Somos lo que hay)",
      "image_url":"http://dummyimage.com/249x100.png/5fa2dd/ffffff",
      "genre":"Drama|Horror",
      "language":"tamil",
      "ratings":4.6,
      "release_date":2013,
      "review":[
         "Solid entertainment with some heartfelt moments."
      ]
   },
   {
      "id":63,
      "title":"Grey Zone, The",
      "image_url":"http://dummyimage.com/211x100.png/ff4444/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.2,
      "release_date":2011,
      "review":[
         "A strong finish to a well-told story."
      ]
   },
   {
      "id":64,
      "title":"Civic Duty",
      "image_url":"http://dummyimage.com/163x100.png/ff4444/ffffff",
      "genre":"Drama|Thriller",
      "language":"tamil",
      "ratings":1.3,
      "release_date":2015,
      "review":[
         "Great atmosphere and direction."
      ]
   },
   {
      "id":65,
      "title":"Doug's 1st Movie",
      "image_url":"http://dummyimage.com/179x100.png/5fa2dd/ffffff",
      "genre":"Animation|Children",
      "language":"tamil",
      "ratings":3.9,
      "release_date":2009,
      "review":[
         "Highly enjoyable from start to finish."
      ]
   },
   {
      "id":66,
      "title":"Summer School",
      "image_url":"http://dummyimage.com/147x100.png/ff4444/ffffff",
      "genre":"Horror",
      "language":"tamil",
      "ratings":4.8,
      "release_date":2014,
      "review":[
         "Beautifully made.",
         "Stunning visuals."
      ]
   },
   {
      "id":67,
      "title":"Two-Lane Blacktop",
      "image_url":"http://dummyimage.com/201x100.png/dddddd/000000",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.1,
      "release_date":0,
      "review":[
         "A delightful experience.",
         "Would watch again."
      ]
   },
   {
      "id":68,
      "title":"Mickey's Once Upon a Christmas",
      "image_url":"http://dummyimage.com/144x100.png/ff4444/ffffff",
      "genre":"Animation|Comedy|Fantasy",
      "language":"tamil",
      "ratings":4.3,
      "release_date":2005,
      "review":[
         "Touching and well-acted."
      ]
   },
   {
      "id":69,
      "title":"Paper Man",
      "image_url":"http://dummyimage.com/115x100.png/dddddd/000000",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":3.6,
      "release_date":2011,
      "review":[
         "One of the best I've seen in a while."
      ]
   },
   {
      "id":70,
      "title":"Newsies",
      "image_url":"http://dummyimage.com/198x100.png/cc0000/ffffff",
      "genre":"Children|Musical",
      "language":"tamil",
      "ratings":2.1,
      "release_date":2020,
      "review":[
         "Amazing story with a strong message."
      ]
   },
   {
      "id":71,
      "title":"Now and Then",
      "image_url":"http://dummyimage.com/142x100.png/5fa2dd/ffffff",
      "genre":"Children|Drama",
      "language":"tamil",
      "ratings":2.4,
      "release_date":2010,
      "review":[
         "An unforgettable film.",
         "Outstanding performances."
      ]
   },
   {
      "id":72,
      "title":"After Earth",
      "image_url":"http://dummyimage.com/219x100.png/dddddd/000000",
      "genre":"Action|Adventure|Sci-Fi|IMAX",
      "language":"tamil",
      "ratings":3.1,
      "release_date":2019,
      "review":[
         "A must-watch!",
         "Breathtaking."
      ]
   },
   {
      "id":73,
      "title":"xXx: State of the Union",
      "image_url":"http://dummyimage.com/102x100.png/5fa2dd/ffffff",
      "genre":"Action|Crime|Thriller",
      "language":"tamil",
      "ratings":2.4,
      "release_date":2007,
      "review":[
         "Exceeded my expectations.",
         "Brilliant storytelling."
      ]
   },
   {
      "id":74,
      "title":"Double Whammy",
      "image_url":"http://dummyimage.com/200x100.png/dddddd/000000",
      "genre":"Action|Comedy|Drama",
      "language":"tamil",
      "ratings":4.9,
      "release_date":2012,
      "review":[
         "A masterpiece.",
         "Left me speechless."
      ]
   },
   {
      "id":75,
      "title":"Diary of the Dead",
      "image_url":"http://dummyimage.com/206x100.png/dddddd/000000",
      "genre":"Horror|Sci-Fi",
      "language":"tamil",
      "ratings":2.5,
      "release_date":2009,
      "review":[
         "One of the best movies of the decade."
      ]
   },
   {
      "id":76,
      "title":"Human Experience, The",
      "image_url":"http://dummyimage.com/233x100.png/ff4444/ffffff",
      "genre":"Documentary",
      "language":"tamil",
      "ratings":2.4,
      "release_date":2017,
      "review":[
         "Absolutely captivating."
      ]
   },
   {
      "id":77,
      "title":"Year of the Comet",
      "image_url":"http://dummyimage.com/247x100.png/ff4444/ffffff",
      "genre":"Action|Adventure|Comedy|Romance",
      "language":"tamil",
      "ratings":5,
      "release_date":2012,
      "review":[
         "An inspiring story.",
         "Heartwarming from start to finish."
      ]
   },
   {
      "id":78,
      "title":"End of Watch",
      "image_url":"http://dummyimage.com/189x100.png/5fa2dd/ffffff",
      "genre":"Crime|Drama|Thriller",
      "language":"tamil",
      "ratings":1.2,
      "release_date":2020,
      "review":[
         "A perfect blend of emotions.",
         "Highly recommended."
      ]
   },
   {
      "id":79,
      "title":"It Runs in the Family",
      "image_url":"http://dummyimage.com/108x100.png/cc0000/ffffff",
      "genre":"Comedy|Drama",
      "language":"tamil",
      "ratings":3.3,
      "release_date":2013,
      "review":[
         "An instant classic.",
         "I loved every minute."
      ]
   },
   {
      "id":80,
      "title":"The Tattooist",
      "image_url":"http://dummyimage.com/178x100.png/cc0000/ffffff",
      "genre":"Horror|Thriller",
      "language":"tamil",
      "ratings":2.8,
      "release_date":2014,
      "review":[
         "A phenomenal movie.",
         "Truly remarkable."
      ]
   },
   {
      "id":81,
      "title":"Osama",
      "image_url":"http://dummyimage.com/219x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":4.5,
      "release_date":2011,
      "review":[
         "Simply amazing.",
         "One of my favorites."
      ]
   },
   {
      "id":82,
      "title":"WarGames",
      "image_url":"http://dummyimage.com/102x100.png/5fa2dd/ffffff",
      "genre":"Drama|Sci-Fi|Thriller",
      "language":"tamil",
      "ratings":2.8,
      "release_date":2009,
      "review":[
         "An outstanding film."
      ]
   },
   {
      "id":83,
      "title":"Losing Isaiah",
      "image_url":"http://dummyimage.com/249x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":3.2,
      "release_date":2013,
      "review":[
         "Beautifully done.",
         "A powerful story."
      ]
   },
   {
      "id":84,
      "title":"Way of War, The",
      "image_url":"http://dummyimage.com/240x100.png/5fa2dd/ffffff",
      "genre":"Action|Thriller",
      "language":"tamil",
      "ratings":1.9,
      "release_date":2014,
      "review":[
         "Incredible performances.",
         "A true masterpiece."
      ]
   },
   {
      "id":85,
      "title":"Out 1: Spectre",
      "image_url":"http://dummyimage.com/230x100.png/5fa2dd/ffffff",
      "genre":"Comedy|Drama|Thriller",
      "language":"tamil",
      "ratings":1.7,
      "release_date":2015,
      "review":[
         "A cinematic gem.",
         "Unforgettable experience."
      ]
   },
   {
      "id":86,
      "title":"Gunfighter's Moon",
      "image_url":"http://dummyimage.com/181x100.png/dddddd/000000",
      "genre":"Romance|Western",
      "language":"tamil",
      "ratings":4.4,
      "release_date":2016,
      "review":[
         "I was moved to tears.",
         "A must-see for everyone."
      ]
   },
   {
      "id":87,
      "title":"Lion of the Desert",
      "image_url":"http://dummyimage.com/210x100.png/dddddd/000000",
      "genre":"War",
      "language":"tamil",
      "ratings":4.1,
      "release_date":2020,
      "review":[
         "Absolutely loved it!",
         "Will watch again and again."
      ]
   },
   {
      "id":88,
      "title":"In Country",
      "image_url":"http://dummyimage.com/202x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.3,
      "release_date":2015,
      "review":[
         "Top-notch storytelling.",
         "Brilliant execution."
      ]
   },
   {
      "id":89,
      "title":"Painted Veil, The",
      "image_url":"http://dummyimage.com/146x100.png/ff4444/ffffff",
      "genre":"Drama|Romance",
      "language":"tamil",
      "ratings":3.1,
      "release_date":2020,
      "review":[
         "One of the most impactful movies I've ever seen."
      ]
   },
   {
      "id":90,
      "title":"Daffy Duck's Quackbusters",
      "image_url":"http://dummyimage.com/149x100.png/ff4444/ffffff",
      "genre":"Animation|Children|Comedy|Horror",
      "language":"tamil",
      "ratings":1.1,
      "release_date":2010,
      "review":[
         "A breathtaking experience.",
         "Highly emotional and moving."
      ]
   },
   {
      "id":91,
      "title":"Lasa y Zabala",
      "image_url":"http://dummyimage.com/135x100.png/5fa2dd/ffffff",
      "genre":"(no genres listed)",
      "language":"tamil",
      "ratings":4,
      "release_date":2015,
      "review":[
         "Masterful direction.",
         "An extraordinary piece of cinema."
      ]
   },
   {
      "id":92,
      "title":"Wrath of God, The",
      "image_url":"http://dummyimage.com/205x100.png/5fa2dd/ffffff",
      "genre":"Western",
      "language":"tamil",
      "ratings":3.7,
      "release_date":2016,
      "review":[
         "The best movie I’ve ever watched."
      ]
   },
   {
      "id":93,
      "title":"Red Psalm (Még kér a nép)",
      "image_url":"http://dummyimage.com/191x100.png/5fa2dd/ffffff",
      "genre":"Drama|Musical|War",
      "language":"tamil",
      "ratings":1.8,
      "release_date":2018,
      "review":[
         "A brilliant piece of storytelling."
      ]
   },
   {
      "id":94,
      "title":"Past Midnight",
      "image_url":"http://dummyimage.com/177x100.png/dddddd/000000",
      "genre":"Horror|Thriller",
      "language":"tamil",
      "ratings":1.8,
      "release_date":2019,
      "review":[
         "Loved the cinematography!",
         "The characters were relatable.",
         "An emotional rollercoaster."
      ]
   },
   {
      "id":95,
      "title":"Rocky IV",
      "image_url":"http://dummyimage.com/190x100.png/5fa2dd/ffffff",
      "genre":"Action|Drama",
      "language":"tamil",
      "ratings":2.2,
      "release_date":2010,
      "review":[
         "A heartwarming tale with a fantastic message."
      ]
   },
   {
      "id":96,
      "title":"Home Sweet Home",
      "image_url":"http://dummyimage.com/184x100.png/ff4444/ffffff",
      "genre":"Comedy",
      "language":"tamil",
      "ratings":4.9,
      "release_date":2013,
      "review":[
         "Incredibly well acted!",
         "Such a unique perspective on the topic."
      ]
   },
   {
      "id":97,
      "title":"Dickson Greeting",
      "image_url":"http://dummyimage.com/158x100.png/ff4444/ffffff",
      "genre":"(no genres listed)",
      "language":"tamil",
      "ratings":3.4,
      "release_date":2015,
      "review":[
         "Absolutely stunning visuals.",
         "A captivating story that kept me on the edge of my seat."
      ]
   },
   {
      "id":98,
      "title":"Eclipse, The",
      "image_url":"http://dummyimage.com/100x100.png/5fa2dd/ffffff",
      "genre":"Drama|Horror|Thriller",
      "language":"tamil",
      "ratings":1.5,
      "release_date":2015,
      "review":[
         "A great film that everyone should see.",
         "Powerful performances.",
         "The music was perfect."
      ]
   },
   {
      "id":99,
      "title":"Story of Floating Weeds, A (Ukikusa monogatari)",
      "image_url":"http://dummyimage.com/241x100.png/cc0000/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":2.2,
      "release_date":2014,
      "review":[
         "A fun ride from start to finish.",
         "So entertaining!",
         "Made me laugh and cry."
      ]
   },
   {
      "id":100,
      "title":"Little Man Tate",
      "image_url":"http://dummyimage.com/211x100.png/5fa2dd/ffffff",
      "genre":"Drama",
      "language":"tamil",
      "ratings":1.6,
      "release_date":2011,
      "review":[
         "This movie blew me away!",
         "Exceptional storytelling.",
         "One of my all-time favorites.",
         "Will watch again!"
      ]
   }
]

movie.insert_many(movie_mock)