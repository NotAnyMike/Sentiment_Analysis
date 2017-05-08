#!/usr/bin/python
# -*- coding: latin-1 -*-
from nltk.corpus import stopwords
stop = set(stopwords.words('spanish'))
t = "Vencer la corrupción menos estarás la dictadura dé peñalosa que usted apoya y proteje con su silencio".decode('utf8')
tokens = ([i for i in t.lower().split() if i not in stop])
print tokens
for x in tokens:
    print x.encode('utf8')
