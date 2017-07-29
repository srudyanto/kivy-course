from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout

class root(ScatterLayout):
    pass
    
class Scatterlayoutapp(App):
    def build(self):
        return root()
        
if __name__=="__main__":
    Scatterlayoutapp().run()