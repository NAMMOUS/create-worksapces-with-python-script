from function import *
import json
import os
command=os.system("aws workspaces describe-workspaces > inventaire.txt")
command=os.system("aws workspaces describe-workspace-directories  > directory.txt")
with open('inventaire.txt') as json_file:
        data = json.load(json_file)
        for p in data['Workspaces']:
                id = p['UserName']
                if id in open('ids.txt').read():
                        #print(p['WorkspaceId'], p['DirectoryId'],p['UserName'],p['IpAddress'],p['State'],p['BundleId'], p['SubnetId'], p['ComputerName'])
                        #print(p['WorkspaceId'], p['DirectoryId'],p['UserName'],p['BundleId'], p['State'])
                        #print(p['UserName'],p['IpAddress'],p['ComputerName'],dir_code(p['DirectoryId']))
                        print(p['UserName'],"  \t",p['IpAddress'],"  \t",p['ComputerName']," \t",dir_code(p['DirectoryId'])," \t")
                        #print(p['ComputerName'],end =",")

