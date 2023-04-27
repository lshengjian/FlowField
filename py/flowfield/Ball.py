from typing import Callable

class Ball:
    #pos:complex=complex(0,0)
    def __init__(self,x0:float,y0:float,x1=-1,x2=1):
        self.pos=complex(x0,y0)
        self.x1=x1
        self.x2=x2

    def move(self,slop:Callable[[complex], float],step:float=0.1):
        x,y=self.pos.real,self.pos.imag
        if x>self.x2:
            x=self.x1
        if x<self.x1:
            x=x2
        s1=slop(self.pos)
        x2,y2=x+step,y+step*s1
        s2=slop(complex(x2,y2))
        x3,y3=x2+step,y2+step*s2
        s3=slop(complex(x3,y3))
        x4,y4=x3+step,y3+step*s3
        s4=slop(complex(x4,y4))
        s=(s1+s4+2*(s2+s3))/6.0
        self.pos=complex(x+step,y+step*s)

    def reset(self,x,y):
        self.pos=complex(x,y)
