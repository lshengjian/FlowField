from math import atan,pi
from .data_def import Vector
from .view import View

class SamplePoint:

    def __init__(self,v:View,data:Vector):
        self._state:Vector=data
        self._view:View=v
        self._field=v._field
        self.update()

    # def reset(self,data:Vector):
    #     self._state=data
        

    # def __str__(self):
    #     return f"({self._data.x:.2f},{self._data.y:.2f})"
    
    def _update1(self,step):#step is dx
        slop=self._field.constraint
        x1=self._state.get_value(self._view.x_axis.name)
        y1=self._state.get_value(self._view.y_axis.name)
        s1=slop(self._state)
        x2,y2=x1+step,y1+step*s1
        state=self._field.get_state_zero()
        state.set_value(self._view.x_axis.name,x2)
        state.set_value(self._view.y_axis.name,y2)                
        s2=slop(state)
        x3,y3=x2+step,y2+step*s2
        state.set_value(self._view.x_axis.name,x3)
        state.set_value(self._view.y_axis.name,y3) 
        s3=slop(state)
        x4,y4=x3+step,y3+step*s3
        state.set_value(self._view.x_axis.name,x4)
        state.set_value(self._view.y_axis.name,y4) 
        s4=slop(state)
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step,y1+step*s

    def _update2(self,step):#step is delta_time
        slop=self._field.constraint
        x1=self._state.get_value(self._view.x_axis.name)
        y1=self._state.get_value(self._view.y_axis.name)
        
        s1=slop(self._state)
        x2,y2=x1+step*y1,y1+step*s1
        state=self._field.get_state_zero()
        state.set_value(self._view.x_axis.name,x2)
        state.set_value(self._view.y_axis.name,y2)  
        s2=slop(state)
        x3,y3=x2+step*y2,y2+step*s2
        state.set_value(self._view.x_axis.name,x3)
        state.set_value(self._view.y_axis.name,y3) 
        s3=slop(state)
        x4,y4=x3+step*y3,y3+step*s3
        state.set_value(self._view.x_axis.name,x4)
        state.set_value(self._view.y_axis.name,y4)
        s4=slop(state)
        
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step*y1,y1+step*s
    
    def update(self):
        step:float=self._field.arg_value('step')
       
        x,y=0,0
        if not self._field.isTwoOrder:
            x,y=self._update1(step)
        else:
            x,y=self._update2(step)
        x,y=self._field.limit([x,y])
        self._state.set_data(x,y)


    @property
    def state(self):
        return self._state
  

    @property
    def degree(self):
        x,y=self._state.get_value(self._view.x_axis.name,self._view.y_axis.name)
        a = -atan(self._field.constraint(x,y)) #todo
        return a*180.0/pi