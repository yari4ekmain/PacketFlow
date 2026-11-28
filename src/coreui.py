from cache import Cache
from ui.home import Home
from ui.tcp_udp import TCP_USP
import flet as ft
async def main(page: ft.Page):
    page.title = "calend tool"
    cache = Cache()
    async def inform(route: str):
        await page.push_route(f'{route}')


    routes = {
        '/home': lambda: Home(cache,inform),
        '/tcp_and_udp': lambda: TCP_USP(cache,inform),
 
    }
    

    
    def route_change(e):
        page.views.clear()
        builder = routes.get(page.route)
        if builder:
            page.views.append(ft.View(
                route=page.route,
                controls=[builder()],
                scroll=ft.ScrollMode.AUTO
            ))
            
        page.update()
    page.on_route_change = route_change
    await page.push_route("/home")
    page.window.height = 700
    page.window.width = 1500
    page.update()





ft.run(main)