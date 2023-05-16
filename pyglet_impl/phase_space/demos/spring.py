from ..core.space  import Space,ArgInfo

class Spring(Space):

    def config_args(self):
        self.set_args([ArgInfo('a',4,0,6,0.2),ArgInfo('b',5,2,5,0.5)])
    
    def set_description(self):
        self.description="|time:t|pos:x|velocity:v| &  v'+a.v+b.x=0"
    
    def constraint(self,t:float,pos:float,vol:float=0):#time,pos,vol
        return -self.arg_value('a')*vol-self.arg_value('b')*pos
        
