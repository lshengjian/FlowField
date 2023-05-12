# from math import pi
# from pyglet import shapes
# from ..core import SamplePoint,Field
# from .config import WIDTH,HEIGHT
# from ..core.view import View

# class Line(View):
#     def __init__(self,field:Field,x0:float=0):
#         super().__init__(field)
#         #self._body=shapes.Circle(0, 0,6,color=(255, 25, 13),batch=self._batch)
#         dx,_=field.size
#         self._k1=WIDTH/100
#         self._k2=HEIGHT/dx
#         self.x0=x0
#         self.lines=[]
#         self.reset()
   
         
    


#     def reset(self):
#         sp:SamplePoint= SamplePoint(self._field,self.x0,0) 
#         self.lines.append(shapes.Circle(0, (sp.x-self._field.x_axis.bound.low)*self._k2,2,color=(255, 255, 255),batch=self._batch))
#         for  t in range(1,100):
#             sp.update()
#             self.lines.append(shapes.Circle(t*self._k1,(sp.x-self._field.x_axis.bound.low)*self._k2,2,color=(255, 255, 255),batch=self._batch))
       


