import flet as ft
from flet import (Column, Row, Text, TextField, Page, UserControl, colors, icons)


class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


def main(page: Page):
    page.title = "Group Name <3"

    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank :)"
            user_name.update()
        else:
            page.session.set("user_name", user_name.value)
            page.dialog.open = False
            new_message.prefix = Text(f"{user_name.value}: ")
            page.pubsub.send_all(Message(
                user_name=user_name.value,
                text=f"{user_name.value} has joined the chat.",
                message_type="login_message"))
            page.update()

    def send_click(e):
        if new_message.value != "":
            page.pubsub.send_all(Message(
                user_name=page.session.get("user_name"),
                text=new_message.value,
                message_type="chat_message"))
            new_message.value = ""
            page.update()

    def on_message(message: Message):
        # after any property of a control are updated
        # \update() method should be called for effect to take place
        if message.message_type == "chat_message":
            chat.controls.append(Text(f"{message.user_name}: {message.text}"))
        elif message.message_type == "login_message":
            chat.controls.append(Text(message.text, italic=True, size=12, opacity=0.7))
        page.update()

    page.pubsub.subscribe(on_message)

    user_name = TextField(label="Enter your name")

    chat = ft.ListView(
        expand=True,
        auto_scroll=True,
    )

    new_message = TextField(
        hint_text="Type a message here...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=15,
        filled=True,
        expand=True,
        on_submit=send_click,
    )

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
