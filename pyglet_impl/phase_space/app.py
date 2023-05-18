from pyglet.window import mouse,Window,key
from pyglet import clock
from .core import *

from .views import *
from .ui import UI

class App(Window):
    def __init__(self,CFG):
        self.CFG=CFG
        
        w,h=CFG['WIDTH'],CFG['HEIGHT']
        super().__init__(w,h , "Phase Space View (by alex)", resizable=False)
        self.set_vsync(False)
        clock.schedule_interval(self.update, 1/FPS)
        self._case_idx=0
        self.demo_names:List[str]=CFG['demo_names']
        self.select_space()
        
    def select_space(self):
        name=self.demo_names[self._case_idx]
        self.space,self.views=self.CFG['make_views'](name)
        self.reset()     
        
    def on_draw(self):
        self.clear()
        #name=self.demo_names[self._case_idx]
        for  v in self.views:
            v.render()
        self._UI.render()
        
    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        if symbol==key.LEFT or symbol==key.UP :
            self._case_idx+=len(self.demo_names)-1
        elif symbol==key.RIGHT or symbol==key.DOWN:
            self._case_idx+=1
        self._case_idx%= len(self.demo_names)
        self.select_space()
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button & mouse.RIGHT:
            self.views[0].on_click(x,y)

    def ui_callback(self,name):
        self._case_idx=self.demo_names.index(name)
        self.select_space()

            
    def reset(self):
        self.space.reset()
        for  v in self.views:
            v.reset(self.CFG)
        self._UI = UI(self,self.ui_callback, self.demo_names,self.space, "Config",  "Set Parameters")
        

    def update(self, dt):
        for  v in self.views:
            v.update()

        for key,arg in self.space._args.items():
            if self._UI.settings.get_changed(key):
                arg.value=self._UI.settings.get_value(key)
                self.reset()


