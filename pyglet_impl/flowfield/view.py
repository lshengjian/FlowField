#from abc import ABC, abstractmethod

class BaseView:
    
    def __init__(self,left,top,w,h,xbounds,ybounds):
        self.left,self.top=left,top
        self.width,self.height=w,h
        self.xs=xbounds
        self.ys=ybounds

    def get_position(self,x,y):
        if x<self.xs[0]:
            x=self.xs[0]
        elif x>self.xs[1]:
            x=self.xs[1]
        if y<self.ys[0]:
            y=self.ys[0]
        elif y>self.ys[1]:
            y=self.ys[1]
        x=self.left+(x-self.xs[0])/(self.xs[1]-self.xs[0])*self.width
        y=self.height-(y-self.ys[0])/(self.ys[1]-self.ys[0])*self.height
        return round(x),round(y)
    
    def update(self, dt):
        pass

   
    def draw(self):
        pass
