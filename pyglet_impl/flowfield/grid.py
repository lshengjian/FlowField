from .view import BaseView
from pyglet import shapes,graphics
class Grid(BaseView):
    def __init__(self,left,top,w,h,xbounds,ybounds,ns):
        super().__init__(left,top,w,h,xbounds,ybounds)
        self.ps={}
        dy=h/(ns[0]+1)
        dx=w/(ns[1]+1)
        R=min(dx,dy)*0.618
        self.batch = graphics.Batch()
        self.circle = shapes.Circle(20, 20, 10, color=(50, 225, 30), batch=self.batch)
        for r in range(ns[0]):
            for c in range(ns[1]):
                x=left+(c+1)*dx
                y=top+(r+1)*dy
                self.ps[(r,c)]=shapes.Rectangle(x,y,R,1,color=(50, 225, 30),batch=self.batch)
                #shapes.Line(x=x,y=y, x2=x+R,y2=y, color=(50, 225, 30),batch=self.batch)

   
    def draw(self):
        line:shapes.Rectangle=self.ps[(2,1)]
        line.color=(255,0,0)
        line.rotation =-90
        
        self.batch.draw()