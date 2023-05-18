from ..core  import Space,ArgInfo,State

class Spring(Space):

    def config_args(self):
        self.set_args([ArgInfo('b',4,0.1,6,0.2,'b:Spring strength'),ArgInfo('k',0,0,5,0.5,'k:damp')])
        self.description="t:time x:pos v:velocity |  v'+k.v+b.x=0"
    
       
    
    def constraint(self,state:State):#time,pos,vol
        return -self.arg_value('k')*state.velocity-self.arg_value('b')*state.pos
        
