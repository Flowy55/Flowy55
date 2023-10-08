import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import random 

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    def throw(self):
        number = random.randint(1, 2)
        if number == 1:
            self.monetochka.text = "Орел!"
        if number == 2:
            self.monetochka.text = "Решка"
    def pred(self):
        self.predict.text = random.choice(["да.", "нет.", 'возможночастично.', "возможно.", "частично."])
class RandomApp(App):
    def build(self):
        return MyRoot()

randomApp = RandomApp()
randomApp.run()
