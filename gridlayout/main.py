from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GridLayout(GridLayout):
    pass
    
class Gridlayoutapp(App):
    def build(self):
        return GridLayout()
        
if __name__=="__main__":
    Gridlayoutapp().run()
    