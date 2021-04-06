#!/usr/bin/env python3

'''
Task 9*
For this task you need to have docker daemon installed and running.  The task is to create a python script, that has following functions:  
1. connects to docker API and print a warning message if there are dead or stopped containers with their ID and name. 
2. containers list, similar to docker ps -a  
3. image list, similar to docker image ls 
4. container information, like docker inspect 
 
Connection function must accept connection string for example 'http://192.168.56.101:2376' and connect to it or use string from environment
if no connection string is given.    
In order to connect to docker, you can use either Unix socket or reconfigure daemon to use a network socket 
(https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option)
'''
import sys
from pprint import pprint
import docker
import requests
import socket
import pprint

from urllib3.connection import HTTPConnection
from urllib3.connectionpool import HTTPConnectionPool
from requests.adapters import HTTPAdapter

import datetime
MY_UTC_EPOCH_START = 1262304000  # 00:00:00 01.01.2010 UTC

def my_utcfromtimestamp(ts):
    return datetime.datetime.utcfromtimestamp(ts + MY_UTC_EPOCH_START)
    
#для использования unix-socket
class DockerConnection(HTTPConnection):
    def __init__(self):
        super().__init__("localhost")

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect("/var/run/docker.sock")


class DockerConnectionPool(HTTPConnectionPool):
    def __init__(self):
        super().__init__("localhost")

    def _new_conn(self):
        return DockerConnection()


class DockerAdapter(HTTPAdapter):
    def get_connection(self, url, proxies=None):
        return DockerConnectionPool()





def docker_con():
    try:
        url=sys.argv[1]
    except IndexError:
        url='unix://var/run/docker.sock'
        print("Connection string wasn't given as an argument to the script {0}. {1} will be used."  .format(sys.argv[0], url))
    
    #client = docker.from_env()
    client_api = docker.APIClient(base_url=url)
    client = docker.DockerClient(base_url=url)
    
    input("Press ENTER to continue.")
    
    
    #1.print a warning message if there are dead or stopped containers with their ID and name.
    print("Task #1") 
    for container in client.containers.list(all=True):
        if container.status in ['dead', 'stopped', 'exited', 'paused', 'created' ]:
            print('Warning! name={0}  :  id={1}  :  status={2}'.format(container.name,container.id,container.status))
    
    
    input("Press ENTER to continue.")
    
    #2. containers list, similar to docker ps -a
    print("Task #2")
    print(client.containers.list(all=True))
    
    
    input("Press ENTER to continue.")
    
    #3. image list, similar to docker image ls 
    print("Task #3")
    print(client.images.list())
    
    input("Press ENTER to continue.")
    
    
    #4. container information, like docker inspect 
    for container in client.containers.list(all=True):
        print('\n\n\nInsperct of {}.\n\n\n'.format(container.name))
        pprint(client_api.inspect_container(container.id))
        input("Press ENTER to continue.")
    
    client.close()
    client_api.close()

def docker_req():
    #curl --unix-socket /var/run/docker.sock http://localhost/v1.41/containers/json?all=1
    try:
        url=sys.argv[1]
    except IndexError:
        url='http://localhost/'
        print("Connection string wasn't given as an argument to the script {0}. {1} will be used."  .format(sys.argv[0], url))
    
    session = requests.Session()
    session.mount(f"{url}", DockerAdapter())
    response = session.get(f"{url}/v1.41/containers/json?all=1")
    
    
    json_response = response.json()
    
    #1.print a warning message if there are dead or stopped containers with their ID and name.
    print("Task #1") 
    for container in json_response:
        if container["Status"].lower() in ['dead', 'stopped', 'exited', 'paused', 'created' ]:
            print('Warning! name={0}  :  id={1}  :  status={2}'.format(container["Names"][0],container["Id"][0:12],container["Status"]))
    
    input("Press ENTER to continue.")
    
    #2. containers list, similar to docker ps -a
    print("Task #2")
    
    CONTAINER_ID='CONTAINER_ID'
    IMAGE='IMAGE'
    COMMAND='COMMAND'
    CREATED='CREATED'
    STATUS='STATUS'
    PORTS='PORTS'
    NAMES='NAMES'
    print(f'{CONTAINER_ID:<20} {IMAGE:<25} {COMMAND:<18} {CREATED:<20} {STATUS:<15} {PORTS:<50} {NAMES:<20}')
    for con in json_response:
        try:
            pp=con["Ports"].pop(0)
        except IndexError:
            p_ports=''
        except KeyError:
            p_ports=''
        else:
            p_ports=f'{pp["PrivatePort"]}/{pp["Type"]}'
            for p in con["Ports"]:
                p_ports+=','
                try:
                    p_ports+=f'{p["IP"]}:{p["PublicPort"]}->{p["PrivatePort"]}:{p["Type"]}'
                except KeyError:
                    p_ports+=''
        con_created=datetime.datetime.fromtimestamp(int(con["Created"])).strftime('%Y-%m-%d %H:%M:%S')
        print(f'{con["Id"][0:12]:<20} {con["Image"]:<25} {con["Command"]:<18} {con_created:<20} {con["Status"]:<15} {p_ports:<50} {con["Names"][0]:<20}')
    
    input("Press ENTER to continue.")
    
    #3. image list, similar to docker image ls 
    print("Task #3")
    response_images = session.get(f"{url}/v1.41/images/json")
    json_response_images = response_images.json()
    for img in json_response_images:
        pprint.pprint(json_response_images)
        
    
    
    input("Press ENTER to continue.")    
    
    #4. container information, like docker inspect
    
    pprint.pprint(response.json())





#docker_con()
docker_req()





