
from pyglet import gl
from flowfield.ui import *
from flowfield.app import *
import pyglet

def main():
    settings = UISettings(
        [
            UISetting(
                dtype="int",
                type="input",
                value=10,
                name="n_boids",
                description="Number of boids",
            ),
            UISetting(
                dtype="float",
                type="slider",
                value=1,
                min=0,
                max=100,
                step=1,
                format="%.0f",
                name="distance",
                description="Distance between boids",
            )
        ])
    WIDTH = 800
    HEIGHT = 800
    app = App(
        width=WIDTH,
        height=HEIGHT,
        settings=settings,
        #simulation=SimulationBoids(width=WIDTH, height=HEIGHT, settings=settings),
        dt=1 / 60,
    )
    pyglet.app.run()
if __name__ == "__main__":
    main()
