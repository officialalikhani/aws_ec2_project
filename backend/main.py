from aws_class import aws_class
from psycopg2 import FastAPI
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
import time
import threading
from datetime import date

app = FastAPI()

security = HTTPBasic()
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "P@ssw0rd123")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/deploy_droplets")
async def read_item(user: str, size: str, username: str = Depends(get_current_username)):
    obj = aws_class()
    size_dic= {
        '1*1':'t2.micro',
        '1*2':'t2.small',
        '2*4':'t2.medium',
        '2*8':'t2.large',
        '4*16':'t2.xlarge',
    }
    region_dic = {
        'US-Virginia':'us-east-1',
        'US-Ohio':'us-east-2',
        'US-California':'us-west-1',
        'US-Oregon':'us-west-2',
        'Africa':'af-south-1',
        'Hong Kong':'ap-east-1',
        'Seoul':'ap-northeast-2',
        'Tokyo':'ap-northeast-1',
        'Canada':'ca-central-1',
        'Frankfurt':'eu-central-1',
        'Ireland':'eu-west-1',
        'London':'eu-west-2',
        'Milan':'eu-south-1',
        'Paris':'eu-west-3',
        'Stockholm':'eu-north-1',
        'Bahrain':'me-south-1',
        'São Paulo':'sa-east-1',
    }
    images_dic = {
        'RHel8':'ami-0b0af3577fe5e3532',
        'Suse':'ami-08f182b25f271ef79',
        'ubuntu20':'ami-04505e74c0741db8d',
        'ubuntu18':'ami-0e472ba40eb589f49',
        'winodwsserver2019':'ami-08ed5c5dd62794ec0',
        'windowsserver2022':'ami-03fe02556b17692cb',
        'debian10':'ami-07d02ee1eeb0c996c',
        'centos7':'ami-006219aba10688d0b',
    }
    _size_ = size_dic.get(size)
    _region_ = 'us-east-1'
    _images_ = 'ami-006219aba10688d0b'
    a = obj.create_instance(_region_,_images_,_size_)   
    time.sleep(5)
    ip=obj.get_public_ip(a)
    today = date.today()
    obj.insert(a, ip, user, size, _region_, today)
    js= {
        'ip':ip,
        'id':a,
    }
    return js    

@app.get("/Project exist")
async def read_item(user: str,username: str = Depends(get_current_username)):
    obj = aws_class()
    a = obj.select(user)
    return a

@app.get("/terminate")
async def read_item(id_vm: str,username: str = Depends(get_current_username)):
    obj = aws_class()
    a = obj.terminate_instance(id_vm)
    return a
