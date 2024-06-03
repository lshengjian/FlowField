

from pyglet.text import Label
from .view import View
class Tip(View):
    
    def reset(self):
        super().reset()
        #cfg=self.cfg
        w,h=self.w,self.h

        self._tips=[
            Label('TIP: ',font_size=20,color=(0,255,8,210),x=20,y=64,batch=self._batch),
            Label('arrow key show next case',font_size=18,color=(5,235,28,210),x=20,y=44,batch=self._batch),
            Label('right mouse reset the ball',font_size=18,color=(5,235,28,210),x=20,y=24,batch=self._batch)
        ]
        
        self._name=Label(self._space.x_name,font_size=20,x=20,y=h-30,batch=self._batch)
        self._ylable=Label(self._space.y_name,font_size=20,x=20,y=h/2,batch=self._batch)
        self._xlable=Label(self._space.x_name,font_size=20,x=w/2,y=20,batch=self._batch)
        

        self._desc=Label(self.cfg.desc,font_size=20,color=(255,0,0,255),x=w*0.382,y=h-32,batch=self._batch)
        


