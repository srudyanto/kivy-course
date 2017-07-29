from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class container(BoxLayout):
    pass
    
class Boxlayoutapp(App):
    def build(self):
        return container()
        
if __name__ == "__main__":
    Boxlayoutapp().run()
    