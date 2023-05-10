from math import atan,pi

from .field import Field

class SamplePoint:
    #default_args:Dict[str,float]={'K1':2.0,'K2':1}

    def __init__(self,f:Field,x,y):
        self._x=x
        self._y=y
        self._field=f
        self.update()

    def reset(self,x,y):
        self._x=x
        self._y=y
        



    def __str__(self):
        return f"({self._pos.x:.2f},{self._pos.y:.2f})"
    
    def _update1(self,step):#step is dx
        slop=self._field.gradient
        x1,y1=self._x,self._y
        s1=slop(x1,y1)
        x2,y2=x1+step,y1+step*s1
        s2=slop(x2,y2)
        x3,y3=x2+step,y2+step*s2
        s3=slop(x3,y3)
        x4,y4=x3+step,y3+step*s3
        s4=slop(x4,y4)
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step,y1+step*s

    def _update2(self,step):#step is delta_time
        slop=self._field.gradient
        x1,y1=self._x,self._y
        s1=slop(x1,y1)
        x2,y2=x1+step*y1,y1+step*s1
        s2=slop(x2,y2)
        x3,y3=x2+step*y2,y2+step*s2
        s3=slop(x3,y3)
        x4,y4=x3+step*y3,y3+step*s3
        s4=slop(x4,y4)
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step*y1,y1+step*s
    
    def update(self):
        step:float=self._field.arg_value('step')
        x,y=0,0
        if not self._field.isTwoOrder:
            x,y=self._update1(step)
        else:
            x,y=self._update2(step)
        self._x,self._y=self._field.force(x,y)


    @property
    def position(self):
        return (self._x,self._y)
  

    @property
    def degree(self):
        a = -atan(self._field.gradient(self._x,self._y))
        return a*180.0/pi