from random import randint
from math import cos,sin,sqrt
from pyglet.window import Window,key
from pyglet import shapes,graphics
from pyglet.text import Label
from pyglet import clock

from imgui.integrations.pyglet import create_renderer

import pyglet
import imgui

  

def isPrimer(n):
    for i in range(2,round(sqrt(n)+1)):
        if n>2 and n%i==0 :
            return False
    return True

class App(Window):
    W,H=800,600  #width,heigt
    FPS=60 
    COLOR_NUMS=[6,44,710]
    K=0.1
    N=10 
    JustPrimer=False
    def __init__(self):
        super().__init__(App.W,App.H , 'Primers View', resizable=False)
        self.set_vsync(False)
        self._color_num_index=0
        self._colors=[]
        self._points=[]
        
        clock.schedule_interval(self.update, 1/App.FPS)

        self._batch=graphics.Batch()
        self._tip=Label('press SPACE change colors',font_size=18,color=(5,235,28,210),x=20,y=App.H-40,batch=self._batch)
        imgui.create_context()
        self._impl = create_renderer(self)
        App.K=App.H/2/App.N

    def make_colors(self):
        num_colors=App.COLOR_NUMS[self._color_num_index]
        self._colors.clear()
        for i in range(num_colors):
            c=(randint(50,256),randint(50,256),randint(50,256))
            self._colors.append(c)  

    def make_points(self):
        self._points.clear()
        for i in range(2,App.N+1):
            flag=isPrimer(i)
            if App.JustPrimer and not flag:
                continue
            r=2 if flag else 1
            x,y=App.W//2+i*cos(i)*App.K, App.H//2+i*sin(i)*App.K
            color_num=App.COLOR_NUMS[self._color_num_index]
            circle = shapes.Circle(x=x,y=y,radius=r,color=self._colors[i%color_num],batch=self._batch)
            self._points.append(circle)
        
    def draw(self):
        self.clear()
        self._batch.draw()
        imgui.render()
        self._impl.render(imgui.get_draw_data())

        
    def on_key_press(self, symbol, modifiers):# callback
        super().on_key_press(symbol, modifiers)
        if symbol==key.SPACE :
            self._color_num_index=(self._color_num_index+1)%len(App.COLOR_NUMS)
            self._tip.text=str(App.COLOR_NUMS[self._color_num_index])
            self.make_colors()
            self.make_points()

    def update(self, dt):
        imgui.new_frame()
        imgui.begin("Config")
        changed, App.N = imgui.slider_int("N", App.N, min_value = 10, max_value = 99000)
        changed1, App.JustPrimer = imgui.checkbox(
                "Only Show Primer", # Label
                App.JustPrimer # Input current state
            )
        if changed or changed1 :
            App.K=App.H/2/App.N
            #print(App.H,App.N,App.K)
            self.make_colors()
            self.make_points()
        imgui.end()
        self.draw()

if __name__ == "__main__":
    App()
    pyglet.app.run()
