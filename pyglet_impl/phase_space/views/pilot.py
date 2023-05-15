from math import pi
from pyglet import shapes
from ..core import *
from random import random,randint

class Pilot(View):
    
    def __init__(self,field:Field,viewport:Viewport=default_viewport,bg_color=None):
        super().__init__(field,viewport,bg_color)
   
    def reset(self):
        super().reset()
        w,h=self._viewport.size
        ox,oy=self._viewport.start
        xb,yb=self._field.measures[0].bound,self._field.measures[1].bound
        kx=w/xb.distance
        ky=h/yb.distance
        lx,ly=xb.low,yb.low
        self._ox,self._oy=ox,oy
        self._kx,self._ky=kx,ky
        self._lx,self._ly=lx,ly
        self.w,self.h=w,h
        time_bound=xb
        pos_bound=yb
        ns=self._field.measures[0].num_sampling
        DX=time_bound.distance/(ns-1)

       
        step=DX/10#self._field.arg_value('step')
        self._ps=[]
        for k in range(8):
            self.add_line(k,time_bound, pos_bound, DX, step)

    def add_line(self,k, time_bound, pos_bound, DX, step):
        dy=pos_bound.distance/8
        py=(pos_bound.low+dy*k)*0.618
        state=State(0,py,0)
        c=(randint(0,255),randint(0,255),randint(0,255))
        t2=0
        dx=0
        while t2<time_bound.high:
            t1,y1,v1=state #time,pos,vol
            a1=self._field.constraint(t1,y1,v1)
            t2=t1+step
            v2=v1+step*a1
            y2=y1+step*v2
            state=State(t2,y2,v2)
            dx+=step
            if dx>=DX:
                dx=0
                x,y=self.get_pos(state.x,state.y)
                #print(t2,x,y)
                self._ps.append(shapes.Circle(x,y,2,color=c,batch=self._batch))





    


       

