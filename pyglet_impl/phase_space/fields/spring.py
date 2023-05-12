from ..core.field  import Field
from ..core.field import ArgInfo

class Spring(Field):

    def config_args(self):
        self.set_args([ArgInfo('a',4,0,6,1),ArgInfo('b',5,2,5,0.5)])
    
    def set_description(self):
        self.description="location : x | velocity: x' | x''+a.x'+b.x=0"
    
    def gradient(self,x:float,y:float):
        return self.arg_value('a')*y+self.arg_value('b')*x
        
