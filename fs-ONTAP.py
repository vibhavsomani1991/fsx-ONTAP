import boto3
from pprint import pprint
import pandas as pd

# Describe FSx
def describe_FSx():
    session = boto3.session.Session(profile_name ='default',region_name ="eu-east-1")
    client = boto3.client('fsx')
    for allfsx in client.describe_file_systems()['FileSystems']:
        try:
            # pprint(allfsx)
            allfsxid = []
            fstype  = []
            fslifecycle = []
            fsownerid = []
            fsstorage = []
            fsconfig = []
            df = pd.DataFrame()
            allfsxid = allfsx['FileSystemId']
            # print(allfsxid)
            fstype = allfsx['FileSystemType']
            # pprint(fstype)
            fslifecycle = allfsx['Lifecycle']
            # pprint(fslifecycle)
            fsownerid = allfsx['OwnerId']
            # pprint(fsownerid)
            fsstorage = allfsx['StorageCapacity']
            # pprint(fsstorage)
            fsconfig = allfsx['OntapConfiguration']
            # pprint(fsconfig)
            deploymentType = fsconfig['DeploymentType']
            # pprint(deploymentType)
            tags = allfsx['Tags']
            for tag in tags:
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    # pprint(name)
                    # pprint(tag)
            dict = {'fsxid' : [allfsxid] , 'fsxtype' : [fstype] , 'fsxlifecycle' : [fslifecycle] , 'fsxownerid' : [fsownerid] , 'fsxstorage' : [fsstorage] , 'fsdtype' : [deploymentType]}
            df = pd.DataFrame(dict)
            df.to_csv('fsx_test.csv' , index = False)
        
        except Exception as e:
            print(e)
                
# Describe SVM
def describe_SVM():
    session = boto3.session.Session(profile_name ='default',region_name ="eu-east-1")
    client = boto3.client('fsx')
    for allsvm in client.describe_storage_virtual_machines()['StorageVirtualMachines']:
        try:
            #  pprint(allsvm)
            filesystemid = allsvm['FileSystemId']
            # pprint(filesystemid)
            svmname = allsvm['Name']
            # pprint(svmname)
            svmid = allsvm['StorageVirtualMachineId']
            # pprint('svmid')
            dict = {'fsxid' : [filesystemid] , 'svmnme' : [svmname] , 'svmid' : [svmid]}
            df = pd.DataFrame(dict)
            df.to_csv('fsx_svm.csv' , index = False)
        except Exception as e:
            print(e)

# Describe Volume
def describe_volume():
    session = boto3.session.Session(profile_name ='default',region_name ="eu-east-1")
    client = boto3.client('fsx')
    for allvolume in client.describe_volumes()['Volumes']:
        try:
            # pprint(allvolume)
            filesysid = allvolume['FileSystemId']
            # pprint(filesysid)
            volumename = allvolume['Name']
            # pprint(volumename)
            volumeconfig = allvolume['OntapConfiguration']
            securitystyle = volumeconfig['SecurityStyle']
            # pprint(securitystyle)
            size = volumeconfig['SizeInMegabytes']
            # pprint(size)
            svmid = volumeconfig['StorageVirtualMachineId']
            # pprint(svmid)
            volumetype = volumeconfig['StorageVirtualMachineRoot']
            # print(volumetype)
            volumeid = allvolume['VolumeId']
            # pprint(volumeid)
            voltype = allvolume['VolumeType']
            # pprint(voltype)
            dict = {'fsid' : [filesysid] , 'volname' : [volumename] , 'volconfig' : [size] , 'svmid' : [svmid] , 'volumetype' : [volumetype] , 'volid' : [volumeid] , 'voltype' : [voltype]}
            df = pd.DataFrame(dict)
            df.to_csv('fsx_vol.csv' , index = False)
            
        except Exception as e:
            print(e)

# Delete Volume
# def delete_volume():
#     session = boto3.session.Session(profile_name ='default',region_name ="eu-east-1")
#     client = boto3.client('fsx')

# def delete_fsx():
    


describe_FSx()  
describe_SVM()
describe_volume()
# delete_volume()
