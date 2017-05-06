import csv, json

def Csv_to_json(filename, fields):
    csvfile = open(filename, 'r')
    reader = csv.DictReader( csvfile, fields) 
    out = json.dumps([row for row in reader])
