from ..core.space  import Space,ArgInfo,State
from math import sin

class Pendulum(Space):

    def config_args(self):
        self.set_args([ArgInfo('a',2,1,5,0.2),ArgInfo('b',1,0,3,0.2)])
    
    def set_description(self):
        self.description="angle : q | velocity: q' | q''=-a.sin(q)-b.q'"
    
    def constraint(self,state:State):
        x,y=state
        return -self.arg_value('a')*sin(x)-self.arg_value('b')*y
        
