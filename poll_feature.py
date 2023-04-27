import flet as ft
from flet import (Radio,
                   Column,
                   Row,
                   Page,
                   UserControl,
                   FloatingActionButton,
                   IconButton,
                   TextField,
                   colors,
                   icons)

class PollAdmin(UserControl):
    def __init__(self, poll_name, poll_choices):
        super().__init__()
        self.poll_name = poll_name
        self.poll_choices = poll_choices

    def build(self):
        return button_clicked

    def button_clicked(self):
        #UI, return a list
        t.value = f"Your poll result is: {e.control.value}"
        page.update()

        t = ft.Text()
        g = ft.ElevatedButton(text="Go Back", on_click=self.button_clicked)

        cg = ft.RadioGroup(content=ft.Column([
           ft.Radio(value="1", label="1"),
           ft.Radio(value="2", label="2")
        ]), on_change=button_clicked)

        page.add(ft.Text(f"Hi, choose:"), cg, t)

def main(page):

ft.app(target=main)