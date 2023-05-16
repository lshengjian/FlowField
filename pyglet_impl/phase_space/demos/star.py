from ..core.space  import Space
from ..core.space import ArgInfo

class Star(Space):

    def config_args(self):
        self.set_args([ArgInfo('a',2,1,6,0.1),ArgInfo('k',2,1,6,0.1)])
    
    def set_description(self):
        self.description='velocity: v | dv/dt=a+x-kv'
    
    def constraint(self,x:float,y:float):
        return self.arg_value('a')+x-self.arg_value('k')*y
        

# def F1(p:Vec2,time:float,args:Dict[str,float]):
#   return 1+p.x-p.y


# def F2(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return x**2-y**2


# def F3(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return -args['K1']*sin(x)-args['K2']*y