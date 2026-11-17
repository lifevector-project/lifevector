import flet as ft
from lifevector.db.connections import Database


def main(page: ft.Page):
    page.title = "LifeVector"
    page.add(ft.Text("Hello, LifeVector"))

    db_manager = Database()
    db_manager.init_db()


def run():
    ft.run(main)