from pyglet.window import mouse,Window,key
from pyglet import clock
from .core import *
from .demos import *
from .views import *
from .ui import UI

class App(Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Phase Space View (by alex)", resizable=False)
        self.set_vsync(False)
        clock.schedule_interval(self.update, 1/FPS)
        self._case_idx=0
        self.views=get_views()
        
        self.reset()
        
      
        
    def on_draw(self):
        self.clear()
        for  v in self.views[self._field._name]:
            v.render()
        self._UI.render()
        
    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        if symbol==key.LEFT or symbol==key.UP :
            self._case_idx+=len(CASES)-1
        elif symbol==key.RIGHT or symbol==key.DOWN:
            self._case_idx+=1
        self._case_idx%= len(CASES)
        self.reset()
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button & mouse.RIGHT:
            self.grid.on_click(x,y)
            
            # px,py=.get_space_pos(x,y)
            # self._sp.reset(State(px,py,0))

            
    def reset(self):
        self._field=CASES[self._case_idx]
        self._field.reset()
        self.grid=self.views[self._field._name][0]

        for  v in self.views[self._field._name]:
            v.reset()
        self._UI = UI(self, self._field, "Config",  "Set Parameters")
        

    def update(self, dt):
        for  v in self.views[self._field._name]:
            v.update()

        for key,arg in self._field._args.items():
            if self._UI.settings.get_changed(key):
                arg.value=self._UI.settings.get_value(key)
                if key!='step':
                    self.reset()


