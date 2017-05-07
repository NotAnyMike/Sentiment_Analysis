from pymongo import MongoClient
from utils.csv2json import SemicolonToJson

entries = SemicolonToJson("docs/test/tuits.csv", ["date", "user", "full_name", "tweet", "id", "app", "followers", "follows", "retweets", "favorites", "verified", "user_since", "location", "bio", "profile_img", "maps"])
#entries =  SemicolonToJson("docs/test/smallcsv.csv",["number1","number2","number3","name"])

client = MongoClient()
db = client.test

result = db.test.insert_one(entries[0])
print result
