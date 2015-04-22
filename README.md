#CloudIO
CloudIO is a Cloudstack Client written in Python

## Requierments
Tested with Python 2.7.3
OS: Mac, Linux
Cloudstack 4.4 

## Installation (site-wide)
```sh
$ sudo apt-get install python-setuptools
$ python setup.py install
```

## Installation (using virtualenv)
```sh
$ sudo apt-get install python-setuptools
$ sudo easy_install pip virtualenv
$ virtualenv local
$ source local/bin/activate
$ python setup.py install
```
Yep ... thats it. 

## Initial configuration
On your first call you will be asked for your API URL and credentials. 
```sh
$ export CLOUDIO_HOME=/usr/local/share/cloudio
$ cloudiosays
```
The credentials are stored here : /usr/local/share/cloudio/ 
To reenter them just remove the config.pickle 

## Usage 
### list projects
```sh  
$ cloudiosays -c listprojects
```
### list diskofferings
```sh  
$ cloudiosays -c listdiskofferings
```
### list Volumes
```sh  
$ cloudiosays -c listvolumes
```
### list Isos
```sh  
$ cloudiosays -c listisos -p [YOURPROJECT]
```
### list virtual machines
```sh  
$ cloudiosays -c listprojects -p [YOURPROJECT]
```
### Stop virtual machine
```sh  
$ cloudiosays -c stopvm -p [YOURPROJECT] -v [VMNAME]
```
### Start virtual machine
```sh  
$ cloudiosays -c startvm -p [YOURPROJECT] -v [VMNAME]
```
### Create a new virtual machine
```sh  
$ cloudiosays -c creatvm -p [YOURPROJECT] -v [VMNAME without the number] 
```
### Destroy a virtual machine
```sh  
$ cloudiosays -c destroyvm -p [YOURPROJECT] -v [VMNAME]
```

## TODO
 - Progress bar

## License
GNU GENERAL PUBLIC LICENSE V3
