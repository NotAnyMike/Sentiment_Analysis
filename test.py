from pymongo import MongoClient
from nltk.corpus import stopwords
from utils.csv2json import SemicolonToJson

stop = set(stopwords.words('spanish'))

#Reading the file
entries = SemicolonToJson("docs/test/tuits.csv", ["date", "user", "full_name", "tweet", "id", "app", "followers", "follows", "retweets", "favorites", "verified", "user_since", "location", "bio", "profile_img", "maps"])
#entries =  SemicolonToJson("docs/test/smallcsv.csv",["number1","number2","number3","name"])

#Tokenizing every tweet
for entry in entries:
    entry['tokens'] = [i for i in entry['tweet'].lower().split() if i not in stop]

#Connecting to the db
client = MongoClient()
db = client.test

#Saving the results in the db
result = db.test.insert_one(entries[0])
print result
