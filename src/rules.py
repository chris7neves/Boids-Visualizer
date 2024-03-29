import math

"""
Many of the rules here are written according to the pseudocode found here:
http://www.vergenet.net/~conrad/boids/pseudocode.html

As well as the rule descriptions written by Craig Reynolds himself:
http://www.red3d.com/cwr/boids/
"""

PI = 3.14159
RAD_TO_DEG = 180/PI

# Rule 1

# Would be usefule to create only a single looping function that could go through all boids and fetch required data, so that boinds dont have to be looped multiple times
# def move_com(boid_list): # this would be a lot better if it considers only local flockmates. I think locality is necessary. this is where quadtree comes in
#     sum_x = 0
#     sum_y = 0
#     for boid in boid_list: # sum the x and y of all boids
#         sum_x += boid.x
#         sum_y += boid.y

#     if len(boid_list) > 1:
#         subtr = 1
#     else:
#         subtr = 0

#     for boid in boid_list: # need to account for center of mass when there is only 1 bird
#         # Perceived center of mass. Does not include bird doing the observing
#         pcom_x = (sum_x - boid.x)/(len(boid_list) - subtr)
#         pcom_y = (sum_y - boid.y)/(len(boid_list) - subtr)
#         theta = math.atan((pcom_y-boid.y)/(pcom_x-boid.x+0.000000001)) * RAD_TO_DEG # possible division by zero
#         boid.applyforce(15, theta)

def rule1(b, flock):
    """
    Rule 1 (Cohesion): Steer to move toward the average position of local flockmates
    """

    sum_x = 0
    sum_y = 0

    if len(flock) == 1:
        return (0, 0)

    for boid in flock:

        if boid != b:
            sum_x += boid.x
            sum_y += boid.y
    
    pcx = sum_x / (len(flock) - 1)
    pcy = sum_y / (len(flock) - 1)

    velx = (pcx - b.x)/100
    vely = (pcy - b.y)/100

    return (velx, vely)

def rule2(b, flock):
    """
    Rule 2 (Separation): steer to avoid crowding local flockmates.
    """
    closex = 0
    closey = 0

    max_dist = 2000 # This is 100 units squared

    for boid in flock:
        if boid != b:
            if ((boid.x - b.x)**2) + ((boid.y - b.y)**2) < max_dist:
                closex = closex - (boid.x - b.x)
                closey = closey - (boid.y - b.y)

    return (closex, closey)

def rule3(b, flock):
    pass