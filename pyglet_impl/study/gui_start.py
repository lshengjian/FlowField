#from __future__ import absolute_import
from pyglet import gl
#from testwindow import show_test_window
import pyglet
from pyglet.window import mouse
from pyglet import shapes
import imgui
import sys


# Note that we could explicitly choose to use PygletFixedPipelineRenderer
# or PygletProgrammablePipelineRenderer, but create_renderer handles the
# version checking for us.
from imgui.integrations.pyglet import create_renderer

shapes.Rectangle._anchor_x = 10
shapes.Rectangle._anchor_y = 10
window = pyglet.window.Window(width=1024, height=768, resizable=True)
#window.set_mouse_visible(False)
circle = shapes.Circle(x=100, y=150, radius=100, color=(50, 225, 30))
rectangle = shapes.Rectangle(x=200, y=100, width=50, height=50, color=(250, 25, 30))
rectangle.anchor_position = 5, 5
checkbox_activ=True
state_radioButton = [True, False, False]
color = (1.0, 0.0, 0.5)
value_intSlider_1=5
#
@window.event
def on_mouse_press(x, y, button, modifiers):
    #global pc
    if button & mouse.RIGHT:
        #pc=(x,y)
        circle.position=(x,y)
        print(x,y)

def main():

    gl.glClearColor(1, 1, 1, 1)
    imgui.create_context()
    impl = create_renderer(window)

    def update(dt):
        global checkbox_activ,state_radioButton,color,value_intSlider_1
        impl.process_inputs()
        imgui.new_frame()
        imgui.begin("MyGame")

        changed, value_intSlider_1 = imgui.slider_int("Slider int 1",
            value_intSlider_1, min_value = 0, max_value = 100)


        # A checkbox has 2 return values
        # 1) "clicked" is a bool value and is "True" if the checkbox is clicked
        #   (the value is only for short time "True")
        # 2) "checkbox_enabled" is a bool value and is "True" if the
        #   checkbox is activated
        _, rt = imgui.checkbox(
            "Checkbox 1", # Label
            checkbox_activ # Input current state
        )
        checkbox_activ=rt
        # If the checkbox was clicked and activated, the value "True"
        # is assigned to the variable "checkbox_activ". In the next frame
        # of the main loop, the checkbox is reading this new value from the
        # variable and remains active.
        # The value can certainly be used by other elements or functions.

        imgui.text(f"State of the checkbox: {checkbox_activ}")


        imgui.separator()

        # Radio buttons have also a state, but these have only the
        # "clicked" return value (as with the checkbox).
        # The characteristic is that from a group only one radio button should
        # be active. To accomplish this, you must create an if-statement and
        # modify the states.
        if imgui.radio_button("Radio button 1", state_radioButton[0]):
            # Following statements handle the states of the radio buttons.
            # Only one radio button can always be active.
            state_radioButton[0] = True
            state_radioButton[1] = False
            state_radioButton[2] = False

        imgui.same_line()

        if imgui.radio_button("Radio button 2", state_radioButton[1]):
            state_radioButton[0] = False
            state_radioButton[1] = True
            state_radioButton[2] = False

        imgui.same_line()

        if imgui.radio_button("Radio button 3", state_radioButton[2]):
            state_radioButton[0] = False
            state_radioButton[1] = False
            state_radioButton[2] = True

        # Color edits (just like sliders and drags) returns int and float
        # values or tuples.
        # "change_color" is a bool value
        # "color" is a tuple with the rgb values
        change_color, color = imgui.color_edit3("Color 1", *color)

        imgui.end()


    def draw(dt):
        update(dt)
        window.clear()
        imgui.render()
        impl.render(imgui.get_draw_data())
        circle.draw()
        rectangle.draw()

        

    pyglet.clock.schedule_interval(draw, 1 / 120.0)
    pyglet.app.run()
    impl.shutdown()


if __name__ == "__main__":
    main()