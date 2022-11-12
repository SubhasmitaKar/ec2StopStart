import json
import boto3
import sys

ec2 = boto3.resource('ec2', region_name='us-east-1')

def stop_running_instances(ec2):
    filters = [{'Name': 'instance-state-name', 'Values': ['running']}, {'Name':'tag:Role','Values':['Jenkins']}]
    allinstances = ec2.instances.all()
    filteredinstances = ec2.instances.filter(Filters=filters)
    instancesId = []
    filteredId = []
    for k in filteredinstances:
        filteredId.append(k.id)
    for i in allinstances:
        idAll=i.id
        if (idAll not in filteredId):
            instancesId.append(idAll)
    for instance in instancesId:
        ec2.Instance(instance).stop()
   
def start_running_instances(ec2):
    filters = [{'Name': 'instance-state-name', 'Values': ['stopped']}, {'Name':'tag:Role','Values':['Jenkins']}]
    allinstances = ec2.instances.all()
    filteredinstances = ec2.instances.filter(Filters=filters)
    instancesId = []
    filteredId = []
    for k in filteredinstances:
        filteredId.append(k.id)
    for i in allinstances:
        idAll=i.id
        if (idAll not in filteredId):
            instancesId.append(idAll)
    for instance in instancesId:
        ec2.Instance(instance).start()
   
action = sys.argv[1]
if (action=="start"):
    start_running_instances(ec2)
    print('Sucessfully started the instances')
elif (action=="stop"):
    stop_running_instances(ec2)
    print('Sucessfully stopped the instances')
