import flet as ft
import datetime
from core import TSP_IP,get_outbound_local_ip
class TCP_USP(ft.Container):
    def __init__(self,cache,inform):
        super().__init__()
        self.inf = inform
        
        self.cache = cache
        self.content = ft.ListView([],scroll=ft.ScrollMode.AUTO)
        self.ip_addres = get_outbound_local_ip()
        self.buttom_bar = ft.Row([
            ft.IconButton(icon=ft.Icons.START, on_click=self._start,bgcolor="#1eac49"),
            ft.TextField(width=100),
            ft.IconButton(icon=ft.Icons.STOP,bgcolor="#790000"),
            ft.IconButton(icon=ft.Icons.SETTINGS,bgcolor="#000000")
        ],expand=True,alignment=ft.MainAxisAlignment.SPACE_AROUND)
    def did_mount(self):
        self.page.floating_action_button = ft.FloatingActionButton(self.buttom_bar,width=300,bgcolor="#363636")   
        self.page.update()

    def callback(self,ip,tcp):
        payload = bytes(tcp.payload)[:64]
        hex_view = payload.hex(" ")

        ascii_view = "".join(
            chr(b) if 32 <= b <= 126 else "."
            for b in payload
        )
    
        payload_preview = f"HEX: {hex_view}\nASCII: {ascii_view}"
        ignore_port = ft.Button('ignore')
        time = ft.Text(str(datetime.datetime.now()),size=10)
        src = ft.Text(f"{ip.src}:{tcp.sport}",color=("#008f00" if ip.src == self.ip_addres else "#b9b9b9"))
        dst = ft.Text(f"{ip.dst}:{tcp.dport}",color=("#008f00" if ip.dst == self.ip_addres else "#b9b9b9"))
        
        fin_cont = ft.Container(ft.Column([time,ft.Row([ft.Text('TCP:'),src,ft.Text('-->'),dst,ignore_port]),ft.Text(f"{payload_preview}")]),bgcolor="#313030",
                                border_radius=15,padding=15, margin=5)
        self.content.controls.append(fin_cont)
        self.update()
    def _start(self,e):
        tsp_ip = TSP_IP(self.callback)
        tsp_ip.start(count=200)
         
