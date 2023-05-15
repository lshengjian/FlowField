from dataclasses import dataclass
@dataclass
class State:
    x:int
    y:int
    z:int
    def __iter__(self):
        yield from [self.x,self.y,self.z]

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

    def limit(self,x):
        if x> self.high:
            x= self.low
        elif x< self.low:
            x= self.high
        return x
    @property
    def distance(self):
        return self.high-self.low

if __name__ == "__main__":
    s=State(1,2,3)
    assert [1,2,3]==list(s)
    s.y=999.9
    assert [1,999.9,3]==list(s)
    