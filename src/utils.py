from boid import boid
from random import seed
from random import random

seed(42)

def rand_init(fsize, flock, screen_x, screen_y):
    flock.clear()
    for i in range(0, fsize):
        x = random() * screen_x 
        y = random() * screen_y 
        flock.append(boid(x=x, y=y, radius=4, color=(50, 225, 255)))
    
    return flock

def find_cg(flock):
    """
    Find the cg of the flock.
    """

    sumcg_x = 0
    sumcg_y = 0

    if len(flock) == 0:
        return (0, 0)

    for boid in flock:
        sumcg_x += boid.x
        sumcg_y += boid.y

    pcgx = sumcg_x /(len(flock))
    pcgy = sumcg_y /(len(flock))

    return (pcgx, pcgy)
