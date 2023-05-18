from typing import Dict,List
from abc import ABC, abstractmethod
from ..utils import ArgInfo
from .state import *
from .measure import *
class Space(ABC):
    def __init__(
        self,
        measures: List[Measure],
        isFirstOrder=True
    ):
        self._sample_point=None
        self._name=type(self).__name__
        self._isFirstOrder=isFirstOrder
        self._description=''
        self._names=[m.name for m in measures]
        #print(self.names)
        self._measures:Dict[str,Measure]={m.name:m for m in measures}
        #self.set_description()

        self._args:Dict[str,ArgInfo]={'step':ArgInfo('step',0.05,0.01,0.5,0.01)}
        self.config_args()
        self.reset()
    
    def get_state_zero(self)->State:
        return State(' '.join(self.names))
    
    def get_index(self,name)->int:
        return self._names.index(name)


    def get_measure(self,name)->Measure:
        for k in self._measures.keys():
            if name==k:
                #print(self._measures[name])
                return self._measures[name]
    @property
    def name(self)->str:
        return self._name
    @property
    def names(self)->List[str]:
        return self._names
      
    def clone(self,state):
        return self.get_state_zero().set_data(*state) 
        
    def reset(self):
        pass

    def limit(self,xs,fix=False): 
        rt=[]
        for i,m in enumerate(self._measures):
            rt.append(m.bound.limit(xs[i],fix))
        return rt 
        
    
    def arg_value(self,name:str)->float:
        return self._args[name].value
    
   
    def set_args(self,args:List[ArgInfo]):
        for arg in args:
            self._args[arg.name]=arg
    
    @property
    def sample_point(self):
        return self._sample_point    
    @sample_point.setter
    def sample_point(self,val):
        self._sample_point=val
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,desc:str):
        self._description=desc
        
    def config_args(self):
        pass

    @abstractmethod 
    def constraint(self,state:State)->float:
        pass