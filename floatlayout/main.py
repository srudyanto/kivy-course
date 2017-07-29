from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class root(FloatLayout):
    pass
    
class Floatlayoutapp(App):
    def build(self):
        return root()
        
if __name__=="__main__":
    Floatlayoutapp().run()