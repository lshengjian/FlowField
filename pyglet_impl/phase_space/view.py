from abc import ABC, abstractmethod
from pyglet.math import Vec2
from pyglet import shapes,graphics
from .model import SamplePoint
from .utils import linear_gradient
from math import pi,atan
class SapceView:
    # PPM:int=80
    # R:int=8
    # CS:int =20
    def __init__(self,size:tuple,start:Vec2,end:Vec2):
        self._batch = graphics.Batch()
        self._size=size
        self._start=start
        self._end=end
        self._ps=[]
        self.kx=size[0]/(end.x-start.x)
        self.ky=size[1]/(end.y-start.y)
        self.R=min(self.kx,self.ky)*0.2
        #self._colors=linear_gradient('#0000FF','#FF0000',SapceView.CS)
        
        #self.circle = shapes.Circle(pos.x, pos.y, 10, color=(50, 225, 30), batch=self.batch)
    def add_point(self,sp:SamplePoint):
        x=(sp.position.x-self._start.x)*self.kx
        y=(sp.position.y-self._start.y)*self.ky
        rect=shapes.Rectangle(x, y,self.R ,1,color=(50, 45, 30),batch=self._batch)
        rect.rotation=sp.degree
        # a = -sp.angle+pi/2
        # n =round(a/pi*SapceView.CS)
        # if n>SapceView.CS-1:
        #     n=SapceView.CS-1
        # rect.color=self._colors[n]
        self._ps.append((sp,rect))
    
    def render(self):
        #self.circle.position=(p.x,p.y)
        self._batch.draw()
    
    def reset(self):
        for sp,rect in self._ps:
            rect.rotation=sp.degree

