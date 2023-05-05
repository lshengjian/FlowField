from pyglet import gl
from phase_space.ui import *
from config import *
from phase_space.app import *
import pyglet

def main():
    app = App(
        width=WIDTH,
        height=HEIGHT,
        settings=settings,
        dt=1 / 60,
    )
    pyglet.app.run()
if __name__ == "__main__":
    main()
