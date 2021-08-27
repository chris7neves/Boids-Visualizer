import pyglet
import boid as bd
import pyglet.window.key as key
from rules import rule1, rule2, rule3
import math
from utils import rand_init, find_cg
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

cg = bd.boid(0, 0, radius=4, color=(255, 255, 255))

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
    if button == pyglet.window.mouse.RIGHT:
        if len(flock) > 0:
            del flock[-1]

@window.event
def on_draw():
    window.clear()
    screen_res.draw()
    num_boid.draw()
    cg.draw()
    for boid in flock:
        boid.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('A is pressed')
        flock[0].applyforce(100, 45)
    if symbol == key.S:
        rand_init(10, flock, window.width, window.height)

def update(dt):

    # Get global cg
    cgxy = find_cg(flock)
    cg.x = cgxy[0]
    cg.y = cgxy[1]

    for boid in flock:
        v1 = rule1(boid, flock)
        v2 = rule2(boid, flock)
        #v3 = rule3(boid, flock)
        boid.vel_x = boid.vel_x + v1[0] + v2[0]
        boid.vel_y = boid.vel_y + v1[1] + v2[1]

        boid.update(dt, window.width, window.height)


pyglet.clock.schedule_interval(update, 1/60.0) # passes the elapsed time directly to the update function.
pyglet.app.run()
