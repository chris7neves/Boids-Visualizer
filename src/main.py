import pyglet
import boid as bd
import pyglet.window.key as key
import rules
import math
from time import sleep

# Toggles to add
# - fullscreen, use the window.set_fullscreen() method
# - which display to use (if using multiple screens)

window = pyglet.window.Window(resizable=True)
screen_res = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=12,
                          x=0, anchor_x='left', anchor_y='top')

num_boid = pyglet.text.Label('boids:',
                          font_name='Times New Roman',
                          font_size=12,
                          x=0, anchor_x='left', anchor_y='top')


@window.event
def on_resize(width, height):
    scrn_sz = f"{width}, {height}"
    screen_res.text = scrn_sz
    screen_res.y = height

    num_boid.y = height - 16

flock = []
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        flock.append(bd.boid(x=x, y=y, radius=4, color=(50, 225, 255)))
        num_boid.text = "boids: {}".format(len(flock))


@window.event
def on_draw():
    window.clear()
    screen_res.draw()
    num_boid.draw()
    for boid in flock:
        boid.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('A is pressed')
        flock[0].applyforce(100, 45)


def update(dt):
    # rules.move_com(flock)

    for boid in flock:
        boid.update(dt, window.width, window.height)


pyglet.clock.schedule_interval(update, 1/60.0) # passes the elapsed time directly to the update function.
pyglet.app.run()
