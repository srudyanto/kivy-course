from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import time

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)
    sw_prop = ObjectProperty(None)

class ClockApp(App):
    sw_seconds = 0
    
    def update_time(self,nap):
        self.sw_seconds += nap
        minutes, seconds =divmod(self.sw_seconds,60)
        
        self.root.time_prop.text = time.strftime('[b]%H[/b]:%M:%S')
        self.root.sw_prop.text = ('%02d:%02d.[size=40]%02d[/size]'%(int(minutes), int(seconds), int(seconds*100%100)))
    
    def on_start(self):
        Clock.schedule_interval(self.update_time,0)
    
if __name__=='__main__':
    ClockApp().run()