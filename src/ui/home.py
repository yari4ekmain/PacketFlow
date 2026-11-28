

import flet as ft

class Home(ft.Container):
    def __init__(self,cache,inform):
        super().__init__()
        self.inf = inform
        self.cache = cache
        self.content = ft.TextButton('TCP and UDP',on_click=self._click)

    async def _click(self, e):
        await self.inf('/tcp_and_udp')