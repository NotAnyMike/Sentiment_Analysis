#coding: utf8
from pymongo import MongoClient
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from utils.csv2json import SemicolonToJson

stop = set(stopwords.words('spanish'))

##### Reading the file
entries = SemicolonToJson("docs/test/tuits.csv", ["date", "user", "full_name", "tweet", "id", "app", "followers", "follows", "retweets", "favorites", "verified", "user_since", "location", "bio", "profile_img", "maps", "depured"])
#entries =  SemicolonToJson("docs/test/smallcsv.csv",["number1","number2","number3","name"])

########## Old way
###### Tokenizing every tweet and removing the stop words
#for entry in entries:
    #entry['tokens'] = [i for i in entry['tweet'].lower().split() if i not in stop]
#
#print entry['tokens']

###### Stemming the tokens 
#stemmer = SnowballStemmer("spanish")
#entry['tokens'] = map(lambda token: stemmer.stem(token), entry['tokens'])
#########################
stemmer = SnowballStemmer("spanish")
for entry in entries:
    entry['tokens'] = [stemmer.stem(token) for token in entry['tweet'].lower().split() if token not in stop]

for entry in entries:
    print entry['tokens']

###### Connecting to the db
#client = MongoClient()
#db = client.test

#Saving the results in the db
#result = db.test.insert_one(entries[0])
#print result
