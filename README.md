#CloudIO
CloudIO is a Cloudstack Client written in Python

## Requirementes
Tested with Python 2.7.3
OS: Mac, Linux
Cloudstack 4.4 

## Installation 
```sh
$ python setup.py install
```
Yep ... thats it. 

On your first call you will be asked for your API URL and credentials. 
```sh  
$ /usr/local/bin/cloudiosays
```
The credentials are stored here : /usr/local/share/cloudio/ 
To reentter them just remove the config.pickle 

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
 - Progress bar

## License
GNU GENERAL PUBLIC LICENSE V3
