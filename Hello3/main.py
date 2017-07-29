from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<Hello3Layout>:
    Button:
        text: "Hello World!!!"
''')

class Hello3Layout(BoxLayout):
    pass
    
class Hello3App(App):
    def build(self):
        return Hello3Layout()
    
if __name__=="__main__":
    Hello3App().run()
    
