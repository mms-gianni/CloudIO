#!/usr/bin/python

import sys, getopt, Cloudio, re, os, pickle, help


def main(argv):
   vmname = None
   project = None
   command = None


   client = Cloudio.Cloudio()
   project_arr = client.getPrjectIds()


   try:
      opts, args = getopt.getopt(argv,"hp:c:v:",["project=","command=", "vm=", "help"])
   except getopt.GetoptError:
      print 'test.py -p <project> -c <command>'
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

   if command == 'listisos':
      client.getIsos(project_arr[project])
   if command == 'listvms':
      client.printVirtualMachines()
   elif command == 'stopvm':
      if isinstance(vmname, str) & isinstance(project, str):
         client.stopVM(vmname)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'startvm':
      if isinstance(vmname, str) & isinstance(project, str):
         client.startVM(vmname)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'createvm':
      if isinstance(vmname, str) & isinstance(project, str):
         client.createVM(vmname)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'destroyvm':
      if isinstance(vmname, str) & isinstance(project, str):
         msg = "Expunge vm "+vmname+" ?"
         expunge = raw_input("%s (y/N) " % msg).lower() == 'y'
         expunge = str(expunge).lower()
         client.destroyVM(vmname, expunge)
      else:
         print "Error: vmname and project must be provided"
   elif command == 'listprojects':
      client.printProjects()
   elif command == 'listdiskofferings':
      client.printDiskOfferings()
   elif command == 'listvolumes':
      client.printVolumes()

      


if __name__ == "__main__":
   main(sys.argv[1:])
