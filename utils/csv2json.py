#coding: utf8
import json, codecs

def SemicolonToJson(filename,fields):
    toReturn = []
    #with codecs.open(filename, 'r', encoding='utf-8', errors='replace') as f:
    with open(filename,'r') as f:
        for line in f:
            #values = map(lambda s: s.strip(), line.split(","))
            if '"' not in line:
                values = list(map(lambda s: s.strip(), line.split(",")))
                value = {}
                for attribute in fields:
                    index = fields.index(attribute)
                    value[attribute] = values[index]

                toReturn.append(value)

    return toReturn
