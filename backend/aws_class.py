import boto3
import os
import psycopg2

class aws_class:
    def __init__(self):
        pass 
    
    def create_key_pair(self):
        ec2_client = boto3.client("ec2", region_name="us-east-1")
        key_pair = ec2_client.create_key_pair(KeyName="ec2-key-pair")
        private_key = key_pair["KeyMaterial"]
        with os.fdopen(os.open("/tmp/aws_ec2_key.pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
            handle.write(private_key)

    def create_instance(self,region,image,size):
        ec2 = boto3.resource('ec2', region_name=region)
        instances = ec2.create_instances(
            ImageId=image,
            MinCount=1,
            MaxCount=1,
            InstanceType=size,
            KeyName='pub6'
        )
        id = instances[0]._id
        return id

    def start_instance(self,instance_id):
        ec2_client = boto3.client("ec2", region_name="us-east-1")
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(response)
    
    def stop_instance(self,instance_id):
        ec2_client = boto3.client("ec2", region_name="us-east-1")
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(response)

    def terminate_instance(self,instance_id):
        ec2_client = boto3.client("ec2", region_name="us-east-1")
        response = ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(response)

    def get_public_ip(self,instance_id):
        ec2_client = boto3.client("ec2",region_name="us-east-1")
        reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")
        for reservation in reservations:
            for instance in reservation['Instances']:
                a = (instance.get("PublicDnsName"))
        return a

    def list_instance(self):
        AWS_REGION = "us-east-1"
        EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
        instances = EC2_RESOURCE.instances.all()
        for instance in instances:
            print(f'EC2 instance {instance.id}" information:')
            print(f'Instance state: {instance.state["Name"]}')
            print(f'Instance AMI: {instance.image.id}')
            print(f'Instance platform: {instance.platform}')
            print(f'Instance type: "{instance.instance_type}')
            print(f'Piblic IPv4 address: {instance.public_ip_address}')
            print('-'*60)


    def insert(self, id_vm, ip_address, username, size, location, date):
        conn = psycopg2.connect(
            user='postgres',
            password='P@ssw0rd',
            host='127.0.0.1',
            port='5432',
            database='postgres',
            # sslmode = 'require',
        )
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO public.aws(
	  id_vm, ip_address, username, size_, location_, date)
	VALUES ('{id_vm}','{ip_address}','{username}', '{size}', '{location}', '{date}');""")
        conn.commit()
        cur.close()
        conn.close()

    def select(self,username):
        conn = psycopg2.connect(
            user='postgres',
            password='P@ssw0rd',
            host='127.0.0.1',
            port='5432',
            database='postgres',
            # sslmode = 'require',
        )
        cur = conn.cursor()
        cur.execute(f"""SELECT  id_vm ,ip_address, username, size_, location_, date
            FROM public.aws WHERE username = '{username}' ;""")
        for record in cur:
              print(record)
        cur.close()
        conn.close()
        return record
        
