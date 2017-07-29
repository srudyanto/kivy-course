from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class StackLayoutApp(App):
    def build(self):
        root = StackLayout(orientation='rl-bt')
        for i in range(25):
            btn = Button(text=str(i), width = 40 + i *5, size_hint=(None,0.15))
            root.add_widget(btn)
        return root
        
if __name__=='__main__':
    StackLayoutApp().run()
    