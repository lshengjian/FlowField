from ..core  import Space,ArgInfo,State

class Spring(Space):

    def config_args(self):
        self.set_args([ArgInfo('a',4,0,6,0.2,'Spring strength'),ArgInfo('b',5,2,5,0.5,'damp')])
    
    def set_description(self):
        self.description="|time:t|pos:x|velocity:v| &  v'+a.v+b.x=0"
    
    def constraint(self,state:State):#time,pos,vol
        return -self.arg_value('a')*state.velocity-self.arg_value('b')*state.pos
        
