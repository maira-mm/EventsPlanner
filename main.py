import flet as ft
import time, threading




#chatbox - for mult users

#   user login

class GreeterControl(ft.UserControl):
    def build(self):
        return ft.Column([
            ft.Text(value = "Welcome to your Personal Events Planner"),
        ft.TextField(label="Your name"),
        ft.ElevatedButton("Login")])




def main(page: ft.Page):
    page.title = "Your Personal Event Planner"
    page.add(GreeterControl())

    page.update()


ft.app(target=main)