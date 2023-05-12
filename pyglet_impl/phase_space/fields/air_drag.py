from ..core.field  import Field
from ..core.field import ArgInfo

class AirDrag(Field):

    def config_args(self):
        self.set_args([ArgInfo('a',10,1,10,0.1),ArgInfo('k',2,1,3,0.1)])
    
    def set_description(self):
        self.description='velocity: v | dv/dt=a-kv'
    
    def gradient(self,x:float,y:float):
        return self.arg_value('a')-self.arg_value('k')*y
        
