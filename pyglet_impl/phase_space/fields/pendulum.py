from ..core.field  import Field
from ..core.field import ArgInfo
from math import sin
class Pendulum(Field):

    def config_args(self):
        self.set_args([ArgInfo('a',2,1,5,0.2),ArgInfo('b',1,0,3,0.2)])
    
    def set_description(self):
        self.description="angle : q | velocity: q' | q''=-a.sin(q)-b.q'"
    
    def gradient(self,x:float,y:float):
        return -self.arg_value('a')*sin(x)-self.arg_value('b')*y
        

# def F1(p:Vec2,time:float,args:Dict[str,float]):
#   return 1+p.x-p.y


# def F2(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return x**2-y**2


# def F3(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return -args['K1']*sin(x)-args['K2']*y