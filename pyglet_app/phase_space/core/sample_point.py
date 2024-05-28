from math import atan,pi
from .state import State
from .space import Space
from .view import View

class SamplePoint:

    def __init__(self,view:View):
        self._space:Space=view._space
        self._x_index:int=view._space.get_index(view.x_axis.name)
        self._y_index:int=view._space.get_index(view.y_axis.name)
        self._state:State=State(view._space.names)
        data=list(self._state)
        x=view._space.get_measure(self._space.names[self._x_index])
        y=view._space.get_measure(self._space.names[self._y_index])
        data[self._x_index]=x.bound.low+x.bound.distance/2
        data[self._y_index]=y.bound.low+x.bound.distance/2
        self._state.set_data(*data)
        self._measure_x=x
        self._measure_y=y

        
        
        self.update()

      

    # def __str__(self):
    #     return f"({self._data.x:.2f},{self._data.y:.2f})"
    
    def _update1(self,step):#step is dx
        CS=self._space.constraint
        state=self._state
        data=list(state)
        x1=data[self._x_index]
        y1=data[self._y_index]
        s1=CS(state)
        x2,y2=x1+step,y1+step*s1
        data[self._x_index]=x2
        data[self._y_index]=y2
        state.set_data(*data)
        s2=CS(state)
        x3,y3=x2+step,y2+step*s2
        data[self._x_index]=x3
        data[self._y_index]=y3
        state.set_data(*data)
        s3=CS(state)
        x4,y4=x3+step,y3+step*s3
        data[self._x_index]=x4
        data[self._y_index]=y4
        state.set_data(*data) 
        s4=CS(state)
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step,y1+step*s

    def _update2(self,step):#step is delta_time
        CS=self._space.constraint
        state=self._state
        data=list(state)
        x1=data[self._x_index]
        y1=data[self._y_index]
        s1=CS(self._state)
        x2,y2=x1+step*y1,y1+step*s1
        data[self._x_index]=x2
        data[self._y_index]=y2
        state.set_data(*data)  
        s2=CS(state)
        x3,y3=x2+step*y2,y2+step*s2
        data[self._x_index]=x3
        data[self._y_index]=y3
        state.set_data(*data)
        s3=CS(state)
        x4,y4=x3+step*y3,y3+step*s3
        data[self._x_index]=x4
        data[self._y_index]=y4
        state.set_data(*data)
        s4=CS(state)
        
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step*y1,y1+step*s
    
    def update(self):
        step:float=self._space.arg_value('step')
        x,y=0,0
        if  self._space._isFirstOrder:
            x,y=self._update1(step)
        else:
            x,y=self._update2(step)
        #x,y=self._space.limit([x,y])
        data=list(self._state)
        data[self._x_index]=self._measure_x.bound.limit(x,False)
        data[self._y_index]=self._measure_y.bound.limit(y,False)
        self._state.set_data(*data)


    @property
    def state(self):
        return self._state
  

    # @property
    # def degree(self):
    #     #x=self._state[self._x_index]
    #     #y=self._state[self._y_index]
    #     a = -atan(self._space.constraint(self._state)) #todo
    #     return a*180.0/pi