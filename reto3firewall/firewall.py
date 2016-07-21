"""
Coursera:
- Software Defined Networking (SDN) course
-- Module 4 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
import os
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/taller_sdn_ee24/reto3firewall/firewall-policies.csv" % os.environ['HOME']


class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp(self, event):
        """[TALLER SDN (1/2)]

        Con la libreria de csv de python y la clase DictReader de dicha libreria lee el fichero csv.
        Ten en cuenta que la primera linea del csv son los nombres de las columnas. Por cada linea (excepto la
        primera linea), llama a la funcion sendOpenFlowMessage() para que cree un mensaje FlowMod que bloque el
        trafico de la MAC origen a la MAC destino.
        """
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))


def sendOpenFlowMessage(event, mac_0, mac_1):
    """[TALLER SDN (2/2)]

    Crea un msg flow_mod con la funcion ofp_flow_mod() de la libreria de POX. Modifica ese objeto msg con el match field
    de direccion MAC origen y direccion MAC destino. Ademas, asigna el hard timeout, idle time out y priority deseado.
    A continuacion, fija la accion a DROP (es la accion por defecto). Finalmente envia el mensaje flow mod al switch.
    """


def launch():
    """
    Starting the Firewall module
    """
    core.registerNew(Firewall)
