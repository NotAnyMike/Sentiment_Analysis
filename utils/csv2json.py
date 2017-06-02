#coding: utf8
import json, codecs, re

def SemicolonToJson(filename,fields):
    toReturn = []
    #with codecs.open(filename, 'r', encoding='utf-8', errors='replace') as f:
    with open(filename,'r') as f:
        #for line in f:
        file_string = f.read()
        lines = re.split("\n(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)",file_string)
        
        for line in lines:
            line = line.replace("\s","")
            if line:
                #values = map(lambda s: s.strip(), line.split(","))
                values = list(map(lambda s: s, re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)",line)))
                value = {}
                for attribute in fields:
                    try:
                        index = fields.index(attribute)
                        value[attribute] = values[index]
                    except:
                        print(line)
                        raise

                toReturn.append(value)

    return toReturn
