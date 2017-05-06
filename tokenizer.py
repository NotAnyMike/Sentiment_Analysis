from nltk.corpus import stopwords
stop = set(stopwords.words('spanish'))
t = "Vencer la corrupcion menos la dictadura de penalosa que usted apoya y proteje con su silencio"
print [i for i in t.lower().split() if i not in stop]
