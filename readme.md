# Sentiment Analysis Project

Here will be located the respository for the Sentiment Analysis project for the CL UTL.

# Data preprocessing

1. Upload data from google spreadsheet to mongodb (it can be improved recoleting the data directly into the db)
2. General cleaning
3. Remover repetitions
2. Tokenize the sentence
3. Remove stop words
5. Steamming

* In mac there is a bug, when downloading the csv file from google spreadsheet the encoding will have some problems with special characters and given that we working in spanish it a serious problem, to solve it save the downloaded file with numbers (at least in mac) and make the endode `ult-8`.
* Considere change words as __xq__ to __porque__
* the general algorithm could be improved by taking into account the emojis

## In order to run this section do
1. change to the directory
2. `source sa/bin/activate` in order to start the virtual environment
3. `python test.py`

# General information

This project will use MongoDB as a database, in order to run it run `mongod --dbpath docs/db`

## Useful commands

* Don't forget to do `source sa/bin/activate` and `pip freeze > requirements.txt`
* I recommend to have the MongoDB installed not only through pip, but also through the binary or brew
* In order to use `networkx` it is necesary to have installed `GDAL` if it rises an error taying to install it use a speacial version for instance `pip install GDAL==1.10.0` (I think this one is for another project lol)
