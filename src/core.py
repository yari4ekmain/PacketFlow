
from scapy.all import sniff, IP, TCP, get_if_list
import datetime
iface_name = "\\Device\\NPF_{8D50EC07-D06E-4FB5-9D2F-D57315AD9516}"
class TSP_IP():
    def __init__(self, callback):
        self.callback = callback
    def _interfeis(self):
        self.interfeis = get_if_list()
        return self.interfeis
    def pkt_callback(self,pkt):
        if IP not in pkt or TCP not in pkt:
            return
        ip = pkt[IP]
        tcp = pkt[TCP]
        self.callback(ip,tcp)
    def start(self,interfeis=None,count = 10):
        if interfeis == None:
            interfeis = self._interfeis()
        sniff(iface=interfeis, prn=self.pkt_callback, count=count)
