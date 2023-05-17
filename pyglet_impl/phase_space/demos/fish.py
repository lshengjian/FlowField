from ..core.space  import Space,ArgInfo

class Fish(Space):
    def config_args(self):
        self.set_args([
            ArgInfo('a',5,3,5,0.1,'Reproductive Rate'),
            ArgInfo('b',1,0.5,2,0.1,'Resource Limits'),
            ArgInfo('h',0.1,0,1.0,0.1,'Harvest')
        ])


    def constraint(self,state):
        t,y=state
        return self.arg_value('a')*y-self.arg_value('b')*y*y-self.arg_value('h')
        
    def set_description(self):
        self.description='fish amount: y | dy/dt=ay-by^2-h'

