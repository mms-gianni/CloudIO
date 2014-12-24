# Genereated and manually fixed 
# Gerator : https://github.com/demarey/cloudstack-client-generator
from BaseClient import BaseCloudStackClient


class CloudStackClient(BaseCloudStackClient):

    def createLoadBalancerRule(self, algorithm, name, privatePort, publicPort, account = "", cidrList = "", description = "", domainId = "", forDisplay = "", networkId = "", openFirewall = "", protocol = "", publicIpId = "", zoneId = ""):
        '''
        Creates a load balancer rule
        '''

        return self.request("createLoadBalancerRule", {
            'algorithm' : algorithm,
            'name' : name,
            'privateport' : privatePort,
            'publicport' : publicPort,
            'account' : account,
            'cidrlist' : cidrList,
            'description' : description,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'networkid' : networkId,
            'openfirewall' : openFirewall,
            'protocol' : protocol,
            'publicipid' : publicIpId,
            'zoneid' : zoneId,
        })
    
    def deleteLoadBalancerRule(self, id):
        '''
        Deletes a load balancer rule.
        '''

        return self.request("deleteLoadBalancerRule", {
            'id' : id,
        })
    
    def removeFromLoadBalancerRule(self, id, virtualMachineIds = "", vmIdIpMap = ""):
        '''
        Removes a virtual machine or a list of virtual machines from a load balancer rule.
        '''

        return self.request("removeFromLoadBalancerRule", {
            'id' : id,
            'virtualmachineids' : virtualMachineIds,
            'vmidipmap' : vmIdIpMap,
        })
    
    def assignToLoadBalancerRule(self, id, virtualMachineIds = "", vmIdIpMap = ""):
        '''
        Assigns virtual machine or a list of virtual machines to a load balancer rule.
        '''

        return self.request("assignToLoadBalancerRule", {
            'id' : id,
            'virtualmachineids' : virtualMachineIds,
            'vmidipmap' : vmIdIpMap,
        })
    
    def createLBStickinessPolicy(self, lbruleId, methodName, name, description = "", forDisplay = "", param = ""):
        '''
        Creates a Load Balancer stickiness policy
        '''

        return self.request("createLBStickinessPolicy", {
            'lbruleid' : lbruleId,
            'methodname' : methodName,
            'name' : name,
            'description' : description,
            'fordisplay' : forDisplay,
            'param' : param,
        })
    
    def updateLBStickinessPolicy(self, id, customId = "", forDisplay = ""):
        '''
        Updates LB Stickiness policy
        '''

        return self.request("updateLBStickinessPolicy", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def deleteLBStickinessPolicy(self, id):
        '''
        Deletes a LB stickiness policy.
        '''

        return self.request("deleteLBStickinessPolicy", {
            'id' : id,
        })
    
    def listLoadBalancerRules(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", projectId = "", publicIpId = "", tags = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists load balancer rules.
        '''

        return self.request("listLoadBalancerRules", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'publicipid' : publicIpId,
            'tags' : tags,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def listLBStickinessPolicies(self, forDisplay = "", id = "", keyword = "", lbruleId = "", page = "", pageSize = ""):
        '''
        Lists LBStickiness policies.
        '''

        return self.request("listLBStickinessPolicies", {
            'fordisplay' : forDisplay,
            'id' : id,
            'keyword' : keyword,
            'lbruleid' : lbruleId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listLBHealthCheckPolicies(self, forDisplay = "", id = "", keyword = "", lbruleId = "", page = "", pageSize = ""):
        '''
        Lists load balancer HealthCheck policies.
        '''

        return self.request("listLBHealthCheckPolicies", {
            'fordisplay' : forDisplay,
            'id' : id,
            'keyword' : keyword,
            'lbruleid' : lbruleId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createLBHealthCheckPolicy(self, lbruleId, description = "", forDisplay = "", healthyTreshold = "", intervalTime = "", pingPath = "", responseTimeout = "", unhealthyThreshold = ""):
        '''
        Creates a Load Balancer healthcheck policy
        '''

        return self.request("createLBHealthCheckPolicy", {
            'lbruleid' : lbruleId,
            'description' : description,
            'fordisplay' : forDisplay,
            'healthythreshold' : healthyTreshold,
            'intervaltime' : intervalTime,
            'pingpath' : pingPath,
            'responsetimeout' : responseTimeout,
            'unhealthythreshold' : unhealthyThreshold,
        })
    
    def updateLBHealthCheckPolicy(self, id, customId = "", forDisplay = ""):
        '''
        Updates LB HealthCheck policy
        '''

        return self.request("updateLBHealthCheckPolicy", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def deleteLBHealthCheckPolicy(self, id):
        '''
        Deletes a load balancer HealthCheck policy.
        '''

        return self.request("deleteLBHealthCheckPolicy", {
            'id' : id,
        })
    
    def listLoadBalancerRuleInstances(self, id, applied = "", keyword = "", lbVmIps = "", page = "", pageSize = ""):
        '''
        List all virtual machine instances that are assigned to a load balancer rule.
        '''

        return self.request("listLoadBalancerRuleInstances", {
            'id' : id,
            'applied' : applied,
            'keyword' : keyword,
            'lbvmips' : lbVmIps,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def updateLoadBalancerRule(self, id, algorithm = "", customId = "", description = "", forDisplay = "", name = ""):
        '''
        Updates load balancer
        '''

        return self.request("updateLoadBalancerRule", {
            'id' : id,
            'algorithm' : algorithm,
            'customid' : customId,
            'description' : description,
            'fordisplay' : forDisplay,
            'name' : name,
        })
    
    def uploadSslCert(self, certificate, privateKey, account = "", certChain = "", domainId = "", password = "", projectId = ""):
        '''
        Upload a certificate to cloudstack
        '''

        return self.request("uploadSslCert", {
            'certificate' : certificate,
            'privatekey' : privateKey,
            'account' : account,
            'certchain' : certChain,
            'domainid' : domainId,
            'password' : password,
            'projectid' : projectId,
        })
    
    def deleteSslCert(self, id):
        '''
        Delete a certificate to cloudstack
        '''

        return self.request("deleteSslCert", {
            'id' : id,
        })
    
    def listSslCerts(self, accountId = "", certId = "", lbruleId = "", projectId = ""):
        '''
        Lists SSL certificates
        '''

        return self.request("listSslCerts", {
            'accountid' : accountId,
            'certid' : certId,
            'lbruleid' : lbruleId,
            'projectid' : projectId,
        })
    
    def assignCertToLoadBalancer(self, certId, lbruleId):
        '''
        Assigns a certificate to a Load Balancer Rule
        '''

        return self.request("assignCertToLoadBalancer", {
            'certid' : certId,
            'lbruleid' : lbruleId,
        })
    
    def removeCertFromLoadBalancer(self, lbruleId):
        '''
        Removes a certificate from a Load Balancer Rule
        '''

        return self.request("removeCertFromLoadBalancer", {
            'lbruleid' : lbruleId,
        })
    
    def createGlobalLoadBalancerRule(self, gslbDomainName, gslbServiceType, name, regionId, account = "", description = "", domainId = "", gslblbMethod = "", gslbStickySessionMethodName = ""):
        '''
        Creates a global load balancer rule
        '''

        return self.request("createGlobalLoadBalancerRule", {
            'gslbdomainname' : gslbDomainName,
            'gslbservicetype' : gslbServiceType,
            'name' : name,
            'regionid' : regionId,
            'account' : account,
            'description' : description,
            'domainid' : domainId,
            'gslblbmethod' : gslblbMethod,
            'gslbstickysessionmethodname' : gslbStickySessionMethodName,
        })
    
    def deleteGlobalLoadBalancerRule(self, id):
        '''
        Deletes a global load balancer rule.
        '''

        return self.request("deleteGlobalLoadBalancerRule", {
            'id' : id,
        })
    
    def updateGlobalLoadBalancerRule(self, id, description = "", gslblbMethod = "", gslbStickySessionMethodName = ""):
        '''
        update global load balancer rules.
        '''

        return self.request("updateGlobalLoadBalancerRule", {
            'id' : id,
            'description' : description,
            'gslblbmethod' : gslblbMethod,
            'gslbstickysessionmethodname' : gslbStickySessionMethodName,
        })
    
    def listGlobalLoadBalancerRules(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", regionId = "", tags = ""):
        '''
        Lists load balancer rules.
        '''

        return self.request("listGlobalLoadBalancerRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'regionid' : regionId,
            'tags' : tags,
        })
    
    def assignToGlobalLoadBalancerRule(self, id, loadBalancerRuleList, gslblbRuleWeightsMap = ""):
        '''
        Assign load balancer rule or list of load balancer rules to a global load balancer rules.
        '''

        return self.request("assignToGlobalLoadBalancerRule", {
            'id' : id,
            'loadbalancerrulelist' : loadBalancerRuleList,
            'gslblbruleweightsmap' : gslblbRuleWeightsMap,
        })
    
    def removeFromGlobalLoadBalancerRule(self, id, loadBalancerRuleList):
        '''
        Removes a load balancer rule association with global load balancer rule
        '''

        return self.request("removeFromGlobalLoadBalancerRule", {
            'id' : id,
            'loadbalancerrulelist' : loadBalancerRuleList,
        })
    
    def createLoadBalancer(self, algorithm, instancePort, name, networkId, scheme, sourceIpAddressNetworkId, sourcePort, description = "", forDisplay = "", sourceIpAddress = ""):
        '''
        Creates a Load Balancer
        '''

        return self.request("createLoadBalancer", {
            'algorithm' : algorithm,
            'instanceport' : instancePort,
            'name' : name,
            'networkid' : networkId,
            'scheme' : scheme,
            'sourceipaddressnetworkid' : sourceIpAddressNetworkId,
            'sourceport' : sourcePort,
            'description' : description,
            'fordisplay' : forDisplay,
            'sourceipaddress' : sourceIpAddress,
        })
    
    def listLoadBalancers(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", projectId = "", scheme = "", sourceIpAddress = "", sourceIpAddressNetworkId = "", tags = ""):
        '''
        Lists Load Balancers
        '''

        return self.request("listLoadBalancers", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'scheme' : scheme,
            'sourceipaddress' : sourceIpAddress,
            'sourceipaddressnetworkid' : sourceIpAddressNetworkId,
            'tags' : tags,
        })
    
    def deleteLoadBalancer(self, id):
        '''
        Deletes a load balancer
        '''

        return self.request("deleteLoadBalancer", {
            'id' : id,
        })
    
    def updateLoadBalancer(self, id, customId = "", forDisplay = ""):
        '''
        Updates a Load Balancer
        '''

        return self.request("updateLoadBalancer", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def createRemoteAccessVpn(self, publicIpId, account = "", domainId = "", forDisplay = "", ipRange = "", openFirewall = ""):
        '''
        Creates a l2tp/ipsec remote access vpn
        '''

        return self.request("createRemoteAccessVpn", {
            'publicipid' : publicIpId,
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'iprange' : ipRange,
            'openfirewall' : openFirewall,
        })
    
    def deleteRemoteAccessVpn(self, publicIpId):
        '''
        Destroys a l2tp/ipsec remote access vpn
        '''

        return self.request("deleteRemoteAccessVpn", {
            'publicipid' : publicIpId,
        })
    
    def listRemoteAccessVpns(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", networkId = "", page = "", pageSize = "", projectId = "", publicIpId = ""):
        '''
        Lists remote access vpns
        '''

        return self.request("listRemoteAccessVpns", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'publicipid' : publicIpId,
        })
    
    def updateRemoteAccessVpn(self, id, customId = "", forDisplay = ""):
        '''
        Updates remote access vpn
        '''

        return self.request("updateRemoteAccessVpn", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def addVpnUser(self, password, userName, account = "", domainId = "", projectId = ""):
        '''
        Adds vpn users
        '''

        return self.request("addVpnUser", {
            'password' : password,
            'username' : userName,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def removeVpnUser(self, userName, account = "", domainId = "", projectId = ""):
        '''
        Removes vpn user
        '''

        return self.request("removeVpnUser", {
            'username' : userName,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def listVpnUsers(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", userName = ""):
        '''
        Lists vpn users
        '''

        return self.request("listVpnUsers", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'username' : userName,
        })
    
    def createVpnCustomerGateway(self, cidrList, espPolicy, gateway, ikePolicy, ipsecPsk, account = "", domainId = "", dpd = "", espLifeTime = "", ikeLifeTime = "", name = ""):
        '''
        Creates site to site vpn customer gateway
        '''

        return self.request("createVpnCustomerGateway", {
            'cidrlist' : cidrList,
            'esppolicy' : espPolicy,
            'gateway' : gateway,
            'ikepolicy' : ikePolicy,
            'ipsecpsk' : ipsecPsk,
            'account' : account,
            'domainid' : domainId,
            'dpd' : dpd,
            'esplifetime' : espLifeTime,
            'ikelifetime' : ikeLifeTime,
            'name' : name,
        })
    
    def createVpnGateway(self, vpcId, forDisplay = ""):
        '''
        Creates site to site vpn local gateway
        '''

        return self.request("createVpnGateway", {
            'vpcid' : vpcId,
            'fordisplay' : forDisplay,
        })
    
    def createVpnConnection(self, s2sCustomerGatewayId, s2sVpnGatewayId, forDisplay = "", passive = ""):
        '''
        Create site to site vpn connection
        '''

        return self.request("createVpnConnection", {
            's2scustomergatewayid' : s2sCustomerGatewayId,
            's2svpngatewayid' : s2sVpnGatewayId,
            'fordisplay' : forDisplay,
            'passive' : passive,
        })
    
    def deleteVpnCustomerGateway(self, id):
        '''
        Delete site to site vpn customer gateway
        '''

        return self.request("deleteVpnCustomerGateway", {
            'id' : id,
        })
    
    def deleteVpnGateway(self, id):
        '''
        Delete site to site vpn gateway
        '''

        return self.request("deleteVpnGateway", {
            'id' : id,
        })
    
    def deleteVpnConnection(self, id):
        '''
        Delete site to site vpn connection
        '''

        return self.request("deleteVpnConnection", {
            'id' : id,
        })
    
    def updateVpnCustomerGateway(self, id, cidrList, espPolicy, gateway, ikePolicy, ipsecPsk, account = "", domainId = "", dpd = "", espLifeTime = "", ikeLifeTime = "", name = ""):
        '''
        Update site to site vpn customer gateway
        '''

        return self.request("updateVpnCustomerGateway", {
            'id' : id,
            'cidrlist' : cidrList,
            'esppolicy' : espPolicy,
            'gateway' : gateway,
            'ikepolicy' : ikePolicy,
            'ipsecpsk' : ipsecPsk,
            'account' : account,
            'domainid' : domainId,
            'dpd' : dpd,
            'esplifetime' : espLifeTime,
            'ikelifetime' : ikeLifeTime,
            'name' : name,
        })
    
    def resetVpnConnection(self, id, account = "", domainId = ""):
        '''
        Reset site to site vpn connection
        '''

        return self.request("resetVpnConnection", {
            'id' : id,
            'account' : account,
            'domainid' : domainId,
        })
    
    def listVpnCustomerGateways(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists site to site vpn customer gateways
        '''

        return self.request("listVpnCustomerGateways", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def listVpnGateways(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", vpcId = ""):
        '''
        Lists site 2 site vpn gateways
        '''

        return self.request("listVpnGateways", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'vpcid' : vpcId,
        })
    
    def listVpnConnections(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", vpcId = ""):
        '''
        Lists site to site vpn connection gateways
        '''

        return self.request("listVpnConnections", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'vpcid' : vpcId,
        })
    
    def updateVpnConnection(self, id, customId = "", forDisplay = ""):
        '''
        Updates site to site vpn connection
        '''

        return self.request("updateVpnConnection", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def updateVpnGateway(self, id, customId = "", forDisplay = ""):
        '''
        Updates site to site vpn local gateway
        '''

        return self.request("updateVpnGateway", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def deployVirtualMachine(self, serviceOfferingId, templateId, zoneId, account = "", affinityGroupIds = "", affinityGroupNames = "", customId = "", deploymentPlanner = "", details = "", diskOfferingId = "", displayName = "", displayVm = "", domainId = "", group = "", hostId = "", hypervisor = "", ip6Address = "", ipAddress = "", ipToNetWorkList = "", keyboard = "", keyPair = "", name = "", networkIds = "", projectId = "", rootDiskSize = "", securityGroupIds = "", securityGroupNames = "", size = "", startVm = "", userData = ""):
        '''
        Creates and automatically starts a virtual machine based on a service offering, disk offering, and template.
        '''

        return self.request("deployVirtualMachine", {
            'serviceofferingid' : serviceOfferingId,
            'templateid' : templateId,
            'zoneid' : zoneId,
            'account' : account,
            'affinitygroupids' : affinityGroupIds,
            'affinitygroupnames' : affinityGroupNames,
            'customid' : customId,
            'deploymentplanner' : deploymentPlanner,
            'details' : details,
            'diskofferingid' : diskOfferingId,
            'displayname' : displayName,
            'displayvm' : displayVm,
            'domainid' : domainId,
            'group' : group,
            'hostid' : hostId,
            'hypervisor' : hypervisor,
            'ip6address' : ip6Address,
            'ipaddress' : ipAddress,
            'iptonetworklist' : ipToNetWorkList,
            'keyboard' : keyboard,
            'keypair' : keyPair,
            'name' : name,
            'networkids' : networkIds,
            'projectid' : projectId,
            'rootdisksize' : rootDiskSize,
            'securitygroupids' : securityGroupIds,
            'securitygroupnames' : securityGroupNames,
            'size' : size,
            'startvm' : startVm,
            'userdata' : userData,
        })
    
    def destroyVirtualMachine(self, id, expunge = ""):
        '''
        Destroys a virtual machine. Once destroyed, only the administrator can recover it.
        '''

        return self.request("destroyVirtualMachine", {
            'id' : id,
            'expunge' : expunge,
        })
    
    def rebootVirtualMachine(self, id):
        '''
        Reboots a virtual machine.
        '''

        return self.request("rebootVirtualMachine", {
            'id' : id,
        })
    
    def startVirtualMachine(self, id, deploymentPlanner = "", hostId = ""):
        '''
        Starts a virtual machine.
        '''

        return self.request("startVirtualMachine", {
            'id' : id,
            'deploymentplanner' : deploymentPlanner,
            'hostid' : hostId,
        })
    
    def stopVirtualMachine(self, id, forced = ""):
        '''
        Stops a virtual machine.
        '''

        return self.request("stopVirtualMachine", {
            'id' : id,
            'forced' : forced,
        })
    
    def resetPasswordForVirtualMachine(self, id):
        '''
        Resets the password for virtual machine. The virtual machine must be in a "Stopped" state and the template must already support this feature for this command to take effect. [async]
        '''

        return self.request("resetPasswordForVirtualMachine", {
            'id' : id,
        })
    
    def updateVirtualMachine(self, id, customId = "", displayName = "", displayVm = "", group = "", haEnable = "", isDynamicallyScalable = "", name = "", osTypeId = "", userData = ""):
        '''
        Updates properties of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect. UpdateVirtualMachine does not first check whether the VM is stopped. Therefore, stop the VM manually before issuing this call.
        '''

        return self.request("updateVirtualMachine", {
            'id' : id,
            'customid' : customId,
            'displayname' : displayName,
            'displayvm' : displayVm,
            'group' : group,
            'haenable' : haEnable,
            'isdynamicallyscalable' : isDynamicallyScalable,
            'name' : name,
            'ostypeid' : osTypeId,
            'userdata' : userData,
        })
    
    def listVirtualMachines(self, account = "", affinityGroupId = "", details = "", displayVm = "", domainId = "", forVirtualNetwork = "", groupId = "", hostId = "", hypervisor = "", id = "", ids = "", isoId = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", podId = "", projectId = "", serviceOfferingId = "", state = "", storageId = "", tags = "", templateId = "", vpcId = "", zoneId = ""):
        '''
        List the virtual machines owned by the account.
        '''

        return self.request("listVirtualMachines", {
            'account' : account,
            'affinitygroupid' : affinityGroupId,
            'details' : details,
            'displayvm' : displayVm,
            'domainid' : domainId,
            'forvirtualnetwork' : forVirtualNetwork,
            'groupid' : groupId,
            'hostid' : hostId,
            'hypervisor' : hypervisor,
            'id' : id,
            'ids' : ids,
            'isoid' : isoId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'serviceofferingid' : serviceOfferingId,
            'state' : state,
            'storageid' : storageId,
            'tags' : tags,
            'templateid' : templateId,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def getVMPassword(self, id):
        '''
        Returns an encrypted password for the VM
        '''

        return self.request("getVMPassword", {
            'id' : id,
        })
    
    def restoreVirtualMachine(self, virtualMachineId, templateId = ""):
        '''
        Restore a VM to original template/ISO or new template/ISO
        '''

        return self.request("restoreVirtualMachine", {
            'virtualmachineid' : virtualMachineId,
            'templateid' : templateId,
        })
    
    def changeServiceForVirtualMachine(self, id, serviceOfferingId, details = ""):
        '''
        Changes the service offering for a virtual machine. The virtual machine must be in a "Stopped" state for this command to take effect.
        '''

        return self.request("changeServiceForVirtualMachine", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
            'details' : details,
        })
    
    def scaleVirtualMachine(self, id, serviceOfferingId, details = ""):
        '''
        Scales the virtual machine to a new service offering.
        '''

        return self.request("scaleVirtualMachine", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
            'details' : details,
        })
    
    def assignVirtualMachine(self, account, domainId, virtualMachineId, networkIds = "", securityGroupIds = ""):
        '''
        Change ownership of a VM from one account to another. This API is available for Basic zones with security groups and Advanced zones with guest networks. A root administrator can reassign a VM from any account to any other account in any domain. A domain administrator can reassign a VM to any account in the same domain.
        '''

        return self.request("assignVirtualMachine", {
            'account' : account,
            'domainid' : domainId,
            'virtualmachineid' : virtualMachineId,
            'networkids' : networkIds,
            'securitygroupids' : securityGroupIds,
        })
    
    def recoverVirtualMachine(self, id):
        '''
        Recovers a virtual machine.
        '''

        return self.request("recoverVirtualMachine", {
            'id' : id,
        })
    
    def expungeVirtualMachine(self, id):
        '''
        Expunge a virtual machine. Once expunged, it cannot be recoverd.
        '''

        return self.request("expungeVirtualMachine", {
            'id' : id,
        })
    
    def addNicToVirtualMachine(self, networkId, virtualMachineId, ipAddress = ""):
        '''
        Adds VM to specified network by creating a NIC
        '''

        return self.request("addNicToVirtualMachine", {
            'networkid' : networkId,
            'virtualmachineid' : virtualMachineId,
            'ipaddress' : ipAddress,
        })
    
    def removeNicFromVirtualMachine(self, nicId, virtualMachineId):
        '''
        Removes VM from specified network by deleting a NIC
        '''

        return self.request("removeNicFromVirtualMachine", {
            'nicid' : nicId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def updateDefaultNicForVirtualMachine(self, nicId, virtualMachineId):
        '''
        Changes the default NIC on a VM
        '''

        return self.request("updateDefaultNicForVirtualMachine", {
            'nicid' : nicId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createCondition(self, counterId, relationalOperator, threshold, account = "", domainId = ""):
        '''
        Creates a condition
        '''

        return self.request("createCondition", {
            'counterid' : counterId,
            'relationaloperator' : relationalOperator,
            'threshold' : threshold,
            'account' : account,
            'domainid' : domainId,
        })
    
    def createAutoScalePolicy(self, action, conditionIds, duration, quietTime = ""):
        '''
        Creates an autoscale policy for a provision or deprovision action, the action is taken when the all the conditions evaluates to true for the specified duration. The policy is in effect once it is attached to a autscale vm group.
        '''

        return self.request("createAutoScalePolicy", {
            'action' : action,
            'conditionids' : conditionIds,
            'duration' : duration,
            'quiettime' : quietTime,
        })
    
    def createAutoScaleVmProfile(self, serviceOfferingId, templateId, zoneId, autoscaleUserId = "", counterParam = "", destroyVmGracePeriod = "", forDisplay = "", otherDeployParams = ""):
        '''
        Creates a profile that contains information about the virtual machine which will be provisioned automatically by autoscale feature.
        '''

        return self.request("createAutoScaleVmProfile", {
            'serviceofferingid' : serviceOfferingId,
            'templateid' : templateId,
            'zoneid' : zoneId,
            'autoscaleuserid' : autoscaleUserId,
            'counterparam' : counterParam,
            'destroyvmgraceperiod' : destroyVmGracePeriod,
            'fordisplay' : forDisplay,
            'otherdeployparams' : otherDeployParams,
        })
    
    def createAutoScaleVmGroup(self, lbruleId, maxMembers, minMembers, scaleDownPolicyIds, scaleUpPolicyIds, vmProfileId, forDisplay = "", interval = ""):
        '''
        Creates and automatically starts a virtual machine based on a service offering, disk offering, and template.
        '''

        return self.request("createAutoScaleVmGroup", {
            'lbruleid' : lbruleId,
            'maxmembers' : maxMembers,
            'minmembers' : minMembers,
            'scaledownpolicyids' : scaleDownPolicyIds,
            'scaleuppolicyids' : scaleUpPolicyIds,
            'vmprofileid' : vmProfileId,
            'fordisplay' : forDisplay,
            'interval' : interval,
        })
    
    def deleteCondition(self, id):
        '''
        Removes a condition
        '''

        return self.request("deleteCondition", {
            'id' : id,
        })
    
    def deleteAutoScalePolicy(self, id):
        '''
        Deletes a autoscale policy.
        '''

        return self.request("deleteAutoScalePolicy", {
            'id' : id,
        })
    
    def deleteAutoScaleVmProfile(self, id):
        '''
        Deletes a autoscale vm profile.
        '''

        return self.request("deleteAutoScaleVmProfile", {
            'id' : id,
        })
    
    def deleteAutoScaleVmGroup(self, id):
        '''
        Deletes a autoscale vm group.
        '''

        return self.request("deleteAutoScaleVmGroup", {
            'id' : id,
        })
    
    def listCounters(self, id = "", keyword = "", name = "", page = "", pageSize = "", source = ""):
        '''
        List the counters
        '''

        return self.request("listCounters", {
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'source' : source,
        })
    
    def listConditions(self, account = "", counterId = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", policyId = ""):
        '''
        List Conditions for the specific user
        '''

        return self.request("listConditions", {
            'account' : account,
            'counterid' : counterId,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'policyid' : policyId,
        })
    
    def listAutoScalePolicies(self, account = "", action = "", conditionId = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", vmGroupId = ""):
        '''
        Lists autoscale policies.
        '''

        return self.request("listAutoScalePolicies", {
            'account' : account,
            'action' : action,
            'conditionid' : conditionId,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'vmgroupid' : vmGroupId,
        })
    
    def listAutoScaleVmProfiles(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", otherDeployParams = "", page = "", pageSize = "", projectId = "", serviceOfferingId = "", templateId = "", zoneId = ""):
        '''
        Lists autoscale vm profiles.
        '''

        return self.request("listAutoScaleVmProfiles", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'otherdeployparams' : otherDeployParams,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'serviceofferingid' : serviceOfferingId,
            'templateid' : templateId,
            'zoneid' : zoneId,
        })
    
    def listAutoScaleVmGroups(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", lbruleId = "", listAll = "", page = "", pageSize = "", policyId = "", projectId = "", vmProfileId = "", zoneId = ""):
        '''
        Lists autoscale vm groups.
        '''

        return self.request("listAutoScaleVmGroups", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'lbruleid' : lbruleId,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'policyid' : policyId,
            'projectid' : projectId,
            'vmprofileid' : vmProfileId,
            'zoneid' : zoneId,
        })
    
    def enableAutoScaleVmGroup(self, id):
        '''
        Enables an AutoScale Vm Group
        '''

        return self.request("enableAutoScaleVmGroup", {
            'id' : id,
        })
    
    def disableAutoScaleVmGroup(self, id):
        '''
        Disables an AutoScale Vm Group
        '''

        return self.request("disableAutoScaleVmGroup", {
            'id' : id,
        })
    
    def updateAutoScalePolicy(self, id, conditionIds = "", duration = "", quietTime = ""):
        '''
        Updates an existing autoscale policy.
        '''

        return self.request("updateAutoScalePolicy", {
            'id' : id,
            'conditionids' : conditionIds,
            'duration' : duration,
            'quiettime' : quietTime,
        })
    
    def updateAutoScaleVmProfile(self, id, autoscaleUserId = "", counterParam = "", customId = "", destroyVmGracePeriod = "", forDisplay = "", templateId = ""):
        '''
        Updates an existing autoscale vm profile.
        '''

        return self.request("updateAutoScaleVmProfile", {
            'id' : id,
            'autoscaleuserid' : autoscaleUserId,
            'counterparam' : counterParam,
            'customid' : customId,
            'destroyvmgraceperiod' : destroyVmGracePeriod,
            'fordisplay' : forDisplay,
            'templateid' : templateId,
        })
    
    def updateAutoScaleVmGroup(self, id, customId = "", forDisplay = "", interval = "", maxMembers = "", minMembers = "", scaleDownPolicyIds = "", scaleUpPolicyIds = ""):
        '''
        Updates an existing autoscale vm group.
        '''

        return self.request("updateAutoScaleVmGroup", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
            'interval' : interval,
            'maxmembers' : maxMembers,
            'minmembers' : minMembers,
            'scaledownpolicyids' : scaleDownPolicyIds,
            'scaleuppolicyids' : scaleUpPolicyIds,
        })
    
    def createSnapshot(self, volumeId, account = "", domainId = "", policyId = "", quiesceVm = ""):
        '''
        Creates an instant snapshot of a volume.
        '''

        return self.request("createSnapshot", {
            'volumeid' : volumeId,
            'account' : account,
            'domainid' : domainId,
            'policyid' : policyId,
            'quiescevm' : quiesceVm,
        })
    
    def listSnapshots(self, account = "", domainId = "", id = "", intervalType = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", snapshotType = "", tags = "", volumeId = "", zoneId = ""):
        '''
        Lists all available snapshots for the account.
        '''

        return self.request("listSnapshots", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'intervaltype' : intervalType,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'snapshottype' : snapshotType,
            'tags' : tags,
            'volumeid' : volumeId,
            'zoneid' : zoneId,
        })
    
    def deleteSnapshot(self, id):
        '''
        Deletes a snapshot of a disk volume.
        '''

        return self.request("deleteSnapshot", {
            'id' : id,
        })
    
    def createSnapshotPolicy(self, intervalType, maxSnaps, schedule, timezone, volumeId, forDisplay = ""):
        '''
        Creates a snapshot policy for the account.
        '''

        return self.request("createSnapshotPolicy", {
            'intervaltype' : intervalType,
            'maxsnaps' : maxSnaps,
            'schedule' : schedule,
            'timezone' : timezone,
            'volumeid' : volumeId,
            'fordisplay' : forDisplay,
        })
    
    def updateSnapshotPolicy(self, customId = "", forDisplay = "", id = ""):
        '''
        Updates the snapshot policy.
        '''

        return self.request("updateSnapshotPolicy", {
            'customid' : customId,
            'fordisplay' : forDisplay,
            'id' : id,
        })
    
    def deleteSnapshotPolicies(self, id = "", ids = ""):
        '''
        Deletes snapshot policies for the account.
        '''

        return self.request("deleteSnapshotPolicies", {
            'id' : id,
            'ids' : ids,
        })
    
    def listSnapshotPolicies(self, forDisplay = "", id = "", keyword = "", page = "", pageSize = "", volumeId = ""):
        '''
        Lists snapshot policies.
        '''

        return self.request("listSnapshotPolicies", {
            'fordisplay' : forDisplay,
            'id' : id,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'volumeid' : volumeId,
        })
    
    def revertSnapshot(self, id):
        '''
        revert a volume snapshot.
        '''

        return self.request("revertSnapshot", {
            'id' : id,
        })
    
    def listVMSnapshot(self, account = "", domainId = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", state = "", tags = "", virtualMachineId = "", vmSnapshotId = ""):
        '''
        List virtual machine snapshot by conditions
        '''

        return self.request("listVMSnapshot", {
            'account' : account,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'state' : state,
            'tags' : tags,
            'virtualmachineid' : virtualMachineId,
            'vmsnapshotid' : vmSnapshotId,
        })
    
    def createVMSnapshot(self, virtualMachineId, description = "", name = "", quiesceVm = "", snapshotMemory = ""):
        '''
        Creates snapshot for a vm.
        '''

        return self.request("createVMSnapshot", {
            'virtualmachineid' : virtualMachineId,
            'description' : description,
            'name' : name,
            'quiescevm' : quiesceVm,
            'snapshotmemory' : snapshotMemory,
        })
    
    def deleteVMSnapshot(self, vmSnapshotId):
        '''
        Deletes a vmsnapshot.
        '''

        return self.request("deleteVMSnapshot", {
            'vmsnapshotid' : vmSnapshotId,
        })
    
    def revertToVMSnapshot(self, vmSnapshotId):
        '''
        Revert VM from a vmsnapshot.
        '''

        return self.request("revertToVMSnapshot", {
            'vmsnapshotid' : vmSnapshotId,
        })
    
    def listPortForwardingRules(self, account = "", domainId = "", forDisplay = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", networkId = "", page = "", pageSize = "", projectId = "", tags = ""):
        '''
        Lists all port forwarding rules for an IP address.
        '''

        return self.request("listPortForwardingRules", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
        })
    
    def createPortForwardingRule(self, ipAddressId, privatePort, protocol, publicPort, virtualMachineId, cidrList = "", forDisplay = "", networkId = "", openFirewall = "", privateEndPort = "", publicEndPort = "", vmGuestIp = ""):
        '''
        Creates a port forwarding rule
        '''

        return self.request("createPortForwardingRule", {
            'ipaddressid' : ipAddressId,
            'privateport' : privatePort,
            'protocol' : protocol,
            'publicport' : publicPort,
            'virtualmachineid' : virtualMachineId,
            'cidrlist' : cidrList,
            'fordisplay' : forDisplay,
            'networkid' : networkId,
            'openfirewall' : openFirewall,
            'privateendport' : privateEndPort,
            'publicendport' : publicEndPort,
            'vmguestip' : vmGuestIp,
        })
    
    def deletePortForwardingRule(self, id):
        '''
        Deletes a port forwarding rule
        '''

        return self.request("deletePortForwardingRule", {
            'id' : id,
        })
    
    def updatePortForwardingRule(self, id, customId = "", forDisplay = "", ipAddressId = "", privateIp = "", privatePort = "", protocol = "", publicPort = "", virtualMachineId = ""):
        '''
        Updates a port forwarding rule.  Only the private port and the virtual machine can be updated.
        '''

        return self.request("updatePortForwardingRule", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
            'ipaddressid' : ipAddressId,
            'privateip' : privateIp,
            'privateport' : privatePort,
            'protocol' : protocol,
            'publicport' : publicPort,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createFirewallRule(self, ipAddressId, protocol, cidrList = "", endPort = "", forDisplay = "", icmpCode = "", icmpType = "", startPort = "", type = ""):
        '''
        Creates a firewall rule for a given ip address
        '''

        return self.request("createFirewallRule", {
            'ipaddressid' : ipAddressId,
            'protocol' : protocol,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'fordisplay' : forDisplay,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'startport' : startPort,
            'type' : type,
        })
    
    def deleteFirewallRule(self, id):
        '''
        Deletes a firewall rule
        '''

        return self.request("deleteFirewallRule", {
            'id' : id,
        })
    
    def listFirewallRules(self, account = "", domainId = "", forDisplay = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", networkId = "", page = "", pageSize = "", projectId = "", tags = ""):
        '''
        Lists all firewall rules for an IP address.
        '''

        return self.request("listFirewallRules", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
        })
    
    def updateFirewallRule(self, id, customId = "", forDisplay = ""):
        '''
        Updates firewall rule
        '''

        return self.request("updateFirewallRule", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def createEgressFirewallRule(self, networkId, protocol, cidrList = "", endPort = "", forDisplay = "", icmpCode = "", icmpType = "", startPort = "", type = ""):
        '''
        Creates a egress firewall rule for a given network
        '''

        return self.request("createEgressFirewallRule", {
            'networkid' : networkId,
            'protocol' : protocol,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'fordisplay' : forDisplay,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'startport' : startPort,
            'type' : type,
        })
    
    def deleteEgressFirewallRule(self, id):
        '''
        Deletes an ggress firewall rule
        '''

        return self.request("deleteEgressFirewallRule", {
            'id' : id,
        })
    
    def listEgressFirewallRules(self, account = "", domainId = "", forDisplay = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", networkId = "", page = "", pageSize = "", projectId = "", tags = ""):
        '''
        Lists all egress firewall rules for network id.
        '''

        return self.request("listEgressFirewallRules", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
        })
    
    def updateEgressFirewallRule(self, id, customId = "", forDisplay = ""):
        '''
        Updates egress firewall rule
        '''

        return self.request("updateEgressFirewallRule", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def createVPC(self, cidr, displayText, name, vpcOfferingId, zoneId, account = "", domainId = "", forDisplay = "", networkDomain = "", projectId = "", start = ""):
        '''
        Creates a VPC
        '''

        return self.request("createVPC", {
            'cidr' : cidr,
            'displaytext' : displayText,
            'name' : name,
            'vpcofferingid' : vpcOfferingId,
            'zoneid' : zoneId,
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'networkdomain' : networkDomain,
            'projectid' : projectId,
            'start' : start,
        })
    
    def listVPCs(self, account = "", cidr = "", displayText = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", restartRequired = "", state = "", supportedServices = "", tags = "", vpcOfferingId = "", zoneId = ""):
        '''
        Lists VPCs
        '''

        return self.request("listVPCs", {
            'account' : account,
            'cidr' : cidr,
            'displaytext' : displayText,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'restartrequired' : restartRequired,
            'state' : state,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'vpcofferingid' : vpcOfferingId,
            'zoneid' : zoneId,
        })
    
    def deleteVPC(self, id):
        '''
        Deletes a VPC
        '''

        return self.request("deleteVPC", {
            'id' : id,
        })
    
    def updateVPC(self, id, customId = "", displayText = "", forDisplay = "", name = ""):
        '''
        Updates a VPC
        '''

        return self.request("updateVPC", {
            'id' : id,
            'customid' : customId,
            'displaytext' : displayText,
            'fordisplay' : forDisplay,
            'name' : name,
        })
    
    def restartVPC(self, id):
        '''
        Restarts a VPC
        '''

        return self.request("restartVPC", {
            'id' : id,
        })
    
    def listVPCOfferings(self, displayText = "", id = "", isDefault = "", keyword = "", name = "", page = "", pageSize = "", state = "", supportedServices = ""):
        '''
        Lists VPC offerings
        '''

        return self.request("listVPCOfferings", {
            'displaytext' : displayText,
            'id' : id,
            'isdefault' : isDefault,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'supportedservices' : supportedServices,
        })
    
    def listPrivateGateways(self, account = "", domainId = "", id = "", ipAddress = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", state = "", vlan = "", vpcId = ""):
        '''
        List private gateways
        '''

        return self.request("listPrivateGateways", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddress' : ipAddress,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'state' : state,
            'vlan' : vlan,
            'vpcid' : vpcId,
        })
    
    def createStaticRoute(self, cidr, gatewayId):
        '''
        Creates a static route
        '''

        return self.request("createStaticRoute", {
            'cidr' : cidr,
            'gatewayid' : gatewayId,
        })
    
    def deleteStaticRoute(self, id):
        '''
        Deletes a static route
        '''

        return self.request("deleteStaticRoute", {
            'id' : id,
        })
    
    def listStaticRoutes(self, account = "", domainId = "", gatewayId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", tags = "", vpcId = ""):
        '''
        Lists all static routes
        '''

        return self.request("listStaticRoutes", {
            'account' : account,
            'domainid' : domainId,
            'gatewayid' : gatewayId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'tags' : tags,
            'vpcid' : vpcId,
        })
    
    def attachIso(self, id, virtualMachineId):
        '''
        Attaches an ISO to a virtual machine.
        '''

        return self.request("attachIso", {
            'id' : id,
            'virtualmachineid' : virtualMachineId,
        })
    
    def detachIso(self, virtualMachineId):
        '''
        Detaches any ISO file (if any) currently attached to a virtual machine.
        '''

        return self.request("detachIso", {
            'virtualmachineid' : virtualMachineId,
        })
    
    def listIsos(self, account = "", bootable = "", domainId = "", hypervisor = "", id = "", isoFilter = "", isPublic = "", isReady = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", showRemoved = "", tags = "", zoneId = ""):
        '''
        Lists all available ISO files.
        '''

        return self.request("listIsos", {
            'account' : account,
            'bootable' : bootable,
            'domainid' : domainId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isofilter' : isoFilter,
            'ispublic' : isPublic,
            'isready' : isReady,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'showremoved' : showRemoved,
            'tags' : tags,
            'zoneid' : zoneId,
        })
    
    def registerIso(self, displayText, name, url, zoneId, account = "", bootable = "", checksum = "", domainId = "", imageStoreUuid = "", isDynamicallyScalable = "", isExtractable = "", isFeatured = "", isPublic = "", osTypeId = "", projectId = ""):
        '''
        Registers an existing ISO into the CloudStack Cloud.
        '''

        return self.request("registerIso", {
            'displaytext' : displayText,
            'name' : name,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'bootable' : bootable,
            'checksum' : checksum,
            'domainid' : domainId,
            'imagestoreuuid' : imageStoreUuid,
            'isdynamicallyscalable' : isDynamicallyScalable,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'ostypeid' : osTypeId,
            'projectid' : projectId,
        })
    
    def updateIso(self, id, bootable = "", displayText = "", format = "", isDynamicallyScalable = "", isRouting = "", name = "", osTypeId = "", passwordEnabled = "", sortKey = ""):
        '''
        Updates an ISO file.
        '''

        return self.request("updateIso", {
            'id' : id,
            'bootable' : bootable,
            'displaytext' : displayText,
            'format' : format,
            'isdynamicallyscalable' : isDynamicallyScalable,
            'isrouting' : isRouting,
            'name' : name,
            'ostypeid' : osTypeId,
            'passwordenabled' : passwordEnabled,
            'sortkey' : sortKey,
        })
    
    def deleteIso(self, id, zoneId = ""):
        '''
        Deletes an ISO file.
        '''

        return self.request("deleteIso", {
            'id' : id,
            'zoneid' : zoneId,
        })
    
    def copyIso(self, id, destZoneId, sourceZoneId = ""):
        '''
        Copies an iso from one zone to another.
        '''

        return self.request("copyIso", {
            'id' : id,
            'destzoneid' : destZoneId,
            'sourcezoneid' : sourceZoneId,
        })
    
    def updateIsoPermissions(self, id, accounts = "", isExtractable = "", isFeatured = "", isPublic = "", op = "", projectids = ""):
        '''
        Updates iso permissions
        '''

        return self.request("updateIsoPermissions", {
            'id' : id,
            'accounts' : accounts,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'op' : op,
            'projectids' : projectids,
        })
    
    def listIsoPermissions(self, id):
        '''
        List iso visibility and all accounts that have permissions to view this iso.
        '''

        return self.request("listIsoPermissions", {
            'id' : id,
        })
    
    def extractIso(self, id, mode, url = "", zoneId = ""):
        '''
        Extracts an ISO
        '''

        return self.request("extractIso", {
            'id' : id,
            'mode' : mode,
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def createAccount(self, accountType, email, firstName, lastname, password, userName, account = "", accountDetails = "", accountId = "", domainId = "", networkDomain = "", timezone = "", userId = ""):
        '''
        Creates an account
        '''

        return self.request("createAccount", {
            'accounttype' : accountType,
            'email' : email,
            'firstname' : firstName,
            'lastname' : lastname,
            'password' : password,
            'username' : userName,
            'account' : account,
            'accountdetails' : accountDetails,
            'accountid' : accountId,
            'domainid' : domainId,
            'networkdomain' : networkDomain,
            'timezone' : timezone,
            'userid' : userId,
        })
    
    def deleteAccount(self, id):
        '''
        Deletes a account, and all users associated with this account
        '''

        return self.request("deleteAccount", {
            'id' : id,
        })
    
    def updateAccount(self, newName, account = "", accountDetails = "", domainId = "", id = "", networkDomain = ""):
        '''
        Updates account information for the authenticated user
        '''

        return self.request("updateAccount", {
            'newname' : newName,
            'account' : account,
            'accountdetails' : accountDetails,
            'domainid' : domainId,
            'id' : id,
            'networkdomain' : networkDomain,
        })
    
    def disableAccount(self, lock, account = "", domainId = "", id = ""):
        '''
        Disables an account
        '''

        return self.request("disableAccount", {
            'lock' : lock,
            'account' : account,
            'domainid' : domainId,
            'id' : id,
        })
    
    def enableAccount(self, account = "", domainId = "", id = ""):
        '''
        Enables an account
        '''

        return self.request("enableAccount", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
        })
    
    def lockAccount(self, account, domainId):
        '''
        Locks an account
        '''

        return self.request("lockAccount", {
            'account' : account,
            'domainid' : domainId,
        })
    
    def listAccounts(self, accountType = "", domainId = "", id = "", isCleanUpRequired = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", state = ""):
        '''
        Lists accounts and provides detailed account information for listed accounts
        '''

        return self.request("listAccounts", {
            'accounttype' : accountType,
            'domainid' : domainId,
            'id' : id,
            'iscleanuprequired' : isCleanUpRequired,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
        })
    
    def addAccountToProject(self, projectId, account = "", email = ""):
        '''
        Adds acoount to a project
        '''

        return self.request("addAccountToProject", {
            'projectid' : projectId,
            'account' : account,
            'email' : email,
        })
    
    def deleteAccountFromProject(self, account, projectId):
        '''
        Deletes account from the project
        '''

        return self.request("deleteAccountFromProject", {
            'account' : account,
            'projectid' : projectId,
        })
    
    def listProjectAccounts(self, projectId, account = "", keyword = "", page = "", pageSize = "", role = ""):
        '''
        Lists project's accounts
        '''

        return self.request("listProjectAccounts", {
            'projectid' : projectId,
            'account' : account,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'role' : role,
        })
    
    def attachVolume(self, id, virtualMachineId, deviceId = ""):
        '''
        Attaches a disk volume to a virtual machine.
        '''

        return self.request("attachVolume", {
            'id' : id,
            'virtualmachineid' : virtualMachineId,
            'deviceid' : deviceId,
        })
    
    def uploadVolume(self, format, name, url, zoneId, account = "", checksum = "", diskOfferingId = "", domainId = "", imageStoreUuid = "", projectId = ""):
        '''
        Uploads a data disk.
        '''

        return self.request("uploadVolume", {
            'format' : format,
            'name' : name,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'checksum' : checksum,
            'diskofferingid' : diskOfferingId,
            'domainid' : domainId,
            'imagestoreuuid' : imageStoreUuid,
            'projectid' : projectId,
        })
    
    def detachVolume(self, deviceId = "", id = "", virtualMachineId = ""):
        '''
        Detaches a disk volume from a virtual machine.
        '''

        return self.request("detachVolume", {
            'deviceid' : deviceId,
            'id' : id,
            'virtualmachineid' : virtualMachineId,
        })
    
    def createVolume(self, name, account = "", customId = "", diskOfferingId = "", displayVolume = "", domainId = "", maxIops = "", minIops = "", projectId = "", size = "", snapshotId = "", virtualMachineId = "", zoneId = ""):
        '''
        Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it.
        '''

        return self.request("createVolume", {
            'name' : name,
            'account' : account,
            'customid' : customId,
            'diskofferingid' : diskOfferingId,
            'displayvolume' : displayVolume,
            'domainid' : domainId,
            'maxiops' : maxIops,
            'miniops' : minIops,
            'projectid' : projectId,
            'size' : size,
            'snapshotid' : snapshotId,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def deleteVolume(self, id):
        '''
        Deletes a detached disk volume.
        '''

        return self.request("deleteVolume", {
            'id' : id,
        })
    
    def listVolumes(self, account = "", diskOfferingId = "", displayVolume = "", domainId = "", hostId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", podId = "", projectId = "", storageId = "", tags = "", type = "", virtualMachineId = "", zoneId = ""):
        '''
        Lists all volumes.
        '''

        return self.request("listVolumes", {
            'account' : account,
            'diskofferingid' : diskOfferingId,
            'displayvolume' : displayVolume,
            'domainid' : domainId,
            'hostid' : hostId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'storageid' : storageId,
            'tags' : tags,
            'type' : type,
            'virtualmachineid' : virtualMachineId,
            'zoneid' : zoneId,
        })
    
    def extractVolume(self, id, mode, zoneId, url = ""):
        '''
        Extracts volume
        '''

        return self.request("extractVolume", {
            'id' : id,
            'mode' : mode,
            'zoneid' : zoneId,
            'url' : url,
        })
    
    def migrateVolume(self, storageId, volumeId, liveMigrate = ""):
        '''
        Migrate volume
        '''

        return self.request("migrateVolume", {
            'storageid' : storageId,
            'volumeid' : volumeId,
            'livemigrate' : liveMigrate,
        })
    
    def resizeVolume(self, id, diskOfferingId = "", shrinkOk = "", size = ""):
        '''
        Resizes a volume
        '''

        return self.request("resizeVolume", {
            'id' : id,
            'diskofferingid' : diskOfferingId,
            'shrinkok' : shrinkOk,
            'size' : size,
        })
    
    def createUser(self, account, email, firstName, lastname, password, userName, domainId = "", timezone = "", userId = ""):
        '''
        Creates a user for an account that already exists
        '''

        return self.request("createUser", {
            'account' : account,
            'email' : email,
            'firstname' : firstName,
            'lastname' : lastname,
            'password' : password,
            'username' : userName,
            'domainid' : domainId,
            'timezone' : timezone,
            'userid' : userId,
        })
    
    def deleteUser(self, id):
        '''
        Deletes a user for an account
        '''

        return self.request("deleteUser", {
            'id' : id,
        })
    
    def updateUser(self, id, email = "", firstName = "", lastname = "", password = "", timezone = "", userApiKey = "", userName = "", userSecretKey = ""):
        '''
        Updates a user account
        '''

        return self.request("updateUser", {
            'id' : id,
            'email' : email,
            'firstname' : firstName,
            'lastname' : lastname,
            'password' : password,
            'timezone' : timezone,
            'userapikey' : userApiKey,
            'username' : userName,
            'usersecretkey' : userSecretKey,
        })
    
    def listUsers(self, account = "", accountType = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", state = "", userName = ""):
        '''
        Lists user accounts
        '''

        return self.request("listUsers", {
            'account' : account,
            'accounttype' : accountType,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'username' : userName,
        })
    
    def lockUser(self, id):
        '''
        Locks a user account
        '''

        return self.request("lockUser", {
            'id' : id,
        })
    
    def disableUser(self, id):
        '''
        Disables a user account
        '''

        return self.request("disableUser", {
            'id' : id,
        })
    
    def enableUser(self, id):
        '''
        Enables a user account
        '''

        return self.request("enableUser", {
            'id' : id,
        })
    
    def getVirtualMachineUserData(self, virtualMachineId):
        '''
        Returns user data associated with the VM
        '''

        return self.request("getVirtualMachineUserData", {
            'virtualmachineid' : virtualMachineId,
        })
    
    def registerUserKeys(self, id):
        '''
        This command allows a user to register for the developer API, returning a secret key and an API key. This request is made through the integration API port, so it is a privileged command and must be made on behalf of a user. It is up to the implementer just how the username and password are entered, and then how that translates to an integration API request. Both secret key and API key should be returned to the user
        '''

        return self.request("registerUserKeys", {
            'id' : id,
        })
    
    def createTemplate(self, displayText, name, osTypeId, bits = "", details = "", isDynamicallyScalable = "", isFeatured = "", isPublic = "", passwordEnabled = "", requireShvm = "", snapshotId = "", templateTag = "", url = "", virtualMachineId = "", volumeId = ""):
        '''
        Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it.
        '''

        return self.request("createTemplate", {
            'displaytext' : displayText,
            'name' : name,
            'ostypeid' : osTypeId,
            'bits' : bits,
            'details' : details,
            'isdynamicallyscalable' : isDynamicallyScalable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'passwordenabled' : passwordEnabled,
            'requireshvm' : requireShvm,
            'snapshotid' : snapshotId,
            'templatetag' : templateTag,
            'url' : url,
            'virtualmachineid' : virtualMachineId,
            'volumeid' : volumeId,
        })
    
    def registerTemplate(self, displayText, format, hypervisor, name, osTypeId, url, zoneId, account = "", bits = "", checksum = "", details = "", domainId = "", isDynamicallyScalable = "", isExtractable = "", isFeatured = "", isPublic = "", isRouting = "", passwordEnabled = "", projectId = "", requireShvm = "", sshkeyEnabled = "", templateTag = ""):
        '''
        Registers an existing template into the CloudStack cloud.
        '''

        return self.request("registerTemplate", {
            'displaytext' : displayText,
            'format' : format,
            'hypervisor' : hypervisor,
            'name' : name,
            'ostypeid' : osTypeId,
            'url' : url,
            'zoneid' : zoneId,
            'account' : account,
            'bits' : bits,
            'checksum' : checksum,
            'details' : details,
            'domainid' : domainId,
            'isdynamicallyscalable' : isDynamicallyScalable,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'isrouting' : isRouting,
            'passwordenabled' : passwordEnabled,
            'projectid' : projectId,
            'requireshvm' : requireShvm,
            'sshkeyenabled' : sshkeyEnabled,
            'templatetag' : templateTag,
        })
    
    def updateTemplate(self, id, bootable = "", displayText = "", format = "", isDynamicallyScalable = "", isRouting = "", name = "", osTypeId = "", passwordEnabled = "", sortKey = ""):
        '''
        Updates attributes of a template.
        '''

        return self.request("updateTemplate", {
            'id' : id,
            'bootable' : bootable,
            'displaytext' : displayText,
            'format' : format,
            'isdynamicallyscalable' : isDynamicallyScalable,
            'isrouting' : isRouting,
            'name' : name,
            'ostypeid' : osTypeId,
            'passwordenabled' : passwordEnabled,
            'sortkey' : sortKey,
        })
    
    def copyTemplate(self, id, destZoneId, sourceZoneId = ""):
        '''
        Copies a template from one zone to another.
        '''

        return self.request("copyTemplate", {
            'id' : id,
            'destzoneid' : destZoneId,
            'sourcezoneid' : sourceZoneId,
        })
    
    def deleteTemplate(self, id, zoneId = ""):
        '''
        Deletes a template from the system. All virtual machines using the deleted template will not be affected.
        '''

        return self.request("deleteTemplate", {
            'id' : id,
            'zoneid' : zoneId,
        })
    
    def listTemplates(self, templateFilter, account = "", domainId = "", hypervisor = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = "", showRemoved = "", tags = "", zoneId = ""):
        '''
        List all public, private, and privileged templates.
        '''

        return self.request("listTemplates", {
            'templatefilter' : templateFilter,
            'account' : account,
            'domainid' : domainId,
            'hypervisor' : hypervisor,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'showremoved' : showRemoved,
            'tags' : tags,
            'zoneid' : zoneId,
        })
    
    def updateTemplatePermissions(self, id, accounts = "", isExtractable = "", isFeatured = "", isPublic = "", op = "", projectids = ""):
        '''
        Updates a template visibility permissions. A public template is visible to all accounts within the same domain. A private template is visible only to the owner of the template. A priviledged template is a private template with account permissions added. Only accounts specified under the template permissions are visible to them.
        '''

        return self.request("updateTemplatePermissions", {
            'id' : id,
            'accounts' : accounts,
            'isextractable' : isExtractable,
            'isfeatured' : isFeatured,
            'ispublic' : isPublic,
            'op' : op,
            'projectids' : projectids,
        })
    
    def listTemplatePermissions(self, id):
        '''
        List template visibility and all accounts that have permissions to view this template.
        '''

        return self.request("listTemplatePermissions", {
            'id' : id,
        })
    
    def extractTemplate(self, id, mode, url = "", zoneId = ""):
        '''
        Extracts a template
        '''

        return self.request("extractTemplate", {
            'id' : id,
            'mode' : mode,
            'url' : url,
            'zoneid' : zoneId,
        })
    
    def startRouter(self, id):
        '''
        Starts a router.
        '''

        return self.request("startRouter", {
            'id' : id,
        })
    
    def rebootRouter(self, id):
        '''
        Starts a router.
        '''

        return self.request("rebootRouter", {
            'id' : id,
        })
    
    def stopRouter(self, id, forced = ""):
        '''
        Stops a router.
        '''

        return self.request("stopRouter", {
            'id' : id,
            'forced' : forced,
        })
    
    def destroyRouter(self, id):
        '''
        Destroys a router.
        '''

        return self.request("destroyRouter", {
            'id' : id,
        })
    
    def changeServiceForRouter(self, id, serviceOfferingId):
        '''
        Upgrades domain router to a new service offering
        '''

        return self.request("changeServiceForRouter", {
            'id' : id,
            'serviceofferingid' : serviceOfferingId,
        })
    
    def listRouters(self, account = "", clusterId = "", domainId = "", forVpc = "", hostId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", podId = "", projectId = "", state = "", version = "", vpcId = "", zoneId = ""):
        '''
        List routers.
        '''

        return self.request("listRouters", {
            'account' : account,
            'clusterid' : clusterId,
            'domainid' : domainId,
            'forvpc' : forVpc,
            'hostid' : hostId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'podid' : podId,
            'projectid' : projectId,
            'state' : state,
            'version' : version,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def listVirtualRouterElements(self, enabled = "", id = "", keyword = "", nspId = "", page = "", pageSize = ""):
        '''
        Lists all available virtual router elements.
        '''

        return self.request("listVirtualRouterElements", {
            'enabled' : enabled,
            'id' : id,
            'keyword' : keyword,
            'nspid' : nspId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def configureVirtualRouterElement(self, id, enabled):
        '''
        Configures a virtual router element.
        '''

        return self.request("configureVirtualRouterElement", {
            'id' : id,
            'enabled' : enabled,
        })
    
    def createVirtualRouterElement(self, nspId, providerType = ""):
        '''
        Create a virtual router element.
        '''

        return self.request("createVirtualRouterElement", {
            'nspid' : nspId,
            'providertype' : providerType,
        })
    
    def createProject(self, displayText, name, account = "", domainId = ""):
        '''
        Creates a project
        '''

        return self.request("createProject", {
            'displaytext' : displayText,
            'name' : name,
            'account' : account,
            'domainid' : domainId,
        })
    
    def deleteProject(self, id):
        '''
        Deletes a project
        '''

        return self.request("deleteProject", {
            'id' : id,
        })
    
    def updateProject(self, id, account = "", displayText = ""):
        '''
        Updates a project
        '''

        return self.request("updateProject", {
            'id' : id,
            'account' : account,
            'displaytext' : displayText,
        })
    
    def activateProject(self, id):
        '''
        Activates a project
        '''

        return self.request("activateProject", {
            'id' : id,
        })
    
    def suspendProject(self, id):
        '''
        Suspends a project
        '''

        return self.request("suspendProject", {
            'id' : id,
        })
    
    def listProjects(self, account = "", displayText = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", state = "", tags = ""):
        '''
        Lists projects and provides detailed information for listed projects
        '''

        return self.request("listProjects", {
            'account' : account,
            'displaytext' : displayText,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'state' : state,
            'tags' : tags,
        })
    
    def listProjectInvitations(self, account = "", activeOnly = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", state = ""):
        '''
        Lists projects and provides detailed information for listed projects
        '''

        return self.request("listProjectInvitations", {
            'account' : account,
            'activeonly' : activeOnly,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'state' : state,
        })
    
    def updateProjectInvitation(self, projectId, accept = "", account = "", token = ""):
        '''
        Accepts or declines project invitation
        '''

        return self.request("updateProjectInvitation", {
            'projectid' : projectId,
            'accept' : accept,
            'account' : account,
            'token' : token,
        })
    
    def deleteProjectInvitation(self, id):
        '''
        Accepts or declines project invitation
        '''

        return self.request("deleteProjectInvitation", {
            'id' : id,
        })
    
    def createNetworkACL(self, protocol, aclId = "", action = "", cidrList = "", endPort = "", forDisplay = "", icmpCode = "", icmpType = "", networkId = "", number = "", startPort = "", trafficType = ""):
        '''
        Creates a ACL rule in the given network (the network has to belong to VPC)
        '''

        return self.request("createNetworkACL", {
            'protocol' : protocol,
            'aclid' : aclId,
            'action' : action,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'fordisplay' : forDisplay,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'networkid' : networkId,
            'number' : number,
            'startport' : startPort,
            'traffictype' : trafficType,
        })
    
    def updateNetworkACLItem(self, id, action = "", cidrList = "", customId = "", endPort = "", forDisplay = "", icmpCode = "", icmpType = "", number = "", protocol = "", startPort = "", trafficType = ""):
        '''
        Updates ACL Item with specified Id
        '''

        return self.request("updateNetworkACLItem", {
            'id' : id,
            'action' : action,
            'cidrlist' : cidrList,
            'customid' : customId,
            'endport' : endPort,
            'fordisplay' : forDisplay,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'number' : number,
            'protocol' : protocol,
            'startport' : startPort,
            'traffictype' : trafficType,
        })
    
    def deleteNetworkACL(self, id):
        '''
        Deletes a Network ACL
        '''

        return self.request("deleteNetworkACL", {
            'id' : id,
        })
    
    def listNetworkACLs(self, account = "", aclId = "", action = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", networkId = "", page = "", pageSize = "", projectId = "", protocol = "", tags = "", trafficType = ""):
        '''
        Lists all network ACL items
        '''

        return self.request("listNetworkACLs", {
            'account' : account,
            'aclid' : aclId,
            'action' : action,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'protocol' : protocol,
            'tags' : tags,
            'traffictype' : trafficType,
        })
    
    def createNetworkACLList(self, name, vpcId, description = "", forDisplay = ""):
        '''
        Creates a Network ACL for the given VPC
        '''

        return self.request("createNetworkACLList", {
            'name' : name,
            'vpcid' : vpcId,
            'description' : description,
            'fordisplay' : forDisplay,
        })
    
    def deleteNetworkACLList(self, id):
        '''
        Deletes a Network ACL
        '''

        return self.request("deleteNetworkACLList", {
            'id' : id,
        })
    
    def replaceNetworkACLList(self, aclId, gatewayId = "", networkId = ""):
        '''
        Replaces ACL associated with a Network or private gateway
        '''

        return self.request("replaceNetworkACLList", {
            'aclid' : aclId,
            'gatewayid' : gatewayId,
            'networkid' : networkId,
        })
    
    def listNetworkACLLists(self, account = "", domainId = "", forDisplay = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", networkId = "", page = "", pageSize = "", projectId = "", vpcId = ""):
        '''
        Lists all network ACLs
        '''

        return self.request("listNetworkACLLists", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'vpcid' : vpcId,
        })
    
    def updateNetworkACLList(self, id, customId = "", forDisplay = ""):
        '''
        Updates Network ACL list
        '''

        return self.request("updateNetworkACLList", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def createSecurityGroup(self, name, account = "", description = "", domainId = "", projectId = ""):
        '''
        Creates a security group
        '''

        return self.request("createSecurityGroup", {
            'name' : name,
            'account' : account,
            'description' : description,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteSecurityGroup(self, account = "", domainId = "", id = "", name = "", projectId = ""):
        '''
        Deletes security group
        '''

        return self.request("deleteSecurityGroup", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'name' : name,
            'projectid' : projectId,
        })
    
    def authorizeSecurityGroupIngress(self, account = "", cidrList = "", domainId = "", endPort = "", icmpCode = "", icmpType = "", projectId = "", protocol = "", securityGroupId = "", securityGroupName = "", startPort = "", userSecurityGroupList = ""):
        '''
        Authorizes a particular ingress rule for this security group
        '''

        return self.request("authorizeSecurityGroupIngress", {
            'account' : account,
            'cidrlist' : cidrList,
            'domainid' : domainId,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'projectid' : projectId,
            'protocol' : protocol,
            'securitygroupid' : securityGroupId,
            'securitygroupname' : securityGroupName,
            'startport' : startPort,
            'usersecuritygrouplist' : userSecurityGroupList,
        })
    
    def revokeSecurityGroupIngress(self, id):
        '''
        Deletes a particular ingress rule from this security group
        '''

        return self.request("revokeSecurityGroupIngress", {
            'id' : id,
        })
    
    def authorizeSecurityGroupEgress(self, account = "", cidrList = "", domainId = "", endPort = "", icmpCode = "", icmpType = "", projectId = "", protocol = "", securityGroupId = "", securityGroupName = "", startPort = "", userSecurityGroupList = ""):
        '''
        Authorizes a particular egress rule for this security group
        '''

        return self.request("authorizeSecurityGroupEgress", {
            'account' : account,
            'cidrlist' : cidrList,
            'domainid' : domainId,
            'endport' : endPort,
            'icmpcode' : icmpCode,
            'icmptype' : icmpType,
            'projectid' : projectId,
            'protocol' : protocol,
            'securitygroupid' : securityGroupId,
            'securitygroupname' : securityGroupName,
            'startport' : startPort,
            'usersecuritygrouplist' : userSecurityGroupList,
        })
    
    def revokeSecurityGroupEgress(self, id):
        '''
        Deletes a particular egress rule from this security group
        '''

        return self.request("revokeSecurityGroupEgress", {
            'id' : id,
        })
    
    def listSecurityGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", securityGroupName = "", tags = "", virtualMachineId = ""):
        '''
        Lists security groups
        '''

        return self.request("listSecurityGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'securitygroupname' : securityGroupName,
            'tags' : tags,
            'virtualmachineid' : virtualMachineId,
        })
    
    def resetSSHKeyForVirtualMachine(self, id, keyPair, account = "", domainId = "", projectId = ""):
        '''
        Resets the SSH Key for virtual machine. The virtual machine must be in a "Stopped" state. [async]
        '''

        return self.request("resetSSHKeyForVirtualMachine", {
            'id' : id,
            'keypair' : keyPair,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def registerSSHKeyPair(self, name, publicKey, account = "", domainId = "", projectId = ""):
        '''
        Register a public key in a keypair under a certain name
        '''

        return self.request("registerSSHKeyPair", {
            'name' : name,
            'publickey' : publicKey,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def createSSHKeyPair(self, name, account = "", domainId = "", projectId = ""):
        '''
        Create a new keypair and returns the private key
        '''

        return self.request("createSSHKeyPair", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteSSHKeyPair(self, name, account = "", domainId = "", projectId = ""):
        '''
        Deletes a keypair by name
        '''

        return self.request("deleteSSHKeyPair", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def listSSHKeyPairs(self, account = "", domainId = "", fingerprint = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = ""):
        '''
        List registered keypairs
        '''

        return self.request("listSSHKeyPairs", {
            'account' : account,
            'domainid' : domainId,
            'fingerprint' : fingerprint,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def createNetwork(self, displayText, name, networkOfferingId, zoneId, account = "", aclId = "", aclType = "", displayNetwork = "", domainId = "", endIp = "", endIpV6 = "", gateway = "", ip6Cidr = "", ip6Gateway = "", isolatedPvlan = "", netmask = "", networkDomain = "", physicalNetworkId = "", projectId = "", startIp = "", startIpV6 = "", subDomainAccess = "", vlan = "", vpcId = ""):
        '''
        Creates a network
        '''

        return self.request("createNetwork", {
            'displaytext' : displayText,
            'name' : name,
            'networkofferingid' : networkOfferingId,
            'zoneid' : zoneId,
            'account' : account,
            'aclid' : aclId,
            'acltype' : aclType,
            'displaynetwork' : displayNetwork,
            'domainid' : domainId,
            'endip' : endIp,
            'endipv6' : endIpV6,
            'gateway' : gateway,
            'ip6cidr' : ip6Cidr,
            'ip6gateway' : ip6Gateway,
            'isolatedpvlan' : isolatedPvlan,
            'netmask' : netmask,
            'networkdomain' : networkDomain,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'startip' : startIp,
            'startipv6' : startIpV6,
            'subdomainaccess' : subDomainAccess,
            'vlan' : vlan,
            'vpcid' : vpcId,
        })
    
    def deleteNetwork(self, id, forced = ""):
        '''
        Deletes a network
        '''

        return self.request("deleteNetwork", {
            'id' : id,
            'forced' : forced,
        })
    
    def listNetworks(self, account = "", aclType = "", canUseForDeploy = "", displayNetwork = "", domainId = "", forVpc = "", id = "", isRecursive = "", isSystem = "", keyword = "", listAll = "", page = "", pageSize = "", physicalNetworkId = "", projectId = "", restartRequired = "", specifyIpRanges = "", supportedServices = "", tags = "", trafficType = "", type = "", vpcId = "", zoneId = ""):
        '''
        Lists all available networks.
        '''

        return self.request("listNetworks", {
            'account' : account,
            'acltype' : aclType,
            'canusefordeploy' : canUseForDeploy,
            'displaynetwork' : displayNetwork,
            'domainid' : domainId,
            'forvpc' : forVpc,
            'id' : id,
            'isrecursive' : isRecursive,
            'issystem' : isSystem,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'restartrequired' : restartRequired,
            'specifyipranges' : specifyIpRanges,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'traffictype' : trafficType,
            'type' : type,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def restartNetwork(self, id, cleanup = ""):
        '''
        Restarts the network; includes 1) restarting network elements - virtual routers, dhcp servers 2) reapplying all public ips 3) reapplying loadBalancing/portForwarding rules
        '''

        return self.request("restartNetwork", {
            'id' : id,
            'cleanup' : cleanup,
        })
    
    def updateNetwork(self, id, changeCidr = "", customId = "", displayNetwork = "", displayText = "", guestVmCidr = "", name = "", networkDomain = "", networkOfferingId = ""):
        '''
        Updates a network
        '''

        return self.request("updateNetwork", {
            'id' : id,
            'changecidr' : changeCidr,
            'customid' : customId,
            'displaynetwork' : displayNetwork,
            'displaytext' : displayText,
            'guestvmcidr' : guestVmCidr,
            'name' : name,
            'networkdomain' : networkDomain,
            'networkofferingid' : networkOfferingId,
        })
    
    def enableStaticNat(self, ipAddressId, virtualMachineId, networkId = "", vmGuestIp = ""):
        '''
        Enables static nat for given ip address
        '''

        return self.request("enableStaticNat", {
            'ipaddressid' : ipAddressId,
            'virtualmachineid' : virtualMachineId,
            'networkid' : networkId,
            'vmguestip' : vmGuestIp,
        })
    
    def createIpForwardingRule(self, ipAddressId, protocol, startPort, cidrList = "", endPort = "", openFirewall = ""):
        '''
        Creates an ip forwarding rule
        '''

        return self.request("createIpForwardingRule", {
            'ipaddressid' : ipAddressId,
            'protocol' : protocol,
            'startport' : startPort,
            'cidrlist' : cidrList,
            'endport' : endPort,
            'openfirewall' : openFirewall,
        })
    
    def deleteIpForwardingRule(self, id):
        '''
        Deletes an ip forwarding rule
        '''

        return self.request("deleteIpForwardingRule", {
            'id' : id,
        })
    
    def listIpForwardingRules(self, account = "", domainId = "", id = "", ipAddressId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", virtualMachineId = ""):
        '''
        List the ip forwarding rules
        '''

        return self.request("listIpForwardingRules", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'ipaddressid' : ipAddressId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'virtualmachineid' : virtualMachineId,
        })
    
    def disableStaticNat(self, ipAddressId):
        '''
        Disables static rule for given ip address
        '''

        return self.request("disableStaticNat", {
            'ipaddressid' : ipAddressId,
        })
    
    def createAffinityGroup(self, name, type, account = "", description = "", domainId = ""):
        '''
        Creates an affinity/anti-affinity group
        '''

        return self.request("createAffinityGroup", {
            'name' : name,
            'type' : type,
            'account' : account,
            'description' : description,
            'domainid' : domainId,
        })
    
    def deleteAffinityGroup(self, account = "", domainId = "", id = "", name = ""):
        '''
        Deletes affinity group
        '''

        return self.request("deleteAffinityGroup", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'name' : name,
        })
    
    def listAffinityGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", type = "", virtualMachineId = ""):
        '''
        Lists affinity groups
        '''

        return self.request("listAffinityGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'type' : type,
            'virtualmachineid' : virtualMachineId,
        })
    
    def updateVMAffinityGroup(self, id, affinityGroupIds = "", affinityGroupNames = ""):
        '''
        Updates the affinity/anti-affinity group associations of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect.
        '''

        return self.request("updateVMAffinityGroup", {
            'id' : id,
            'affinitygroupids' : affinityGroupIds,
            'affinitygroupnames' : affinityGroupNames,
        })
    
    def listAffinityGroupTypes(self, keyword = "", page = "", pageSize = ""):
        '''
        Lists affinity group types available
        '''

        return self.request("listAffinityGroupTypes", {
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def createInstanceGroup(self, name, account = "", domainId = "", projectId = ""):
        '''
        Creates a vm group
        '''

        return self.request("createInstanceGroup", {
            'name' : name,
            'account' : account,
            'domainid' : domainId,
            'projectid' : projectId,
        })
    
    def deleteInstanceGroup(self, id):
        '''
        Deletes a vm group
        '''

        return self.request("deleteInstanceGroup", {
            'id' : id,
        })
    
    def updateInstanceGroup(self, id, name = ""):
        '''
        Updates a vm group
        '''

        return self.request("updateInstanceGroup", {
            'id' : id,
            'name' : name,
        })
    
    def listInstanceGroups(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = "", projectId = ""):
        '''
        Lists vm groups
        '''

        return self.request("listInstanceGroups", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
        })
    
    def updateResourceLimit(self, resourceType, account = "", domainId = "", max = "", projectId = ""):
        '''
        Updates resource limits for an account or domain.
        '''

        return self.request("updateResourceLimit", {
            'resourcetype' : resourceType,
            'account' : account,
            'domainid' : domainId,
            'max' : max,
            'projectid' : projectId,
        })
    
    def updateResourceCount(self, domainId, account = "", projectId = "", resourceType = ""):
        '''
        Recalculate and update resource count for an account or domain.
        '''

        return self.request("updateResourceCount", {
            'domainid' : domainId,
            'account' : account,
            'projectid' : projectId,
            'resourcetype' : resourceType,
        })
    
    def listResourceLimits(self, account = "", domainId = "", id = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", resourceType = ""):
        '''
        Lists resource limits.
        '''

        return self.request("listResourceLimits", {
            'account' : account,
            'domainid' : domainId,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'resourcetype' : resourceType,
        })
    
    def getApiLimit(self, ):
        '''
        Get API limit count for the caller
        '''

        return self.request("getApiLimit", {
        })
    
    def listEvents(self, account = "", domainId = "", duration = "", endDate = "", entryTime = "", id = "", isRecursive = "", keyword = "", level = "", listAll = "", page = "", pageSize = "", projectId = "", startDate = "", type = ""):
        '''
        A command to list events.
        '''

        return self.request("listEvents", {
            'account' : account,
            'domainid' : domainId,
            'duration' : duration,
            'enddate' : endDate,
            'entrytime' : entryTime,
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'level' : level,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'startdate' : startDate,
            'type' : type,
        })
    
    def listEventTypes(self, ):
        '''
        List Event Types
        '''

        return self.request("listEventTypes", {
        })
    
    def archiveEvents(self, endDate = "", ids = "", startDate = "", type = ""):
        '''
        Archive one or more events.
        '''

        return self.request("archiveEvents", {
            'enddate' : endDate,
            'ids' : ids,
            'startdate' : startDate,
            'type' : type,
        })
    
    def deleteEvents(self, endDate = "", ids = "", startDate = "", type = ""):
        '''
        Delete one or more events.
        '''

        return self.request("deleteEvents", {
            'enddate' : endDate,
            'ids' : ids,
            'startdate' : startDate,
            'type' : type,
        })
    
    def associateIpAddress(self, account = "", domainId = "", forDisplay = "", isPortable = "", networkId = "", projectId = "", regionId = "", vpcId = "", zoneId = ""):
        '''
        Acquires and associates a public IP to an account.
        '''

        return self.request("associateIpAddress", {
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'isportable' : isPortable,
            'networkid' : networkId,
            'projectid' : projectId,
            'regionid' : regionId,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def disassociateIpAddress(self, id):
        '''
        Disassociates an ip address from the account.
        '''

        return self.request("disassociateIpAddress", {
            'id' : id,
        })
    
    def listPublicIpAddresses(self, account = "", allocatedOnly = "", associatedNetworkId = "", domainId = "", forDisplay = "", forLoadBalancing = "", forVirtualNetwork = "", id = "", ipAddress = "", isRecursive = "", isSourceNat = "", isStaticNat = "", keyword = "", listAll = "", page = "", pageSize = "", physicalNetworkId = "", projectId = "", tags = "", vlanId = "", vpcId = "", zoneId = ""):
        '''
        Lists all public ip addresses
        '''

        return self.request("listPublicIpAddresses", {
            'account' : account,
            'allocatedonly' : allocatedOnly,
            'associatednetworkid' : associatedNetworkId,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'forloadbalancing' : forLoadBalancing,
            'forvirtualnetwork' : forVirtualNetwork,
            'id' : id,
            'ipaddress' : ipAddress,
            'isrecursive' : isRecursive,
            'issourcenat' : isSourceNat,
            'isstaticnat' : isStaticNat,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'physicalnetworkid' : physicalNetworkId,
            'projectid' : projectId,
            'tags' : tags,
            'vlanid' : vlanId,
            'vpcid' : vpcId,
            'zoneid' : zoneId,
        })
    
    def updateIpAddress(self, id, customId = "", forDisplay = ""):
        '''
        Updates an ip address
        '''

        return self.request("updateIpAddress", {
            'id' : id,
            'customid' : customId,
            'fordisplay' : forDisplay,
        })
    
    def createTags(self, resourceIds, resourceType, tags, customer = ""):
        '''
        Creates resource tag(s)
        '''

        return self.request("createTags", {
            'resourceids' : resourceIds,
            'resourcetype' : resourceType,
            'tags' : tags,
            'customer' : customer,
        })
    
    def deleteTags(self, resourceIds, resourceType, tags = ""):
        '''
        Deleting resource tag(s)
        '''

        return self.request("deleteTags", {
            'resourceids' : resourceIds,
            'resourcetype' : resourceType,
            'tags' : tags,
        })
    
    def listTags(self, account = "", customer = "", domainId = "", isRecursive = "", key = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", resourceid = "", resourceType = "", value = ""):
        '''
        List resource tag(s)
        '''

        return self.request("listTags", {
            'account' : account,
            'customer' : customer,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'key' : key,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'resourceid' : resourceid,
            'resourcetype' : resourceType,
            'value' : value,
        })
    
    def addIpToNic(self, nicId, ipAddress = ""):
        '''
        Assigns secondary IP to NIC
        '''

        return self.request("addIpToNic", {
            'nicid' : nicId,
            'ipaddress' : ipAddress,
        })
    
    def removeIpFromNic(self, id):
        '''
        Removes secondary IP from the NIC.
        '''

        return self.request("removeIpFromNic", {
            'id' : id,
        })
    
    def listNics(self, virtualMachineId, forDisplay = "", keyword = "", networkId = "", nicId = "", page = "", pageSize = ""):
        '''
        list the vm nics  IP to NIC
        '''

        return self.request("listNics", {
            'virtualmachineid' : virtualMachineId,
            'fordisplay' : forDisplay,
            'keyword' : keyword,
            'networkid' : networkId,
            'nicid' : nicId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def configureInternalLoadBalancerElement(self, id, enabled):
        '''
        Configures an Internal Load Balancer element.
        '''

        return self.request("configureInternalLoadBalancerElement", {
            'id' : id,
            'enabled' : enabled,
        })
    
    def createInternalLoadBalancerElement(self, nspId):
        '''
        Create an Internal Load Balancer element.
        '''

        return self.request("createInternalLoadBalancerElement", {
            'nspid' : nspId,
        })
    
    def listInternalLoadBalancerElements(self, enabled = "", id = "", keyword = "", nspId = "", page = "", pageSize = ""):
        '''
        Lists all available Internal Load Balancer elements.
        '''

        return self.request("listInternalLoadBalancerElements", {
            'enabled' : enabled,
            'id' : id,
            'keyword' : keyword,
            'nspid' : nspId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def configureOvsElement(self, id, enabled):
        '''
        Configures an ovs element.
        '''

        return self.request("configureOvsElement", {
            'id' : id,
            'enabled' : enabled,
        })
    
    def listOvsElements(self, enabled = "", id = "", keyword = "", nspId = "", page = "", pageSize = ""):
        '''
        Lists all available ovs elements.
        '''

        return self.request("listOvsElements", {
            'enabled' : enabled,
            'id' : id,
            'keyword' : keyword,
            'nspid' : nspId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listOsTypes(self, description = "", id = "", keyword = "", osCategoryId = "", page = "", pageSize = ""):
        '''
        Lists all supported OS types for this cloud.
        '''

        return self.request("listOsTypes", {
            'description' : description,
            'id' : id,
            'keyword' : keyword,
            'oscategoryid' : osCategoryId,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listOsCategories(self, id = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists all supported OS categories for this cloud.
        '''

        return self.request("listOsCategories", {
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listDomains(self, id = "", keyword = "", level = "", listAll = "", name = "", page = "", pageSize = ""):
        '''
        Lists domains and provides detailed information for listed domains
        '''

        return self.request("listDomains", {
            'id' : id,
            'keyword' : keyword,
            'level' : level,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listDomainChildren(self, id = "", isRecursive = "", keyword = "", listAll = "", name = "", page = "", pageSize = ""):
        '''
        Lists all children domains belonging to a specified domain
        '''

        return self.request("listDomainChildren", {
            'id' : id,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listCapabilities(self, ):
        '''
        Lists capabilities
        '''

        return self.request("listCapabilities", {
        })
    
    def listLdapConfigurations(self, hostname = "", keyword = "", page = "", pageSize = "", port = ""):
        '''
        Lists all LDAP configurations
        '''

        return self.request("listLdapConfigurations", {
            'hostname' : hostname,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'port' : port,
        })
    
    def queryAsyncJobResult(self, jobId):
        '''
        Retrieves the current status of asynchronous job.
        '''

        return self.request("queryAsyncJobResult", {
            'jobid' : jobId,
        })
    
    def listAsyncJobs(self, account = "", domainId = "", isRecursive = "", keyword = "", listAll = "", page = "", pageSize = "", startDate = ""):
        '''
        Lists all pending asynchronous jobs for the account.
        '''

        return self.request("listAsyncJobs", {
            'account' : account,
            'domainid' : domainId,
            'isrecursive' : isRecursive,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'startdate' : startDate,
        })
    
    def listZones(self, available = "", domainId = "", id = "", keyword = "", name = "", networkType = "", page = "", pageSize = "", showCapacities = "", tags = ""):
        '''
        Lists zones
        '''

        return self.request("listZones", {
            'available' : available,
            'domainid' : domainId,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'networktype' : networkType,
            'page' : page,
            'pagesize' : pageSize,
            'showcapacities' : showCapacities,
            'tags' : tags,
        })
    
    def listUsageRecords(self, endDate, startDate, account = "", accountId = "", domainId = "", keyword = "", page = "", pageSize = "", projectId = "", type = ""):
        '''
        Lists usage records for accounts
        '''

        return self.request("listUsageRecords", {
            'enddate' : endDate,
            'startdate' : startDate,
            'account' : account,
            'accountid' : accountId,
            'domainid' : domainId,
            'keyword' : keyword,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'type' : type,
        })
    
    def listServiceOfferings(self, domainId = "", id = "", isSystem = "", keyword = "", name = "", page = "", pageSize = "", systemVmType = "", virtualMachineId = ""):
        '''
        Lists all available service offerings.
        '''

        return self.request("listServiceOfferings", {
            'domainid' : domainId,
            'id' : id,
            'issystem' : isSystem,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
            'systemvmtype' : systemVmType,
            'virtualmachineid' : virtualMachineId,
        })
    
    def listResourceDetails(self, resourceType, account = "", domainId = "", forDisplay = "", isRecursive = "", key = "", keyword = "", listAll = "", page = "", pageSize = "", projectId = "", resourceid = "", value = ""):
        '''
        List resource detail(s)
        '''

        return self.request("listResourceDetails", {
            'resourcetype' : resourceType,
            'account' : account,
            'domainid' : domainId,
            'fordisplay' : forDisplay,
            'isrecursive' : isRecursive,
            'key' : key,
            'keyword' : keyword,
            'listall' : listAll,
            'page' : page,
            'pagesize' : pageSize,
            'projectid' : projectId,
            'resourceid' : resourceid,
            'value' : value,
        })
    
    def listRegions(self, id = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists Regions
        '''

        return self.request("listRegions", {
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def listNetworkOfferings(self, availability = "", displayText = "", forVpc = "", guestIpType = "", id = "", isDefault = "", isTagged = "", keyword = "", name = "", networkId = "", page = "", pageSize = "", sourceNatSupported = "", specifyIpRanges = "", specifyVlan = "", state = "", supportedServices = "", tags = "", trafficType = "", zoneId = ""):
        '''
        Lists all available network offerings.
        '''

        return self.request("listNetworkOfferings", {
            'availability' : availability,
            'displaytext' : displayText,
            'forvpc' : forVpc,
            'guestiptype' : guestIpType,
            'id' : id,
            'isdefault' : isDefault,
            'istagged' : isTagged,
            'keyword' : keyword,
            'name' : name,
            'networkid' : networkId,
            'page' : page,
            'pagesize' : pageSize,
            'sourcenatsupported' : sourceNatSupported,
            'specifyipranges' : specifyIpRanges,
            'specifyvlan' : specifyVlan,
            'state' : state,
            'supportedservices' : supportedServices,
            'tags' : tags,
            'traffictype' : trafficType,
            'zoneid' : zoneId,
        })
    
    def logout(self, ):
        '''
        Logs out the user
        '''

        return self.request("logout", {
        })
    
    def login(self, userName, password, domain = "", domainId = ""):
        '''
        Logs a user into the CloudStack. A successful login attempt will generate a JSESSIONID cookie value that can be passed in subsequent Query command calls until the "logout" command has been issued or the session has expired.
        '''

        return self.request("login", {
            'username' : userName,
            'password' : password,
            'domain' : domain,
            'domainId' : domainId,
        })
    
    def listHypervisors(self, zoneId = ""):
        '''
        List hypervisors
        '''

        return self.request("listHypervisors", {
            'zoneid' : zoneId,
        })
    
    def listDiskOfferings(self, domainId = "", id = "", keyword = "", name = "", page = "", pageSize = ""):
        '''
        Lists all available disk offerings.
        '''

        return self.request("listDiskOfferings", {
            'domainid' : domainId,
            'id' : id,
            'keyword' : keyword,
            'name' : name,
            'page' : page,
            'pagesize' : pageSize,
        })
    
    def getCloudIdentifier(self, userId):
        '''
        Retrieves a cloud identifier.
        '''

        return self.request("getCloudIdentifier", {
            'userid' : userId,
        })
    
    def listApis(self, name = ""):
        '''
        lists all available apis on the server, provided by the Api Discovery plugin
        '''

        return self.request("listApis", {
            'name' : name,
        })
    
