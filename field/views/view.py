from abc import ABC, abstractmethod
from pyglet import graphics
from ..space import Space
from dataclasses import dataclass

@dataclass
class Point:
    x:int
    y:int
    def __iter__(self):
        yield from [self.x,self.y]
@dataclass
class Size:
    width:int
    height:int  

    def __iter__(self):
        yield from [self.width,self.height]
@dataclass   
class Viewport:
    start:Point
    size:Size

class View(ABC):
    def __init__(self,space:Space,viewPort:Viewport=None):
        #self._batch = graphics.Batch()
        self._space:Space=space
        self._batch = graphics.Batch()
        cfg=self.cfg=space.cfg
        self.w,self.h=cfg['WIDTH'],cfg['HEIGHT']
        if viewPort is None:
            self._viewport=Viewport(Point(0,0),Size(self.w,self.h))
        else:
            self._viewport=viewPort
        ox,oy=self._viewport.start
        kx=self.w/(space.x_limit[1]-space.x_limit[0])
        ky=self.h/(space.y_limit[1]-space.y_limit[0])
        lx,ly=space.x_limit[0],space.y_limit[0]
        self._ox,self._oy=ox,oy
        self._kx,self._ky=kx,ky
        self._lx,self._ly=lx,ly
        self.reset()


    def on_click(self,sx,sy):
        pass

    # @abstractmethod  
    # def update(self):
    #     pass
    
    @abstractmethod  
    def reset(self):
        pass
        

    def render(self):
        self._batch.draw()
    
    def get_space_pos(self,screen_x,screen_y):
        x=(screen_x-self._ox)/self._kx+self._lx
        y=(screen_y-self._oy)/self._ky+self._ly
        return x,y

    def get_screen_pos(self,x,y):
        sx=self._ox+(x-self._lx)*self._kx
        sy=self._oy+(y-self._ly)*self._ky
        return int(sx),int(sy)


