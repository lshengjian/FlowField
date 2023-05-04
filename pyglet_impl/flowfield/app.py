from .ui import UISettings, UI
#from base.simulation import Simulation
#import pyglet
from pyglet.window import mouse,Window,FPSDisplay
from pyglet import clock
from .grid import Grid

class App(Window):
    def __init__(
        self,
        width: int,
        height: int,
        settings: UISettings,
        #simulation: Simulation,
        name: str = "My Flow Field Demo",
        dt: float = 1 / 60,
    ):
        super().__init__(width, height, name, resizable=True)
        self.set_vsync(False)
        clock.schedule_interval(self.update, dt)
        self.fps_display = FPSDisplay(window=self)
        self.UI = UI(self, settings)
        self.grid = Grid(0,0,width, height,(-4,4),(-10,10),(20,20))
        #self.settings=settings
        #self.simulation = simulation

    def on_draw(self):
        self.clear()
        self.fps_display.draw()
        self.grid.draw()
        self.UI.render()
        
    #@window.event
    def on_mouse_press(self,x, y, button, modifiers):
        #global pc
        if button & mouse.RIGHT:
            #pc=(x,y)
            self.circle.position=(x,y)

    def update(self, dt):
        
        if self.UI.settings.get_changed("n_boids"):
            print(self.UI.settings.get_value("n_boids"))
        #self.simulation.update(dt)
        #self.simulation.draw()
