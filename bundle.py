import json
import os
command=os.system("aws workspaces describe-workspace-bundles > bundle.txt")
print("---------------------------")
with open('bundle.txt') as json_file:
        data = json.load(json_file)
        for p in data['Bundles']:
                print(p['BundleId'], p['Name'])
print("---------------------------")
