#CloudIO
CloudIO is a Cloudstack Client written in Python

## Requirementes
Tested with Python 2.7.3

## Installation 
```sh
$ curl https://raw.githubusercontent.com/mms-gianni/CloudIO/master/bin/cloudiosays > /usr/local/bin/cloudiosays
$ chmod +x /usr/local/bin/cloudiosays
```
Yep ... thats it. 

On your first call you will be asked for your API RUL and credentials. 
I recommend to run following command first:
```sh  
$ /usr/local/bin/cloudiosays -c listprojects
```

## Usage 
### list projects
```sh  
$ /usr/local/bin/cloudiosays -c listprojects
```
### list diskofferings
```sh  
$ /usr/local/bin/cloudiosays -c listdiskofferings
```
### list Volumes
```sh  
$ /usr/local/bin/cloudiosays -c listvolumes
```
### list Isos
```sh  
$ /usr/local/bin/cloudiosays -c listisos -p [YOURPROJECT]
```
### list virtual machines
```sh  
$ /usr/local/bin/cloudiosays -c listprojects -p [YOURPROJECT]
```
### Stop virtual machine
```sh  
$ /usr/local/bin/cloudiosays -c listvms -p [YOURPROJECT] -v [VMNAME]
```
### Start virtual machine
```sh  
$ /usr/local/bin/cloudiosays -c start-vm -p [YOURPROJECT] -v [VMNAME]
```
### Create a new virtual machine
```sh  
$ /usr/local/bin/cloudiosays -c listprojects -p [YOURPROJECT] -v [VMNAME without the number] 
```
### Destroy a virtual machine
```sh  
$ /usr/local/bin/cloudiosays -c listprojects -p [YOURPROJECT] -v [VMNAME]
```

## TODO
 - hmmm 

## License
GNU GENERAL PUBLIC LICENSE V3
