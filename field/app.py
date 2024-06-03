from pyglet.window import mouse,Window,key
from pyglet import clock
from .space import Space
from .tip import Tip
from .utils import load_config,get_config
from .ui import UI

class App(Window):
    def __init__(self):
        self.reset() 

        
    # def select_space(self):
    #     name=self.demo_names[self._case_idx]
    #     self.space,self.views=self.cfg['make_views'](name)
    #     self.reset()     
        
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
        #self.select_space()
        
    def on_mouse_press(self,x, y, button, modifiers):
        if button & mouse.RIGHT:
            print('mouse press')
            #self.views[0].on_click(x,y)

    def ui_callback(self,name):
        #print(name)
        self.cfg=get_config(name)
        self._UI = UI(self,self.ui_callback, self.demo_names,self.cfg, name,  "Set Parameters")
        # self._case_idx=self.demo_names.index(name)
        # self.select_space()

            
    def reset(self):
        self.demo_names=load_config()
        cfg=get_config(self.demo_names[0])
        self.cfg=cfg
        w,h=cfg['WIDTH'],cfg['HEIGHT']
        super().__init__(w,h , cfg['TITLE'], resizable=False)
        self.set_vsync(False)
        clock.schedule_interval(self.update, 1/cfg['FPS'])
        #self._case_idx=0
        self.views=[Tip(space=Space(cfg))]
        
        
        self._UI = UI(self,self.ui_callback, self.demo_names,cfg,self.demo_names[0],  "Set Parameters")
        

    def update(self, dt):
        # for  v in self.views:
        #     v.update()

        for key,_ in self.cfg.args.items():
            if self._UI.settings.get_changed(key):
                print(self._UI.settings.get_value(key))
            #self.reset()


