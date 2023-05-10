from ..core.field  import Field
from ..core.field import ArgInfo

class AirDrag(Field):

    def config_args(self):
        self.set_args([ArgInfo('a',10,1,10,0.1),ArgInfo('k',2,1,3,0.1)])
    
    def set_description(self):
        self.description='fall velocity: v | dv/dt=a-kv'
    
    def gradient(self,x:float,y:float):
        return self.arg_value('a')-self.arg_value('k')*y
        

# def F1(p:Vec2,time:float,args:Dict[str,float]):
#   return 1+p.x-p.y


# def F2(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return x**2-y**2


# def F3(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return -args['K1']*sin(x)-args['K2']*y