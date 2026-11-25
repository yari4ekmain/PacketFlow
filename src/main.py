import flet as ft
from core import TSP_IP
import datetime
def main(page: ft.Page):
    def callback(ip,tcp):
        payload_preview = bytes(tcp.payload)[:120].decode("utf-8", errors="replace").replace("\n", " ")
        print(f"time: {datetime.datetime.now()} | TCP {ip.src}:{tcp.sport} -> {ip.dst}:{tcp.dport} | {payload_preview}")
    def _start(e):
        TSP_IP(callback).start(count=20)

    page.floating_action_button = ft.FloatingActionButton(
        content='Start', key="increment", on_click=_start
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
