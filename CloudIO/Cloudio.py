from CloudIO.Client import CloudStackClient

import sys, getopt, re, os, pickle, time
class Cloudio(CloudStackClient):

  colors = {
    'Running':    '\033[m\033[0;32m', 
    'Migrating':  '\033[m\033[0;37m', 
    'Stopped':    '\033[m\033[0;31m', 
    'Stopping':   '\033[m\033[0;33m', 
    'Expunging':  '\033[m\033[0;36m', 
    'Starting':   '\033[m\033[0;34m',
    'Destroyed':  '\033[m\033[0;35m',
    'Error':      '\033[m\033[0;35m',
    'OK':         '\033[m\033[0;32m',
    'Title':      '\033[m\033[1;30m\033[38;5;255m',
    'Question':   '\033[m\033[1;30m\033[38;5;226m',
    'Reset':      '\033[0m',
  }

  config = {}

  projects = {}

  projectid = ""

  def __init__(self):
  
    self.config = self.read_config()

    self.apiKey     = self.config['apiKey']
    self.secretKey  = self.config['secretKey']
    self.auth       = True
    self.url        = self.config['apiUrl']

    self.projects = self.read_projects()

  def read_config(self):
    os.environ.setdefault('CLOUDIO_HOME', '/usr/local/share/cloudio')
    conf = {}
    home = os.environ['CLOUDIO_HOME'].rstrip('/')
    config_filename = home + '/config.pickle'

    if os.path.isfile(config_filename):
      conf = pickle.load(open(config_filename, 'rb'))
    else:
      if not os.path.exists(home):
        os.makedirs(home)
      q = self.colors['Question']+"Api URL : "+self.colors['Reset']
      conf['apiUrl'] = raw_input(q)

      q = self.colors['Question']+"Api Key : "+self.colors['Reset']
      conf['apiKey'] = raw_input(q)

      q = self.colors['Question']+"Secret Key : "+self.colors['Reset']
      conf['secretKey'] = raw_input(q)
      pickle.dump(conf, open(config_filename, 'wb'))

    # add configuration variables that don't need to be pickled
    conf['home'] = home
    conf['config_filename'] = config_filename
    conf['project_filename'] = home + '/project.pickle'

    return conf

  def read_projects(self, config = None):
    if config is None: config = self.config
    project_filename = config['home'] + '/project.pickle'
    if os.path.isfile(project_filename):
      projects = pickle.load(open(project_filename, 'rb'))
    else:
      projects = {}
      res = self.listProjects()
      for item in res['listprojectsresponse']['project']:
        projects[item['name']] = item['id']

    pickle.dump(projects, open(project_filename, 'wb'))
    return projects

  def printHelp(self):
    print """
    cloudiosays  -p <project> -c <command> [-v <VM name>] [-h]

      -p|--project    Name of the project you are working in
      -c|--command    The action you want to take 
      -v|--vm         Name of the virtual machine you want to work with 
      -h|--help       This help

    Available Projects
    """
    for projectname,projectid in self.projects.iteritems():
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

  def obsessJob(self, jobID):
    status = "NotDone"

    while status != "Done":
      res = self.queryAsyncJobResult(jobID)
      if res['queryasyncjobresultresponse']['jobstatus'] == 0:
        time.sleep( 3 )
        sys.stdout.write('#')
        sys.stdout.flush()
      else:
        print self.colors['OK']+" [Done]"+self.colors['Reset']
        status = "Done"

  def setProjectID(self, projectname):
    self.projectid = self.projects[projectname]
  def getPrjectIds(self):
    return self.projects

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
    job = self.destroyVirtualMachine(vm[vmname]['id'], expunge)
    return job['destroyvirtualmachineresponse']['jobid']

  def startVM(self, vmname):
    vm = self.getVMListByHame()
    job = self.startVirtualMachine(vm[vmname]['id'])
    return job['startvirtualmachineresponse']['jobid']

  def stopVM(self, vmname):
    vm = self.getVMListByHame()
    job = self.stopVirtualMachine(vm[vmname]['id'])
    return job['stopvirtualmachineresponse']['jobid']

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
      if volumesList.has_key(vmname):
        size = str(volumesList[vmname]['size']/1073741824)
        serviceofferingname = volumesList[vmname]['serviceofferingname']
      else:
        size = "UNKNOWN"
        serviceofferingname = "UNKOWN"
      print vm.ljust(30)+" \t"+item['serviceofferingname']+"\t"+size+" GB \t"+serviceofferingname



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
  
      job = self.deployVirtualMachine(
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
      return job['deployvirtualmachineresponse']['jobid']

    return "None"


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


