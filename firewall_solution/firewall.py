'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 4 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import csv



log = core.getLogger()
policyFile = "%s/pox/pox/taller_sdn_ee24/firewall-policies.csv" % os.environ[ 'HOME' ]




class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):    
        ''' TODO: Read the file...'''

        with open(policyFile) as csvfile:
            policyReader = csv.DictReader(csvfile)
            for row in policyReader:
                sendOpenFlowMessage(event, row['mac_0'], row['mac_1'])
        ''' Hasta aqui'''

        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def sendOpenFlowMessage(event, mac_0, mac_1):
    '''TODO: Generate the OpenFlow messages'''
    print(mac_0, mac_1)
    msg = of.ofp_flow_mod()
    msg.match._dl_src = EthAddr(mac_0)
    msg.match._dl_src = EthAddr(mac_1)
    msg.hard_timeout = 60
    msg.idle_timeout = 30
    msg.priority = 1
    #msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)
    '''Hasta aqui '''


def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)

