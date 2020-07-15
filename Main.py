import pyglet
import user_shapes as bd
from time import sleep

# Toggles to add
# - fullscreen, use the window.set_fullscreen() method
# - which display to use (if using multiple screens)

window = pyglet.window.Window(resizable=True)
screen_res = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=12,
                          x=0, anchor_x='left', anchor_y='top')


flock = []

@window.event
def on_resize(width, height):
    messg = f"{width}, {height}"
    screen_res.text = messg
    screen_res.y = height


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        flock.append(bd.boid(x=x, y=y, radius=4, color=(50, 225, 255)))



@window.event
def on_draw():
    window.clear()
    screen_res.draw()
    for boid in flock:
        boid.draw()


    #pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (15, 15)), ('c3B', (255, 255, 255)))



def update(dt):
    for boid in flock:
        boid.update(dt)


pyglet.clock.schedule_interval(update, 1/60.0) # passes the elapsed time directly to the update function.
pyglet.app.run()
