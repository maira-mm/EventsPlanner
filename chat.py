import flet as ft
from flet import (Column, Row, Text, TextField, Page, UserControl, colors, icons)


class Message():
    def __init__(self, user:str, text:str, message_type:str):
        self.user = user
        self.text = text
        self.message_type = message_type


def main(page: Page):
    chat = Column()
    new_message = TextField()

    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank :)"
            user_name.update()
        else:
            page.session.set("username", user_name.value)
            page.dialog.open = False
            page.pubsub.send_all(Message(
                user=user_name.value,
                text=f"{user_name.value} has joined the chat.",
                message_type="login_message"))
            page.update()

    def send_click(e):
        page.pubsub.send_all(Message(user=page.session.get('user_name'), text=new_message.value, message_type="chat_message"))
        new_message.value = ""
        page.update()



    def on_message(message: Message):
        # after any property of a control are updated
        # \update() method should be called for effect to take place
        if message.message_type == "chat_message":
            chat.controls.append(Text(f"{message.user}: {message.text}"))
        elif message.message_type == "login_message":
            chat.controls.append(
                Text(message.text, italic=True, size=12, opacity=0.7)
            )
        page.update()

    page.pubsub.subscribe(on_message)

    user_name = TextField(label="Enter your name")

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=Text("Welcome to your Personal Event Planner!!"),
        content=Column([user_name], tight=True),
        actions=[ft.ElevatedButton(text="Join the Chat", on_click=join_click)],
        actions_alignment="end",
    )

    page.add(
        chat, Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )



ft.app(target=main, view=ft.WEB_BROWSER)
