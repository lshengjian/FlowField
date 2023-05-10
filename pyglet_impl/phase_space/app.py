from pyglet.window import mouse,Window,key
from typing import List
from pyglet import clock
from .core import *
from .views.config import *
from .ui import UI

from .views.grid import Grid
from .views.ball import Ball

class App(Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Flow Field Demo(by alex)", resizable=False)
        self.set_vsync(False)
        clock.schedule_interval(self.update, 1/FPS)
        self._fields:List[Field]=show_cases
        self._case_idx=0
        self.reset()

        

        
        
    def on_draw(self):
        self.clear()
        #self._fps_display.draw()
        self._grid.render()
        self._ball.render()
        self._UI.render()
        
    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        if symbol==key.LEFT or symbol==key.UP :
            self._case_idx+=len(self._fields)-1
        elif symbol==key.RIGHT or symbol==key.DOWN:
            self._case_idx+=1
        self._case_idx%= len(self._fields)
        self.reset()
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button & mouse.RIGHT:
            px,py=self._ball.get_screen_pos(x,y)
            self._sp.reset(px,py)
            self._ball.moveto(self._sp)
            
    def reset(self):
        self._field=self._fields[self._case_idx]
        self._field.reset()
        self._grid=Grid(self._field,WIDTH, HEIGHT)
        self._sp=SamplePoint(self._field,0,4)
        self._ball=Ball(self._field)
        self._UI = UI(self, self._field, "Config",  "Set Parameters")
        

    def update(self, dt):
        self._sp.update()
        self._ball.moveto(self._sp)
        for key,arg in self._field._args.items():
            if self._UI.settings.get_changed(key):
                arg.value=self._UI.settings.get_value(key)
                if key!='step':
                    self.reset()


