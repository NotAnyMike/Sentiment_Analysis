from utils.csv2json import SemicolonToJson

print SemicolonToJson("docs/test/tuits.csv", ["date", "user", "full_name", "tweet", "id", "app", "followers", "follows", "retweets", "favorites", "verified", "user_since", "location", "bio", "profile_img", "maps"])
#print SemicolonToJson("smallcsv.csv",["number1","number2","number3","name"])
