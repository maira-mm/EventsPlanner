import flet as ft
from flet import (Checkbox,Column, Row, Page, UserControl, FloatingActionButton, IconButton, TextField, colors, icons)

group_number = 8

class PollAdmin(UserControl):
    def __init__(self, poll_name: str, poll_choices: list):
        #later make poll_choices and poll_perc a dictionary
        super().__init__()
        self.poll_name = poll_name
        self.poll_choices = poll_choices
        # self.poll_delete = poll_delete
        poll_choices = []


    def build(self):
        #UI
        number = 1
        self.new_poll_name = TextField(hint_text="What would you like to name your poll?", expand=True)
        self.new_poll_choices = TextField(hint_text=f"Option {number}", expand=True)
        poll_name.value = tree
        poll_name.update()
        poll_choices.value = oak
        poll_choices.update()
        #poll_name = self.new_poll_name
        #poll_choices = self.new_poll_choices
        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.new_poll_choices,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.poll_edit,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete option",
                            on_click=self.poll_delete
                        ),
                    ],
                ),
            ],
        )

        return Column(
                self.display_view
            )

    def poll_delete(e):
        pass

    def poll_edit(self):
        pass



    #def button_clicked(e):
    #    t.value = f"Your poll result is: {e.control.value}"
    #    page.update()

    #t = ft.Text()
    # g = ft.ElevatedButton(text="Go Back", on_click=#go back to chatbox)
    # input like a to-do list
    # have a confirm button (so it can be sent
    # have the percentage be the num of people in group
    # it will be static to begin with, but then add login features, now group num will be dynamic

    #cg = ft.RadioGroup(content=ft.Column([
    #    ft.Radio(value="1", label="1"),
    #    ft.Radio(value="2", label="2")
    #]), on_change=button_clicked)

    #page.add(ft.Text(f"Hi, choose:"), cg, t)

#class PollInterface(UserControl):
    def build(self):
        num = 0
        poll_name = TextField(hint_text="What would you like to name your poll?", expand = True)
        self.poll_choices = TextField(hint_text=f"Option {num}")
        if self.poll_choices.value:
            num +=1



def main(page: Page):
    page.title = f"name"
    page.horizontal_alignment = "center"
    page.update()

    app = PollAdmin()

    page.add(app)

    #def add_poll(e):
    #    if not poll_name.value:
    #        poll_name.value = "Poll"
    #        poll_name.update()
    #    else:
    #        page.session.set("poll_name", poll_name.value)
    #        page.dialog.open = False


ft.app(target=main)