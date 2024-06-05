from pyglet.window import mouse,Window,key
from pyglet import clock
from .space import Space

from .utils import load_config,get_config
from .ui import UI
from .views import Tip,Grid,History,Viewport,Point,Size

class App(Window):
    def __init__(self):
        self._case_idx=0
        self._demo_names=load_config()
        cfg=get_config(self._demo_names[0])
        w,h=cfg['WIDTH'],cfg['HEIGHT']
        super().__init__(w,h , cfg['TITLE'], resizable=False)
        self.set_vsync(False)
        clock.schedule_interval(self.update, 1/cfg['FPS'])
        
        self.reset()
        
       
 
        
    def on_draw(self):
        self.clear()
        for  v in self._views:
            v.render()
        self._UI.render()
        
    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        flag=False
        if symbol==key.LEFT or symbol==key.UP :
            self._case_idx+=len(self._demo_names)-1
            flag=True
        elif symbol==key.RIGHT or symbol==key.DOWN:
            self._case_idx+=1
            flag=True
        if flag:
            self._case_idx%= len(self._demo_names)
            self.reset()
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button & mouse.RIGHT:
            self._views[0].on_click(x,y)


            
    def reset(self):
        self.reload=False
        cfg=get_config(self._demo_names[self._case_idx])
        self._cfg=cfg
        space=Space(cfg)
        self._space=space
        self._views=[Grid(space),Tip(space)]
        trajectory=cfg.get('trajectory',False)
        if trajectory:
            w,h=cfg['WIDTH'],cfg['HEIGHT']
            self._views.append(History(space,viewPort=Viewport(Point(w/2,0),Size(w/2,h/2))))
        
        self._UI = UI(self, cfg,'Setup')
        

    def update(self, dt):
        if self.reload:
            self.reset()
            return
        self._space.update()
        for key,_ in self._cfg.args.items():
            if self._UI.settings.get_changed(key):
                self._cfg.args[key][1]=self._UI.settings.get_value(key)
                self.reload=True
                #print(self._UI.settings.get_value(key))



