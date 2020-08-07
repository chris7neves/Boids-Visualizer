import math

PI = 3.14159
RAD_TO_DEG = 180/PI
# Boid updater

# def update_positions(boid_list):


# Rule 1

# Would be usefule to create only a single looping function that could go through all boids and fetch required data, so that boinds dont have to be looped multiple times
def move_com(boid_list): # this would be a lot better if it considers only local flockmates. I think locality is necessary. this is where quadtree comes in
    sum_x = 0
    sum_y = 0
    for boid in boid_list: # sum the x and y of all boids
        sum_x += boid.x
        sum_y += boid.y

    if len(boid_list) > 1:
        subtr = 1
    else:
        subtr = 0

    for boid in boid_list: # need to account for center of mass when there is only 1 bird
        # Perceived center of mass. Does not include bird doing the observing
        pcom_x = (sum_x - boid.x)/(len(boid_list) - subtr)
        pcom_y = (sum_y - boid.y)/(len(boid_list) - subtr)
        theta = math.atan((pcom_y-boid.y)/(pcom_x-boid.x)) * RAD_TO_DEG # possible division by zero
        boid.applyforce(15, theta)
