class Bound:
    def __init__(
        self,
        low: float=0,
        high: float=1
    ):
        self.low=low
        self.high=high
    
    @property
    def distance(self):
        return self.high-self.low