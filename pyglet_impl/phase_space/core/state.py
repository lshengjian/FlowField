from collections import namedtuple

class State:
    ID=1
    def __init__(self,field_names:str='x1 x2 x3'):
        typeName=f'S{State.ID}'
        
        self._VectorType=namedtuple(typeName,field_names)
        self._fields=self._VectorType._fields
        State.ID+=1
        #print(typeName,len(self._fields))
        self._data=self._VectorType._make([0]*len(self._fields))
    @property
    def data(self)->namedtuple:
        return self._data
    @property
    def fields(self):
        return self._fields
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __getattr__(self, name):
        return self.value(name)   
    
    def value(self,name):
        had=hasattr(self._data,name)
        if had :
            return getattr(self._data,name)
    

    def __iter__(self):
        yield from self._data

    def set_data(self,*ds):
        self._data=self._VectorType._make(ds)
        return self

    # def set_value(self,name,val):
    #     had=hasattr(self._data,name)
    #     if had:
    #         setattr(self._data,name,val)


if __name__ == "__main__":
    p=State('x y')
    p.set_data(1,2)
    assert 1==p[0] and 2==p[1]
    assert 1==p.value('x') and 2==p.value('y')
    assert [1,2]==list(p)
    assert 1==p.x and 2==p.y
