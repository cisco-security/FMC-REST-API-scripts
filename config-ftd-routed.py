
#!/usr/bin/env python
################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License"); you may   #
#    not use this file except in compliance with the License. You may obtain   #
#    a copy of the License at                                                  #
#                                                                              #
#         http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################
import sys
sys.path.insert(0, '/home/user/manual-devpkg/ftd-fi')

from device_script import serviceAudit

#Parameters

tenant_name = 'cl'
#tenant_name = raw_input("Enter Tenant name: ")

l47_dev_name = 'ftdvha'
#l47_dev_name = raw_input("L4-L7 Device Name: ")

vlan_tagged = False
#vlan_tagged =  raw_input("Tagged VLAN True/False: ")

interface1 = 'G0/3'
interface1 = raw_input("Interface1 i.e. unmanaged graph is on G0/1, for no graph use G0/3: ")

interface2 = 'G0/4'
interface2 = raw_input("Interface2 i.e. unmanaged graph is on G0/2, for no graph use G0/4: ")

data_ip1 = '10.1.0.1/16'
#data_ip1 = raw_input("Interface1 IP/mask i.e. 10.1.0.1/16: "

data_ip2 = '10.2.0.1/24'
#data_ip2 = raw_input("Interface1 IP/mask i.e. 10.2.0.1/24: "

ifname1 = 'app'
#ifname1 =  raw_input("Interface1 name i.e. app-nic: ")

ifname2 = 'db'
#ifname2 =  raw_input("Interface2 name i.e. db-nic: ")

vlan1 = 310
#vlan1 =  raw_input("Interface1 VLAN tag number i.e. 310: ")

vlan2 = 311
#vlan2 =  raw_input("Interface2 VLAN tag number i.e. 311: ")

zone1 = 'app-zone'
#zone1 =  raw_input("Zone1 name i.e. app-zone: ")

zone2 = 'db-zone'
#zone2 =  raw_input("Zone2 name i.e. db-zone: ")

ftd_ip1 = "10.0.0.51"
#ftd_ip1 =  raw_input("FTD1 IP address i.e. 10.0.0.51: ")

ftd_ip2 = "10.0.0.52"
#ftd_ip2 =  raw_input("FTD2 IP address i.e. 10.0.0.52: ")

fmc_ip = "10.0.0.30"
#fmc_ip =  raw_input("FMC IP address i.e. 10.0.0.30: ")

username = "apiuser"
#username =  raw_input("Username for FMC: ")

password = "cisco"
#password =  raw_input("Password for FMC: ")

virtual = True
#virtual =  raw_input("FTD virtua i.e. True/False: ")

policy_name = 'ftd-policy'
#policy_name = raw_input("FMC policy name: ")
rule1_name = 'ftd-rule1'
#rule1_name = raw_input("FMC rule1 name: ")
rule1_bidir = 'true'

rule2_name = 'ftd-rule2'
#rule2_name = raw_input("FMC rule2 name: ")
rule2_bidir = 'true'


bvi_ip = '10.1.0.1/16'
bvi_id = 1


config_dev = {
   "dn": "uni/tn-%s/lDevVip-%s/vFTD-l3fw" % (tenant_name,l47_dev_name),
   "name": "FTD-HA1",
   "host": fmc_ip,
   "virtual": virtual,
   "devs": {
      "Device1": {
         "dn": "uni/tn-%s/lDevVip-%s/vFTD-l3fw/cDev-Device1" % (tenant_name,l47_dev_name),
         "state": 2,
         "host": ftd_ip1,
         "virtual": virtual,
         "manager": {
            "hosts": {
               fmc_ip: {
                  "port": 443
               }
            },
            "name": "fmc62",
            "creds": {
               "username": username,
               "password": password
            }
         },
         "version": "6.2.2 (build 81)",
         "port": 443,
         "creds": {
            "username": username,
            "password": password
         }
      },
      "Device2": {
         "dn": "uni/tn-%s/lDevVip-%s/vFTD-l3fw/cDev-Device2" % (tenant_name,l47_dev_name),
         "state": 2,
         "host": ftd_ip2,
         "virtual": virtual,
         "manager": {
            "hosts": {
               fmc_ip: {
                  "port": 443
               }
            },
            "name": "fmc62",
            "creds": {
               "username": username,
               "password": password
            }
         },
         "version": "6.2.2 (build 81)",
         "port": 443,
         "creds": {
            "username": username,
            "password": password
         }
      }
   },
   "manager": {
            "hosts": {
               fmc_ip: {
            "port": 443
         }
      },
      "name": "fmc62",
      "creds": {
         "username": username,
         "password": password
      }
   },
   "contextaware": False,
   "funcmode": 1,
   "port": 443,
   "creds": {
      "username": username,
      "password": password
   }
}
config = {
   (0, '', 4548): {
      'dn': "uni/vDev-[uni/tn-pod3/lDevVip-vFTD-l3fw]-tn-[uni/tn-pod3]-ctx-pod3net",
      'transaction': 0,
      'ackedstate': 0,
      'value': {
         (4, 'SecurityZone', zone1): {
            'state': 2,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'type', 'type'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "ROUTED"
               }
            }
         },
         (1, '', 4800): {
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (3, 'FTD', 'l3fw'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'AccessPolicyFolder', 'AccessPolicyFolder'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InAccessPolicyRel', 'InAccessPolicyRel'): {
                              'state': 2,
                              'transaction': 0,
                              'target': policy_name,
                              'ackedstate': 0
                           }
                        }
                     },
                     (2, 'external', 'consumer'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (9, '', 'vFTD-l3fw_app_2293763_16388'): {
                              'state': 2,
                              'transaction': 0,
                              'target': "vFTD-l3fw_app_2293763_16388",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'ExIntfConfigRelFolder', 'ExtConfig'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'ExIntfConfigRel', 'ExtConfigrel'): {
                              'connector': "consumer",
                              'state': 2,
                              'transaction': 0,
                              'target': "externalInterface",
                              'ackedstate': 0
                           }
                        }
                     },
                     (2, 'internal', 'provider'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (9, '', 'vFTD-l3fw_db_2293763_32774'): {
                              'state': 2,
                              'transaction': 0,
                              'target': "vFTD-l3fw_db_2293763_32774",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'InIntfConfigRelFolder', 'IntConfig'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InIntfConfigRel', 'InConfigrel'): {
                              'connector': "provider",
                              'state': 2,
                              'transaction': 0,
                              'target': "internalInterface",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               }
            },
            'state': 2,
            'absGraph': "l3fw-ftdv-graph",
            'rn': "vGrp-[uni/tn-pod3/GraphInst_C-[uni/tn-pod3/brc-app-to-db]-G-[uni/tn-pod3/AbsGraph-l3fw-ftdv-graph]-S-[uni/tn-pod3/ctx-pod3net]]"
         },
         (4, 'AccessPolicy', policy_name): {
            'state': 2,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (4, 'AccessRule', rule1_name): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'AccDestinationZones', 'AccDestinationZones'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'DestinationZones', 'DestinationZones'): {
                              'state': 2,
                              'transaction': 0,
                              'target': "internalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     },
                     (5, 'bidirectional', 'Bi-Directional'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': rule1_bidir
                     },
                     (4, 'AccSourceZones', 'AccSourceZones'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'SourceZones', 'SourceZone'): {
                              'state': 2,
                              'transaction': 0,
                              'target': "externalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               },
               (4, 'AccessRule', rule2_name): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (5, 'bidirectional', 'bidirectional'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': rule2_bidir
                     },
                     (4, 'AccDestinationZones', 'AccDestinationZones'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'DestinationZones', 'DestinationZones'): {
                              'state': 2,
                              'transaction': 0,
                              'target': "internalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'AccSourceZones', 'AccSourceZones'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'SourceZones', 'SourceZones'): {
                              'state': 2,
                              'transaction': 0,
                              'target': "externalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               }
            }
         },
         (8, '', 'vFTD-l3fw_app_2293763_16388'): {
            'state': 2,
            'transaction': 0,
            'vif': "vFTD-l3fw_app",
            'ackedstate': 0,
            'encap': "2293763_16388"
         },
         (8, '', 'vFTD-l3fw_db_2293763_32774'): {
            'state': 2,
            'transaction': 0,
            'vif': "vFTD-l3fw_db",
            'ackedstate': 0,
            'encap': "2293763_32774"
         },
         (7, '', '2293763_16388'): {
            'transaction': 0,
            'ackedstate': 0,
            'portgroup': "pod3|vFTD-l3fwctxpod3netweb|app",
            'state': 2,
            'tag': vlan1,
            'type': 1
         },
         (4, 'SecurityZone', zone2): {
            'state': 2,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'type', 'type'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "ROUTED"
               }
            }
         },
         (4, 'InterfaceConfig', 'externalInterface'): {
            'state': 2,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'ifname', 'ifname'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': ifname1
               },
               (5, 'enabled', 'enabled'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "True"
               },
               (4, 'IPv4Config', 'IPv4Config'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'static', 'static'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (5, 'address', 'address'): {
                              'state': 2,
                              'transaction': 0,
                              'ackedstate': 0,
                              'value': data_ip1
                           }
                        }
                     }
                  }
               },
               (4, 'int_security_zone', 'int_security_zone'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (6, 'security_zone', 'security_zone'): {
                        'state': 2,
                        'transaction': 0,
                        'target': zone1,
                        'ackedstate': 0
                     }
                  }
               }
            }
         },
         (4, 'InterfaceConfig', 'internalInterface'): {
            'state': 2,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'ifname', 'ifname'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': ifname2
               },
               (5, 'enabled', 'enabled'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "True"
               },
               (4, 'IPv4Config', 'IPv4Config'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'static', 'static'): {
                        'state': 2,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (5, 'address', 'address'): {
                              'state': 2,
                              'transaction': 0,
                              'ackedstate': 0,
                              'value': data_ip2
                           }
                        }
                     }
                  }
               },
               (4, 'int_security_zone', 'int_security_zone'): {
                  'state': 2,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (6, 'security_zone', 'security_zone'): {
                        'state': 2,
                        'transaction': 0,
                        'target': zone2,
                        'ackedstate': 0
                     }
                  }
               }
            }
         },
         (10, '', 'vFTD-l3fw_db'): {
            'state': 2,
            'transaction': 0,
            'cifs': {
               'Device1': interface2,
               'Device2': interface2
            },
            'ackedstate': 0
         },
         (7, '', '2293763_32774'): {
            'transaction': 0,
            'ackedstate': 0,
            'portgroup': "pod3|vFTD-l3fwctxpod3netdb|db",
            'state': 2,
            'tag': vlan2,
            'type': 1
         },
         (10, '', 'vFTD-l3fw_app'): {
            'state': 2,
            'transaction': 0,
            'cifs': {
               'Device1': interface1,
               'Device2': interface1
            },
            'ackedstate': 0
         }
      },
      'txid': 10016,
      'tagPackets': vlan_tagged,
      'state': 2,
      'ctxName': "pod3net",
      'tenant': tenant_name
   }
}
from device_script import serviceModify
serviceModify (config_dev,config)
