from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class container(GridLayout):
    pass
    
class Anchorlayout(App):
    def build(self):
        return container()
        
if __name__ == "__main__":
    Anchorlayout().run()
    