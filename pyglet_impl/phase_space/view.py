#from abc import ABC, abstractmethod
from typing import Tuple
from pyglet import shapes,graphics
from phase_space.core import VelocityDemo,Measure
from phase_space.utils import linear_gradient,Bound
from math import pi,atan

class SapceView:
    # PPM:int=80
    # R:int=8
    CS:int = 8
    def __init__(self,size:tuple):
        self._batch = graphics.Batch()
        self._size=size
        self._colors=linear_gradient('#0000FF','#FF0000',SapceView.CS)
        m1=Measure('time',Bound(0,10),11)
        m2=Measure('velocity',Bound(3,7),11)
        self.demo=VelocityDemo(m1,m2)

        self.kx=size[0]/m1.bound.distance
        self.ky=size[1]/m2.bound.distance
        self.R=min(self.kx,self.ky)*0.2
        self._ps=[]
        for p in self.demo:
            self.add_point(p)


        
        
        #self.circle = shapes.Circle(pos.x, pos.y, 10, color=(50, 225, 30), batch=self.batch)
    def add_point(self,sp:Tuple):
        px=self.demo._xs.get_position(sp[0])
        py=self.demo._ys.get_position(sp[1])
        x=(px-self.demo._xs.bound.low)*self.kx
        y=(py-self.demo._ys.bound.low)*self.ky
        rect=shapes.Rectangle(x, y,self.R ,3,color=(50, 45, 30),batch=self._batch)
        rect.anchor_position=(rect.width/2,rect.height/2)
        c=shapes.Circle(x, y,2,color=(5, 245, 13),batch=self._batch)
        self.set_color(sp, rect)
        self._ps.append((c,rect))
    
    def render(self):
        #self.circle.position=(p.x,p.y)
        self._batch.draw()
    
    def reset(self):
        pass
        # for sp,rect in self._ps:
        #     self.set_color(sp, rect)

    def set_color(self, sp, rect):
        a = -atan(sp[2])
        d= a*180.0/pi
        rect.rotation=d
        a = -a+pi/2
        n =round(a/pi*SapceView.CS)
        if n>SapceView.CS-1:
            n=SapceView.CS-1
        rect.color=self._colors[n]


class Ball: #pendulum
    def __init__(self,size:tuple):
        self._size=size
        # self._start=start
        # self._end=end
        # self._sp=sp
        # self.kx=size[0]/(end.x-start.x)
        # self.ky=size[1]/(end.y-start.y)
        # x=(sp.position.x-self._start.x)*self.kx
        # y=(sp.position.y-self._start.y)*self.ky
        # self.circle = shapes.Circle(x, y, 5, color=(255, 255, 30))
        # self.rope=shapes.Rectangle(size[0]/2,size[1]-100,6,200,color=(255, 255, 244))
        # self.rope.anchor_x=self.rope.width/2
        # self.rope.anchor_y=self.rope.height
        # self.rope.rotation=-sp.position.x/pi*180

    def move(self,dt:float):
        self._sp.move(dt)
        self._sp.update()
        x=(self._sp.position.x-self._start.x)*self.kx
        y=(self._sp.position.y-self._start.y)*self.ky
        self.circle.position=(x,y)
        self.rope.rotation=-self._sp.position.x/pi*180

    def reset(self,x,y):
        self.circle.position=(x,y)
        x=x/self.kx+self._start.x
        y=y/self.ky+self._start.y
        self._sp.reset(x,y)



    def render(self):
        self.circle.draw()
        self.rope.draw()
