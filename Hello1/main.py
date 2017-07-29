from kivy.app import App
from kivy.uix.button import Button

class Hello1App(App):
    def build(self):
        return Button(text='Hello World!!',size=100,100)
        
if __name__=="__main__":
    Hello1App().run()