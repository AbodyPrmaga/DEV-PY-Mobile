from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.selectioncontrol import MDCheckbox



class TodoCard(MDCard):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = "80dp"
        self.padding = "8dp"
        self.radius = [12]
        self.elevation = 6
        self.orientation = "horizontal"
        self.spacing = "10dp"

        self.checkbox = MDCheckbox(size_hint=(None, None), size=("40dp", "40dp"))
        self.label = MDLabel(text=text, halign="left", valign="center")
        self.remove_btn = MDIconButton(icon="delete", on_release=self.delete_self)

        self.add_widget(self.checkbox)
        self.add_widget(self.label)
        self.add_widget(self.remove_btn)

    def delete_self(self, *args):
        self.parent.remove_widget(self)


class TodoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        screen = MDScreen()

        self.task_input = MDTextField(
            hint_text="Enter a task",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5},
        )

        self.task_list = MDBoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter("height"))

        scroll = MDScrollView()
        scroll.add_widget(self.task_list)

        add_btn = MDIconButton(
            icon="plus-circle",
            pos_hint={"center_x": 0.9},
            on_release=self.add_task,
        )

        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)
        layout.add_widget(self.task_input)
        layout.add_widget(scroll)
        layout.add_widget(add_btn)

        screen.add_widget(layout)
        return screen

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            task_card = TodoCard(text=task_text)
            self.task_list.add_widget(task_card)
            self.task_input.text = ""


TodoApp().run()
