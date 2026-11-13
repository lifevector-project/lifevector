import flet as ft


def main(page: ft.Page):
    page.title = "LifeVector"
    page.add(ft.Text("Hello, LifeVector"))


def run():
    ft.run(main)
