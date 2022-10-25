import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button

KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x":0.5, "center_y":0.5}

        Label:
                front_size: "30sp"
                text: root.data_label

        Button:
                text: "Поиск по названию"
                bold: True
                backgraund_color: '#00ffce'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "Поиск по названию"
                bold: True
                backgraund_color: '#00ffce'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "Поиск по названию"
                bold: True
                backgraund_color: '#00ffce'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "Поиск по названию"
                bold: True
                backgraund_color: '#00ffce'
                size_hint: (1,0.5)
                on_press: root.callback()                                
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Треугольник!")

    def callback(self):
        print("Поиск по названию")


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()


