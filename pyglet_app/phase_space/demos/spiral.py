from ..core.space  import Space,ArgInfo
from ..core import State
from math import sin,cos,log
class Spiral(Space):

    def config_args(self):
        self.set_args([ArgInfo('k',2,1,3,0.1,'k:scale'),ArgInfo('r',0,0,3,0.1,'r:init ridus')])
        self.description='time:t,x,y,z | z=k.t,R=r+ln(1+z) x=R.cos(t) y=R.sin(t)'
    
       
    
    def constraint(self,s:State):
        t,x,y,z=s
        z=self.arg_value('k')*t
        R=self.arg_value('r')+log(1+z)
        x=R*cos(t)
        y=R*sin(t)
        s.set_data(t,x,y,z)