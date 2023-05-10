class Bound:
    def __init__(
        self,
        low: float=0,
        high: float=1
    ):
        self.low=low
        self.high=high

    def force(self,x):
        if x> self.high:
            x= self.low
        elif x< self.low:
            x= self.high
        return x
    @property
    def distance(self):
        return self.high-self.low