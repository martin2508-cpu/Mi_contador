
import flet as ft


class ContadorApp:

    def __init__(self, page):
        self.page = page
        self.contador = 0

        self.texto_contador = ft.Text(
            "0",
            size=50,
            weight=ft.FontWeight.BOLD
        )

    def incrementar(self, e):
        self.contador += 1
        self.texto_contador.value = str(self.contador)

    def reiniciar(self, e):
        self.contador = 0
        self.texto_contador.value = str(self.contador)

    def construir(self):
        self.page.title = "Contador Interactivo"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.page.add(
            ft.Text("Mi contador", size=25),
            self.texto_contador,
            ft.Button(
                content="Incrementar",
                on_click=self.incrementar
            ),
            ft.Button(
                content="Reiniciar",
                on_click=self.reiniciar
            )
        )


def main(page: ft.Page):
    aplicacion = ContadorApp(page)
    aplicacion.construir()


ft.run(main)
