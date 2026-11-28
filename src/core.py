import socket
from scapy.all import sniff, IP, TCP, UDP, get_if_list
class TSP_IP():
    
    def __init__(self, callback):
        self.callback = callback
  


    def _interfeis(self):
        self.interfeis = get_if_list()
        print('true')
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
        
def _my_ipaddres():
    try:
        host_name = socket.gethostname()
        print(host_name)
        return socket.gethostbyname(host_name)
    except socket.gaierror as e:
        return False
def get_outbound_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        return False
        
    finally:
        s.close()