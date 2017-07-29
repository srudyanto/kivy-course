import kivy

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def animate(self,instance):
        animation = Animation(pos=(100,100),t='out_bounce')
        animation += Animation(pos=(200,100), t='out_bounce')
        animation &= Animation(size=(500,500))
        animation += Animation(size=(100,50))
        animation.start(instance)
        
    def build(self):
        button = Button(size_hint=(None,None),text='plop', on_press=self.animate)
        return button
        
if __name__=="__main__":
    TestApp().run()
    