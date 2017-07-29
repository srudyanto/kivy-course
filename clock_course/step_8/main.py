from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
import time

LabelBase.register(name='Roboto',
                   fn_regular='Roboto-Thin.ttf',
                   fn_bold='Roboto-Medium.ttf',
                   )

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)
    sw_prop = ObjectProperty(None)

class ClockApp(App):
    sw_seconds = 0
    sw_started = False
    
    def update_time(self,nap):
        minutes, seconds =divmod(self.sw_seconds,60)
        
        self.root.time_prop.text = time.strftime('[b]%H[/b]:%M:%S')
        if self.sw_started:
            self.sw_seconds += nap
        self.root.sw_prop.text = ('%02d:%02d.[size=40]%02d[/size]'%(int(minutes), int(seconds), int(seconds*100%100)))
    
    def on_start(self):
        Clock.schedule_interval(self.update_time,0)
        
    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started
        
    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text='Start'
            self.sw_started=False
        self.sw_seconds=0
    
if __name__=='__main__':
    ClockApp().run()