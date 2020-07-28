# Boid updater

# def update_positions(boid_list):


# Rule 1

def move_com(boid_list): # this would be a lot better if it considers only local flockmates. I think locality is necessary
    sum_x = 0
    sum_y = 0
    for boid in boid_list: # sum the x and y of all boids
        sum_x = boid.x
        sum_y = boid.y

    for boid in boid_list:
        pcom_x = (sum_x - boid.x)/(len(boid_list) - 1) # Finds the perceived COM which does not include the boid being considered
        pcom_y = (sum_y - boid.y)/(len(boid_list) - 1)

