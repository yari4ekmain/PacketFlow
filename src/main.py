import flet as ft
from core import TSP_IP,get_outbound_local_ip
import datetime
def main(page: ft.Page):
    column_ip_trafik = ft.ListView([],scroll=ft.ScrollMode.AUTO)
    ip_addres = get_outbound_local_ip()
    
    def callback(ip,tcp):
        payload = bytes(tcp.payload)[:64]
        hex_view = payload.hex(" ")

        ascii_view = "".join(
            chr(b) if 32 <= b <= 126 else "."
            for b in payload
        )

        payload_preview = f"{hex_view}\n{ascii_view}"

        time = ft.Text(str(datetime.datetime.now()),size=10)
        src = ft.Text(f"{ip.src}:{tcp.sport}",color=("#008f00" if ip.src == ip_addres else "#b9b9b9"))
        dst = ft.Text(f"{ip.dst}:{tcp.dport}",color=("#008f00" if ip.dst == ip_addres else "#b9b9b9"))
        
        fin_cont = ft.Container(ft.Column([time,ft.Row([ft.Text('TCP:'),src,ft.Text('-->'),dst]),ft.Text(f"{payload_preview}")]),bgcolor="#313030",
                                border_radius=15,padding=15, margin=5)
        column_ip_trafik.controls.append(fin_cont)
        page.update()
    def _start(e):
        tsp_ip = TSP_IP(callback)
        tsp_ip.start(count=200)
    page.floating_action_button = ft.FloatingActionButton(
        content='Start', key="increment", on_click=_start
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                column_ip_trafik,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
