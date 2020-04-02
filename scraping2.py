import csv
import json

with open('output.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    goodnames = []
    for row in reader:
        name = row[0]
        if name.count(' ')>0:
            if name.islower()!=1:
                if name.replace(' ','a').isalpha():
                    goodnames.append(name)
                
            else:
                print(name)
        else :
            print(name)
        
f = open ('students.json', "r") 

data = json.loads(f.read()) 

print("\n\n\n")

for entry in data:
    #print(entry['a'])
    name = entry['n']
    if name in goodnames:
        print (name)
        print (entry['r'])
        print (entry['p'])
        with open('output.csv', newline='') as myFile:
            reader = csv.reader(myFile)
            for row in reader:
                if(name==row[0]):
                    print (row[1])
                    print(row[2])
                    print("\n\n")

