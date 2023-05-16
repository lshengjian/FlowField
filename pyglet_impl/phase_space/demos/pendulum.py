from ..core.space  import Space,ArgInfo
from math import sin

class Pendulum(Space):

    def config_args(self):
        self.set_args([ArgInfo('a',2,1,5,0.2),ArgInfo('b',1,0,3,0.2)])
    
    def set_description(self):
        self.description="angle : q | velocity: q' | q''=-a.sin(q)-b.q'"
    
    def constraint(self,x:float,y:float,z:float=0):
        return -self.arg_value('a')*sin(x)-self.arg_value('b')*y
        

