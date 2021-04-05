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

docker_con()
