from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongBall(Widget):
    velocity_x = NumericProperty(1)
    velocity_y = NumericProperty(1)
    
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity)+ self.pos
        
class PongPaddle(Widget):
    score = NumericProperty(0)
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speed_up = 1.1
            offset = 0.02 * Vector(0,ball.center_y  - self.center_y)
            ball.velocity = speed_up * (offset - ball.velocity)
            
        
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    def serve_ball(self, vel=(4,0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        
    def update(self, dt):
        self.ball.move()
        
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
            
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball()
            
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball()
        
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
            
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
            
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
        
if __name__=="__main__":
    PongApp().run()