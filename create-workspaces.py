import json
import os
import time
def add_workspace(data,bundelId,Username,DirectoryId):
        data["Workspaces"].append({"DirectoryId" : DirectoryId,"UserName" : Username ,"BundleId" : bundelId,"WorkspaceProperties": {"RunningMode": "ALWAYS_ON"}})
print("Please Make sure that the ids.txt file is filled with updated Agent logins")
time.sleep(3)

#-------------------------- parametres ------------------------------------------------------------------

print("Please submit the bundle ID from the following list")
os.system("python3 bundle.py")
bundelId=input("bundleID: ")
print("Please submit the directory ID from the following list")
os.system("python3 directory.py")
DirectoryId=input("DirectoryId: ")
#---------------------------------------------------------------------------------------------------------


#-------------------------Make sure that the ids.txt file is filled with Agent logins---------------------
fichier= open("ids.txt","r")
ids=fichier.readlines()
list=[]
for id in ids:
        id=id[0:-1]
        if id !="":
                 list.append(id)
#------------------------------------How many pages have to be used --------------------------------------
n=len(list)
#print(n)
page=int(n/20)
if n%20 == 0:
        print("le nombre de  pages est: ",page)
else:
        page=page+1
        print("le nombre de  pages est: ",page)

#---------------------------Erease old pages--------------------------------------------------------------
os.system("rm -f page*")
#----------------------------Create the necessary pages --------------------------------------------------
for i in range (1,page +1):
        commande="touch page"+str(i)
        os.system(commande)

page_n=1
infra = {}
infra["Workspaces"]=[]
for i in range(1,n+1):
        Username=list[i-1]
        if i%20==0:
                add_workspace(infra,bundelId,Username,DirectoryId)
                file="page"+str(page_n)
                with open(file,'w') as outfile:
                        json.dump(infra, outfile)
                page_n=page_n+1
                infra = {}
                infra["Workspaces"]=[]
        elif i==n:
                add_workspace(infra,bundelId,Username,DirectoryId)
                file="page"+str(page_n)
                with open(file,'w') as outfile:
                        json.dump(infra, outfile)
        else:
                add_workspace(infra,bundelId,Username,DirectoryId)
#------------------------------ Prepare push file ---------------------------------------------------------
os.system("truncate -s0 push.bash")
for j in range(1,page+1):
        commande1 = "aws workspaces create-workspaces --cli-input-json file://page"+str(j)
        commande2 = "echo aws workspaces create-workspaces --cli-input-json file://page"+str(j)+" >> push.bash"
        print(commande1)
        os.system(commande2)
