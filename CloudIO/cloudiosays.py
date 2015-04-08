#!/usr/bin/python

import sys, getopt, Cloudio, re, os, pickle
import json

def inventory():
   """entry point that converts the list of all VMS to an ansible inventory."""
   data = {}
   client = Cloudio.Cloudio()
   projects = client.getProjectIds()
   for i in projects:
      client.setProjectID(i)
      vmlist = client.getVMListByHame()
      data[i] = []
      for vmname, vmdata in vmlist.iteritems():
         data[i].append(vmname)

   print json.dumps(data)

def main(argv = sys.argv[1:]):
   vmname = None
   project = None
   command = None
   obsess = False
   jobid = "None"

   client = Cloudio.Cloudio()
   project_arr = client.getProjectIds()

   try:
      opts, args = getopt.getopt(argv,"hop:c:v:",["project=","command=", "vm=", "help", "obsess"])
   except getopt.GetoptError:
      print sys.argv[0] + ' -p <project> -c <command>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help"):
         client.printHelp()
         sys.exit()
      elif opt in ("-p", "--project"):
         project = arg
         client.setProjectID(project)
      elif opt in ("-c", "--command"):
         command = arg
      elif opt in ("-v", "--vm"):
         vmname = arg
      elif opt in ("-o", "--obsess"):
         obsess = True

   if command == 'listisos':
      client.getIsos(project_arr[project])
   if command == 'listvms':
      client.printVirtualMachines()
   elif command == 'stopvm':
      if isinstance(vmname, str) & isinstance(project, str):
         jobid = client.stopVM(vmname)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'startvm':
      if isinstance(vmname, str) & isinstance(project, str):
         jobid = client.startVM(vmname)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'createvm':
      if isinstance(vmname, str) & isinstance(project, str):
         jobid = client.createVM(vmname)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'destroyvm':
      if isinstance(vmname, str) & isinstance(project, str):
         msg = "Expunge vm "+vmname+" ?"
         expunge = raw_input("%s (y/N) " % msg).lower() == 'y'
         expunge = str(expunge).lower()
         jobid = client.destroyVM(vmname, expunge)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'listprojects':
      client.printProjects()
   elif command == 'listdiskofferings':
      client.printDiskOfferings()
   elif command == 'listvolumes':
      client.printVolumes()

   if obsess and jobid != "None":
      print "Running: ",
      client.obsessJob(jobid)


if __name__ == "__main__":
   main()