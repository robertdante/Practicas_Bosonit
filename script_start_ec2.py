import boto3
import sys
import time


ec2 = boto3.client('ec2')

action = sys.argv[1] 
instances = [sys.argv[2]] if len(sys.argv) > 2 else '.'

def main():
    if action == "stop":
        stopInstance()
    elif action == "start":
        startInstance()
    elif action == "list":
        listInstances()
    else:
        print("Choose start + instanceId, stop + instanceId or list")
        
        
def startInstance():
    ec2.start_instances(InstanceIds=instances)
    print("============================")
    print('Try to start Ec2 instance...')
    print("============================")
    time.sleep(30)
    
def stopInstance():
    ec2.stop_instances(InstanceIds=instances)
    print("===========================")
    print('Try to stop Ec2 instance...')
    print("===========================")
    time.sleep(30)
    
def listInstances():
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])
            print(instance["Tags"])
            print(instance["Placement"])
            print(instance["State"])
            print("====================")
       
    
if __name__ == '__main__':
    main() 
