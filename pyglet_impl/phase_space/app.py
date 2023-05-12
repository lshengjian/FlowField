from pyglet.window import mouse,Window,key
from pyglet import clock
from .core import *
from .fields import *
from .views import *
from .ui import UI
from typing import Dict,List

class App(Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Phase Space View (by alex)", resizable=False)
        self.set_vsync(False)
        clock.schedule_interval(self.update, 1/FPS)
        self._case_idx=0
        self.CASES:List[Field]=[FALL,FISH,PENDULUM]
        self.VIEWS:Dict[str,List[View]]={
            'AirDrag':[Grid(FALL),Ball(FALL)],
            'Fish':[Grid(FISH),Ball(FISH)],
            'Pendulum':[Grid(PENDULUM),Ball(PENDULUM),Pole(PENDULUM)]
        }
        self.reset()
        
      
        
    def on_draw(self):
        self.clear()
        for  v in self.VIEWS[self._field.name]:
            v.render()
        self._UI.render()
        
    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        if symbol==key.LEFT or symbol==key.UP :
            self._case_idx+=len(self.CASES)-1
        elif symbol==key.RIGHT or symbol==key.DOWN:
            self._case_idx+=1
        self._case_idx%= len(self.CASES)
        self.reset()
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button & mouse.RIGHT:
            px,py=self.VIEWS[self._field.name][1].get_space_pos(x,y)
            self._sp.reset(px,py)

            
    def reset(self):
        self._field=self.CASES[self._case_idx]
        self._field.reset()
        self._sp=SamplePoint(self._field,0,0)
        for  v in self.VIEWS[self._field.name]:
            v.reset()
        self._UI = UI(self, self._field, "Config",  "Set Parameters")
        

    def update(self, dt):
        self._sp.update()
        for  v in self.VIEWS[self._field.name]:
            v.moveto(self._sp)

        for key,arg in self._field._args.items():
            if self._UI.settings.get_changed(key):
                arg.value=self._UI.settings.get_value(key)
                if key!='step':
                    self.reset()


