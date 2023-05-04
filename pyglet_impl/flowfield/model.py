import math
class Model:
    def __init__(self,x1,x2,y1,y2):
        self.theta_range=(x1,x2)
        self.omiga_range=(y1,y2)
        self.theta=(x1+x2)/2
        self.omiga=(y1+y2)/2
        self.L=0.5 #单摆长度
        self.K=0.2 #空气阻力系数

    def init_data(self,t,w):
        self.theta=t
        self.omiga=w

    def dw_dt(self):
        return -math.sqrt(9.8/self.L)*self.theta-self.K*self.omiga


