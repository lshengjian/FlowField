from math import pi
from pyglet import shapes
from ..core import *
from random import random,randint

class Pilot(View):
    

   
    def reset(self):
        super().reset()
        w,h=self._viewport.size
        
        ns=self.x_axis.num_sampling
        DX=self.x_axis.bound.distance/(ns-1)

       
        step=DX/10#self._field.arg_value('step')
        self._ps=[]
        for k in range(8):
            self.add_line(k, DX, step)

    def add_line(self,k,  DX, step):
        time_bound=self.x_axis.bound
        pos_bound=self.y_axis.bound
        dy=pos_bound.distance/8
        py=(pos_bound.low+dy*k)*0.618
        state=self._space.get_state_zero().set_data(0,py,0)
        c=(randint(0,255),randint(0,255),randint(0,255))
        t2=0
        dx=0
        while t2<time_bound.high:
            t1,y1,v1=state #time,pos,vol
            a1=self._space.constraint(state)
            t2=t1+step
            v2=v1+step*a1
            y2=y1+step*v2
            data=list(state)
            data[:3]=[t2,y2,v2]
            state=self._space.clone(state).set_data(*data)
            dx+=step
            if dx>=DX:
                dx=0
                x,y=self.get_pos(data[0],data[1])
                #print(t2,x,y)
                self._ps.append(shapes.Circle(x,y,2,color=c,batch=self._batch))





    


       

