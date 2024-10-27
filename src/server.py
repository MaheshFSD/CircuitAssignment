
# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://mahagn118:GrZjP7Y71yHjXtHx@moviecluster.sdfmk.mongodb.net/moviedb?retryWrites=true&w=majority&appName=moviecluster"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)




# from pymongo import pymongo
# from pymongo import MongoClient
# import collectioncluster = MongoClient('mongodb+srv://admin:admin123@cluster0.fbsul.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# db = cluster["sldb"]
# collection = db["employee"]
# post = {"name": "amar", "email": "amar@mail.com"}
# collection.insert_one(post)