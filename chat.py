import flet as ft
from flet import (Column, Row, Text, TextField, Page, UserControl, colors, icons)


class Message():
    def __init__(self, user:str, text:str):
        self.user = user
        self.text = text


def main(page: Page):
    chat = Column()
    new_message = TextField()

    def on_message(message: Message):
        # after any property of a control are updated
        # \update() method should be called for effect to take place
        chat.controls.append(Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(Message(user=page.session_id, text=new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        chat, Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )


ft.app(target=main, view=ft.WEB_BROWSER)
