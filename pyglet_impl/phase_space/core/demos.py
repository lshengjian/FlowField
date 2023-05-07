from .field  import Field
from .field import ArgInfo

class VelocityDemo(Field):
    def config_args(self):
        a1=ArgInfo('a',10,1,10,0.1)
        a2=ArgInfo('k',2,1,3,0.1)
        self._args={
            a1.name:a1,
            a2.name:a2
        }

    def slop(self,x:float,y:float):
        return self._args['a'].value-self._args['k'].value*y
        

# def F1(p:Vec2,time:float,args:Dict[str,float]):
#   return 1+p.x-p.y


# def F2(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return x**2-y**2


# def F3(p:Vec2,time:float,args:Dict[str,float]):
#   x,y=p.x,p.y
#   return -args['K1']*sin(x)-args['K2']*y