# Sentiment Analysis Project

Here will be located the respository for the Sentiment Analysis project for the CL UTL.

# Data preprocessing

1. Upload data from google spreadshit to mongodb (it can be improved recoleting the data directly into the db)
2. General cleaning
2. Tokenize the sentence
3. Remove stop words
5. Steamming

## General information

This project will use MongoDB as a database, in order to run it run `mongod --dbpath docs/db`

## Useful commands

* Don't forget to do `source sa/bin/activate` and `pip freeze > requirements.txt`
* I recommend to have the MongoDB installed not only through pip, but also through the binary or brew
* In order to use `networkx` it is necesary to have installed `GDAL` if it rises an error taying to install it use a speacial version for instance `pip install GDAL==1.10.0` (I think this one is for another project lol)
