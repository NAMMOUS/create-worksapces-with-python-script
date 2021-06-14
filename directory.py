import json
import os
command=os.system("aws ds describe-directories > directory.txt")
print("---------------------------")
with open('directory.txt') as json_file:
        data = json.load(json_file)
        for p in data['DirectoryDescriptions']:
                print(p['DirectoryId'], " ",p['Alias'])

print("---------------------------")
