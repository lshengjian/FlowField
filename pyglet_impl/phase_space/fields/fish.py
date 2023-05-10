from ..core.field  import Field
from ..core.field import ArgInfo

class Fish(Field):
    def config_args(self):
        self.set_args([
            ArgInfo('a',4,1,5,0.5),
            ArgInfo('b',2,0.5,3,0.5),
            ArgInfo('h',0.3,0.1,3,0.5)
        ])


    def gradient(self,x:float,y:float):
        return self.arg_value('a')*y-self.arg_value('b')*y*y-self.arg_value('h')
        
    def set_description(self):
        self.description='fish amount: y | dy/dt=ay-by^2-h'

