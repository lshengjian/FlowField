from ..core.space  import Space,ArgInfo
from ..core import State
class Fall(Space):

    def config_args(self):
        self.set_args([ArgInfo('a',10,1,10,0.1,'acc'),ArgInfo('k',2,1,3,0.1,'dump')])
    
    def set_description(self):
        self.description='|time:t|velocity:v| & dv/dt=a-kv'
    
    def constraint(self,xs:State):
        return self.arg_value('a')-self.arg_value('k')*xs.velocity
        
