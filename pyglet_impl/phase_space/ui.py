from typing import List
import imgui
from imgui.integrations.pyglet import create_renderer
from .core import Space
class UISetting:
    def __init__(
        self,
        dtype: str,
        type: str,
        value: float,
        min: float = None,
        max: float = None,
        step: float = None,
        format: str = None,
        name: str = "No name",
        description: str = None,
    ):
        self.dtype = dtype
        self.type = type
        self.value = value
        self.min = min
        self.max = max
        self.step = step
        self.format = format
        self.name = name
        self.description = description
        self.changed = False

    def set_config(self):
        
       



        desc=self.name if self.description is None else self.description
        """Missing some combinations"""
        if self.dtype == "int" and self.type == "input":
            self.changed, self.value = imgui.input_int(self.description, self.value)
        elif self.dtype == "float" and self.type == "slider":
            self.changed, self.value = imgui.slider_float(
                desc, self.value, self.min, self.max, self.format, self.step
            )
        else:
            raise Exception("Unknown type")
        return self


class UISettings(List):
    def __init__(self, field:Space):
        settings=[]
        for key,arg in field._args.items():
            settings.append(UISetting(
                dtype="float",
                type="slider",
                value=arg.value,
                min=arg.low,
                max=arg.high,
                step=arg.step,
                format="%.2f",
                name=key,
                description=arg.desc
            ))
            #arg.attach(self.callbak)
        self.settings = settings
        self._index = 0
    #def callbak(self,arg):
    #    print(arg.name)
        
    def __iter__(self):
        for setting in self.settings:
            yield setting

    def __setitem__(self, item, value):
        self.settings[item] = value
        return self

    def get_value(self, name: str):
        out = None
        for setting in self.settings:
            if setting.name == name:
                out = setting.value
        if out is None:
            raise KeyError("Setting not found")
        return out

    def get_changed(self, name: str):
        out = None
        for setting in self.settings:
            if setting.name == name:
                out = setting.changed
        if out is None:
            raise KeyError("Setting not found")
        return out


class UI:
    def __init__(
        self, window, cb, demo_names:List[str], space:Space,name: str = "Config", text: str = "Set pendulum parameters"
    ):
        settings: UISettings=UISettings(space)
        imgui.create_context()
        self.impl = create_renderer(window)
        self.settings = settings
        self.name = name
        self.text = text
        self.demo_names=demo_names
        self.callback=cb




    def render(self):#,names:List[str]=['C1','C2'],cb=None
        imgui.new_frame()
        imgui.begin(self.name)
        imgui.text(self.text)
        
        N=len(self.demo_names)
        data=[False]*N
        for idx,na in enumerate(self.demo_names):
            if imgui.radio_button(na, data[idx]):
                if self.callback!=None:
                    imgui.end()
                    imgui.end_frame()
                    #imgui.render()
                    self.callback(na)
                    return
            if idx<N-1:
                imgui.same_line()


        for index, setting in enumerate(self.settings):
            self.settings[index] = setting.set_config()

        imgui.end()
        imgui.end_frame()
        imgui.render()
        self.impl.render(imgui.get_draw_data())
