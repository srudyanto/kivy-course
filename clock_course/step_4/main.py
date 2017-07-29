from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import time

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)

class ClockApp(App):
    def update_time(self,nap):
        self.root.time_prop.text = time.strftime('[b]%H[/b]:%M:%S')
    
    def on_start(self):
        Clock.schedule_interval(self.update_time,1)
    
if __name__=='__main__':
    ClockApp().run()