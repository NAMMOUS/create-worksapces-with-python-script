import json
import os
from function import bundl_name
from function import dir_code
command=os.system("aws workspaces describe-workspaces > inventaire.txt")
command=os.system("aws workspaces describe-workspace-directories  > directory.txt")
command=os.system("aws workspaces describe-workspace-bundles > bundle.txt")
with open('inventaire.txt') as json_file:
        data = json.load(json_file)
        for p in data['Workspaces']:
            print(p['UserName'],"  \t",p['IpAddress'],"  \t",p['ComputerName']," \t",dir_code(p['DirectoryId'])," \t",bundl_name(p['BundleId']),"\t", p['State'])
                
