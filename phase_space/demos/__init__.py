from os import listdir
from os.path import dirname, basename
from importlib import import_module
from inspect import isclass
from ..core import Space

# Get a list of all Python files in the same directory as this file
module_names = [basename(f)[:-3] for f in listdir(dirname(__file__)) if f[-3:] == ".py" and not f.endswith("__init__.py")]

classes=[]
cls_map={}
for module_name in module_names:
    module = import_module('phase_space.demos.'+module_name)
    _cs=[getattr(module, cls) for cls in dir(module)  ]
    #print(_cs)
    for c in _cs:
        if   isclass(c) and issubclass(c,Space) and c.__name__ != 'Space':
            classes.append(c)
            cls_map[c.__name__]=c
            #print(f'import module:{module_name}')
print(cls_map.keys())
def make_space(name,*args):
    return cls_map[name](*args)
demo_names=[cls.__name__ for cls in classes]
# nowants=['ArgInfo',  'Space',  'State']
# for item in nowants:
#     demo_names.remove(item)
# Add all class names to __all__ variable
__all__ = ['demo_names','make_space']
__all__.extend(demo_names)

globals().update({cls.__name__: cls for cls in classes})



