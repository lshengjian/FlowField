from .ui import UISettings, _UI
#from base.simulation import Simulation
#import pyglet
from pyglet.window import mouse,Window,FPSDisplay
from pyglet import clock
from pyglet.math import Vec2
from .model import Space,SamplePoint
from .view import SapceView,Ball

class App(Window):
    def __init__(
        self,
        width: int,
        height: int,
        settings: UISettings,

        name: str = "My Flow Field Demo",
        dt: float = 1 / 60,
    ):
        super().__init__(width, height, name, resizable=True)
        self.set_vsync(False)
        clock.schedule_interval(self.update, dt)
        self._fps_display = FPSDisplay(window=self)
        
        self._UI = _UI(self, settings)
        start=Vec2(-4,-4)
        end=Vec2(7,4)
        self._space=Space(start,end,offset=Vec2(0.5,0.5))
        self._space_view = SapceView((width,height),start,end)
        self._ball=Ball((width,height),start,end,SamplePoint(Vec2(0.5,3.8)))
        for sp in self._space:
            self._space_view.add_point(sp)
        

    def on_draw(self):
        self.clear()
        self._fps_display.draw()
        self._space_view.render()
        self._ball.render()
        self._UI.render()
        
    #@window.event
    def on_mouse_press(self,x, y, button, modifiers):
        #global pc
        if button & mouse.RIGHT:
            self._ball.reset(x,y)
            #pc=(x,y)
            

    def update(self, dt):
        args=SamplePoint.default_args
        
        if self._UI.settings.get_changed("K1"):
            
            args["K1"]=self._UI.settings.get_value("K1")
            self._space.reset()
            self._space_view.reset()
            #print(self._UI.settings.get_value("K1"))
        if self._UI.settings.get_changed("K2"):
            #print(self._UI.settings.get_value("K2"))
            args["K2"]=self._UI.settings.get_value("K2")
            self._space.reset()
            self._space_view.reset()
        self._ball.move(dt)
