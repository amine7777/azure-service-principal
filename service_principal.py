
import os
import subprocess

import re
from subprocess import check_output
azure_info=""
subscription_id=""
tenant_id=""
secret=""
azure_info2=""
client_id=""
#this script works only with one subscription id / you can inspire yourself and make it for many :)
#with love amine7777


#entering name and role
name= raw_input("name:")
role=raw_input("role:")


#login to azure and recover the info
output = check_output(["az", "login"])

azure_info=output


#find the subscription id and tenant id in the output
subscription_id = re.findall(r'id.*', azure_info)


#converting the lists to string
subscription_id= "".join(subscription_id)


#cleaning the id
subscription_id= subscription_id.replace('"' , "")
subscription_id= subscription_id.replace("," , "")
subscription_id= subscription_id.replace("id: " ,"")




check_output(["az", "account", "set","-s",subscription_id])
#creating the service account with the variables
#if the variables are empty you will get an error


#create a service account with name and role
out=check_output(["az","ad","sp","create-for-rbac","--name",name,"--role",role])
azure_info2=out


tenant_id = re.findall(r'tenant.*', azure_info2)
client_id = re.findall(r'appId.*', azure_info2)
secret= re.findall(r'password.*', azure_info2)

#change to string
tenant_id= "".join(tenant_id)
client_id= "".join(client_id)
secret= "".join(secret)
#clear the string
tenant_id= tenant_id.replace('"' , "")
tenant_id= tenant_id.replace("," , "")
tenant_id= tenant_id.replace("tenant: " , "")

client_id= client_id.replace('"' , "")
client_id= client_id.replace("," , "")
client_id= client_id.replace("appId: " , "")

secret= secret.replace('"' , "")
secret= secret.replace("," , "")
secret= secret.replace("password: " , "")

print("subscription_id:"+subscription_id )
print("tenant:"+tenant_id)
print("client_id:"+client_id)
print("secret:"+secret)
