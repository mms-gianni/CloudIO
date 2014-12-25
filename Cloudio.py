from Client import CloudStackClient

import sys, getopt, re, os, pickle
class Cloudio(CloudStackClient):

  colors = {
    'Running':    '\033[m\033[0;32m', 
    'Stopped':    '\033[m\033[0;31m', 
    'Stopping':   '\033[m\033[0;33m', 
    'Expunging':  '\033[m\033[0;36m', 
    'Starting':   '\033[m\033[0;34m',
    'Destroyed':  '\033[m\033[0;35m',
    'Error':      '\033[m\033[0;35m',
    'Title':      '\033[m\033[1;30m\033[38;5;255m',
    'Question':   '\033[m\033[1;30m\033[38;5;226m',
    'Reset':      '\033[0m',
  }

  project_arr = {}

  projectid = ""

  def __init__(self):
  
    config_arr = {}
    path = '/usr/local/share/cloudio'
    if os.path.isfile(path+'/config.pickle'):
       config_arr = pickle.load(open(path+'/config.pickle', 'rb'))
    else:
       if not os.path.exists(path):
          os.makedirs(path)
       q = self.colors['Question']+"Api URL : "+self.colors['Reset']
       config_arr['apiUrl'] = raw_input(q)

       q = self.colors['Question']+"Api Key : "+self.colors['Reset']
       config_arr['apiKey'] = raw_input(q)

       q = self.colors['Question']+"Secret Key : "+self.colors['Reset']
       config_arr['secretKey'] = raw_input(q)
       pickle.dump(config_arr, open(path+'/config.pickle', 'wb'))


    self.apiKey     = config_arr['apiKey']
    self.secretKey  = config_arr['secretKey']
    self.auth       = True
    self.url        = config_arr['apiUrl']


    if os.path.isfile(path+'/project.pickle'):
      self.project_arr = pickle.load(open(path+'/project.pickle', 'rb'))
    else:
      res = client.listProjects()
      for item in res['listprojectsresponse']['project']:
        self.project_arr[item['name']] = item['id'] 

      pickle.dump(self.project_arr, open(path+'/project.pickle', 'wb'))

  def printHelp(self):
    print """
    cloudiosays  -p <project> -c <command> [-v <VM name>] [-h]

      -p|--project    Name of the project you are working in
      -c|--command    The action you want to take 
      -v|--vm         Name of the virtual machine you want to work with 
      -h|--help       This help

    Available Projects
    """
    for projectname,projectid in self.project_arr.iteritems():
      print "   - "+projectname

    print """
    Available Commands 

     - listvms
     - createvm
     - destroyvm
     - stopvm
     - startvm
     - listisos
     - listvolumes
     - listdiskofferings
     - listprojects


    """
  def setProjectID(self, projectname):
    self.projectid = self.project_arr[projectname]
  def getPrjectIds(self):
    return self.project_arr

  def printProjects(self):
    res = self.listProjects()
    for item in res['listprojectsresponse']['project']:
      print item['name']+" \t "+item['id'] 

  def printDiskOfferings(self):
    res = self.listDiskOfferings()
    for item in res['listdiskofferingsresponse']['diskoffering']:
      print item['name']+" \t "+item['id'] 

  def getVolumesByName(self):
    res = self.listVolumes(
        "", #account = 
        "", #diskOfferingId = 
        "", #displayVolume = 
        "", #domainId = 
        "", #hostId = 
        "", #id = 
        "", #isRecursive = 
        "", #keyword = 
        "", #listAll = 
        "", #name = 
        "", #page = 
        "", #pageSize = 
        "", #podId = 
        self.projectid, #projectId 
        "", #storageId = 
        "", #tags = 
        "", #type = 
        "", #virtualMachineId = 
        ""  #zoneId = 
    )
    volumesList = {};

    for volume in res['listvolumesresponse']['volume']: 
      if volume['state'] != "Ready":
        volume['vmstate'] = "Stopped"
        volumesList[volume['name']] = volume
      elif volume['type'] == "ROOT":
        volumesList[volume['vmname']] = volume
      else: 
        if not volume.has_key("vmstate"):
            volume['vmstate'] = "Stopped"
        volume['serviceofferingname'] = "DATADISK"
        volumesList[volume['name']] = volume

    return volumesList

  def printVolumes(self):

    volumesList = self.getVolumesByName()
    for vmname, volume in volumesList.iteritems():
      vm = self.colors[volume['vmstate']]+vmname+self.colors['Reset']
      size = str(volume['size']/1073741824)
      print vm.ljust(30)+" \t"+size+" GB"+" \t "+volume['serviceofferingname']


  def destroyVM(self, vmname, expunge):
    vm = self.getVMListByHame()
    res = self.destroyVirtualMachine(vm[vmname]['id'], expunge)

  def startVM(self, vmname):
    vm = self.getVMListByHame()
    res = self.startVirtualMachine(vm[vmname]['id'])

  def stopVM(self, vmname):
    vm = self.getVMListByHame()
    res = self.stopVirtualMachine(vm[vmname]['id'])

  def getVMListByHame(self):
    res = self.listVirtualMachines(
      "", #account 
      "", #affinityGroupId 
      "", #details 
      "", #displayVm  
      "", #domainId 
      "", #forVirtualNetwork  
      "", #groupId  
      "", #hostId 
      "", #hypervisor  
      "", #id  
      "", #ids 
      "", #isoId 
      "", #isRecursive  
      "", #keyword  
      "true", #listAll 
      "", #name 
      "", #networkId  
      "", #page 
      "", #pageSize  
      "", #podId 
      self.projectid, #projectId 
      "", #serviceOfferingId 
      "", #state  
      "", #storageId
      "", #tags 
      "", #templateId
      "", #vpcId
      "", #zoneId
      )
    vmlist = {};

    for item in res['listvirtualmachinesresponse']['virtualmachine']: 
      vmlist[item['name']] = item

    return vmlist

  def printVirtualMachines(self):

    vmlist = self.getVMListByHame()
    volumesList = self.getVolumesByName()
    for vmname, item in vmlist.iteritems():
      vm = self.colors[item['state']]+item['displayname']+self.colors['Reset']
      size = str(volumesList[vmname]['size']/1073741824)
      print vm.ljust(30)+" \t"+item['serviceofferingname']+"\t"+size+" GB \t"+volumesList[vmname]['serviceofferingname']



  def createVM(self, rolename):
    vmlist = self.getVMListByHame()
    volumelist = self.getVolumesByName()

    templatevm        = rolename+"-1"
    #isoid             = vmlist[templatevm]['isoid']
    serviceofferingid = vmlist[templatevm]['serviceofferingid']
    zoneid            = vmlist[templatevm]['zoneid']
    disksize          = str(volumelist[templatevm]['size']/1073741824)
    nicids            = ''
    nicnames          = ''
    for nic in vmlist[templatevm]['nic']:
      nicids += nic['networkid']+","
      nicnames += nic['networkname']+","

    iso = self.getIsos(zoneid)
    isoid             = iso[0]['id']

    for i in range(1, 100):
      if vmlist.has_key(rolename+"-"+str(i)):
        continue
      vmname = rolename+"-"+str(i)
      break

    print self.colors['Title']+"Next VM of service "+rolename+" will have these parameters : "+self.colors['Reset']
    print "VM Name         : "+vmname
    print "Zone            : "+vmlist[templatevm]['zonename']
    print "Project         : "+vmlist[templatevm]['project']
    print "Serviceoffering : "+vmlist[templatevm]['serviceofferingname']
    print "ISO             : "+iso[0]['name']
    print "Networks        : "+nicnames
    print "Disksize        : "+disksize+" GB"+volumelist[templatevm]['serviceofferingid']
    print "Diskoffering    : "+volumelist[templatevm]['serviceofferingname']

    q = self.colors['Question']+"Do you agree with these parameters ?"+self.colors['Reset']
    create = raw_input("%s [y/N] " % q) == 'y'
    if create:
      print "creating "+vmname
  
    res = self.deployVirtualMachine(
      serviceofferingid, #serviceOfferingId, 
      iso[0]['id'], #templateId, 
      zoneid, #zoneId, 
      "", #account = "", 
      "", #affinityGroupIds = "", 
      "", #affinityGroupNames = "", 
      "", #customId = "", 
      "", #deploymentPlanner = "", 
      "", #details = "", 
      volumelist[templatevm]['serviceofferingid'], #diskOfferingId = "", 
      "", #displayName = "", 
      "", #displayVm = "", 
      "", #domainId = "", 
      "", #group = "", 
      "", #hostId = "", 
      "vmware", #hypervisor = "", 
      "", #ip6Address = "", 
      "", #ipAddress = "", 
      "", #ipToNetWorkList = "", 
      "", #keyboard = "", 
      "", #keyPair = "", 
      vmname, #name = "", 
      nicids, #networkIds = "", 
      self.projectid, #projectId = "", 
      "", #rootDiskSize = "", 
      "", #securityGroupIds = "", 
      "", #securityGroupNames = "", 
      disksize, #size = "", 
      "", #startVm = "", 
      "", #userData = ""
    )

    print res


  def getIsos(self, zoneid=""):
    res = self.listIsos(
      "", #account
      "", #bootable
      "", #domainId
      "", #hypervisor
      "", #id
      "executable", #isoFilter
      "", #isPublic
      "", #isReady
      "", #isRecursive
      "", #keyword
      "", #listAll
      "", #name
      "", #page
      "", #pageSize
      self.projectid, #projectId
      "", #showRemoved
      "", #tags
      zoneid, #zoneId
    )
    #int(datetime.datetime.strptime('01/12/2011', '%d/%m/%Y').strftime("%s"))
    return res['listisosresponse']['iso']


