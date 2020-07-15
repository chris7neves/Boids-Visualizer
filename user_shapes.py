import pyglet

class boid(pyglet.shapes.Circle):
    def __init__(self, x, y, radius=5, segments=None, color=(255, 255, 255), batch=None, group=None):
        super().__init__(x, y, radius, segments, color, batch, group)
        self.vel_x = 0
        self.vel_y = 0
        self.accel_y = -10

    def update(self, dt):
        self.x += self.vel_x*dt
        self.vel_y += self.accel_y * dt
        self.y += self.vel_y*dt