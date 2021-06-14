import json
import os

def bundl_name(bdl_id):
    with open('bundle.txt') as json_file:
         data = json.load(json_file)
         for p in data['Bundles']:
             if p['BundleId'] == bdl_id:
                return p['Name']

def dir_code(dir_id):
        with open('directory.txt') as json_file:
                data = json.load(json_file)
                for p in data['Directories']:
                        if p['DirectoryId']== dir_id:
                                return p["RegistrationCode"]

def get_dir_alias(dir_id):
    with open('directory.txt') as json_file:
        data = json.load(json_file)
        for p in data['DirectoryDescriptions']:
            if p['DirectoryId']==dir_id:
               return p['Alias']
