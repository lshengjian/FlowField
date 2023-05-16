from dataclasses import dataclass
# @dataclass
# class State:
#     x:int
#     y:int
#     z:int
#     def __iter__(self):
#         yield from [self.x,self.y,self.z]

@dataclass
class Point:
    x:int
    y:int
    def __iter__(self):
        yield from [self.x,self.y]
@dataclass
class Size:
    width:int
    height:int  
    
    # def __post_init__(self):
    #     self._data=[self.width,self.height]
    def __iter__(self):
        yield from [self.width,self.height]
@dataclass   
class Viewport:
    start:Point
    size:Size
class Bound:
    def __init__(
        self,
        low: float=0,
        high: float=1
    ):
        self.low=low
        self.high=high

class Bound:
    def __init__(
        self,
        low: float=0,
        high: float=1
    ):
        self.low=low
        self.high=high

    def limit(self,x,isFixed=False):
        rt=x
        if x<self.low:
            rt=self.low if isFixed else self.high
        elif  x>self.high:
            rt=self.high if isFixed else self.low
        return rt


    @property
    def distance(self):
        return self.high-self.low
@dataclass
class ArgInfo:
    """可变参数定义."""
    name: str
    value: float
    low: float
    high: float
    step: float=0 
    desc: str=None
    '''
    def __init__(
        self,
        name: str,
        value: float,
        low: float,
        high: float,
        step: float=0
        
    ):
        self._name=name
        self._value=value
        self._low=low
        self._high=high
        self._step=step
        self._callbaks=[]

    def notify(self):
        for cb in self._callbaks:
            cb(self)
    def attach(self,callback):
        self._callbaks.append(callback)

    def detach(self,callback):
        self._callbaks.remove(callback)
    @property
    def name(self):
        return self._name
    @property
    def low(self):
        return self._low        
    @property
    def high(self):
        return self._high
    @property
    def step(self):
        return self._step
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,val):
        self._value=val
        self.notify()
    '''

if __name__ == "__main__":
    p=Point(1,2)
    assert [1,2]==list(p)
    p.y=9.9
    assert [1,9.9]==list(p)
    