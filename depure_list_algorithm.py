#encoding: utf8
from utils.csv2json import SemicolonToJson
import csv
import re

#asking fo the name of the file
file_location = input("write the location of the csv file: ")
if file_location == "0":
    file_location = "docs/test/tuits.csv"

#load the csv file
entries = SemicolonToJson(file_location, ["date", "user", "full_name", "tweet", "id", "app", "followers", "follows", "retweets", "favorites", "verified", "user_since", "location", "bio", "profile_img", "maps"])

#change depure the tweets
for entry in entries:
    entry["depured"] = re.sub(r'(https)(([^(\"|,)|\s|$])*)(?=(?:\"|\,|\s|$))', '', entry["tweet"].lower())

#save the value
f = csv.writer(open(file_location.replace(".csv", "") + "_depured.csv", "w", encoding='utf-8-sig'), dialect='excel')

# Write CSV Header, If you dont need that, remove this line
f.writerow(["date", "user", "full_name", "tweet", "id", "app", "followers", "follows", "retweets", "favorites", "verified", "user_since", "location", "bio", "profile_img", "maps", "depured"])

for x in entries:
    f.writerow([x["date"], x["user"], x["full_name"], x["tweet"], x["id"], x["app"], x["followers"], x["follows"], x["retweets"], x["favorites"], x["verified"], x["user_since"], x["location"], x["bio"], x["profile_img"], x["maps"], x["depured"]])
