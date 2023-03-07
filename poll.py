import flet as ft
from flet import (Checkbox,Column, Row, Page, UserControl, FloatingActionButton, IconButton, TextField, colors, icons)

class Poll():
    def __init__(self):
        #poll_name: str, poll_options: str, poll_delete
        super().__init__()
        #self.poll_name = poll_name
        #self.poll_delete = poll_delete

    #def build(self):

def main(page):
    def button_clicked(e):
        t.value = f"Your poll result is:{cg.value}"
        page.update()
    t = ft.Text()
    b = ft.ElevatedButton(text="Confirm", on_click=button_clicked)
        #input like a to-do list
        #have a confirm button (so it can be sent
        #have the percentage be the num of people in group
        #it will be static to begin with, but then add login features, now group num will be dynamic

    cg = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="1", label="1"),
        ft.Radio(value="2", label="2")
        ]))

    page.add(ft.Text(f"Hi, choose"), cg, t)

ft.app(target=main)