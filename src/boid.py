import pyglet
from math import *


class boid(pyglet.shapes.Circle):

    def __init__(self, x, y, radius=5, segments=None, color=(255, 255, 255), batch=None, group=None):
        super().__init__(x, y, radius, segments, color, batch, group)
        self.vel_x = 0
        self.vel_y = 0
        self.accel_x = 0
        self.accel_y = 0

    def update(self, dt, scrn_x, scrn_y):

        #self.vel_x += self.accel_x * dt
        
        if self.x >= 0.95 * scrn_x:
            self.x = 0.95 * scrn_x
            #self.vel_x -= scrn_x/20
            self.vel_x = -1 * self.vel_x
        elif self.x < 0.05 * scrn_x:
            self.x = 0.05 * scrn_x
            #self.vel_x += scrn_x/20
            self.vel_x = -1 * self.vel_x

        self.vel_y += self.accel_y * dt
        
        if self.y >= 0.95 * scrn_y:
            self.y = 0.95 * scrn_y
            #self.vel_y -= scrn_y/20
            self.vel_y = -1 * self.vel_y
        elif self.y < 0.05 * scrn_y:
            self.y = 0.05 * scrn_y
            #self.vel_y += scrn_y/20
            self.vel_y = -1 * self.vel_y 
        
        if self.vel_x > 250:
            self.vel_x = 250
        
        if self.vel_y > 250:
            self.vel_y = 250


        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

    def applyforce(self, f_mag, f_dir):
        """
        Applies a given force to a boid and changes its acceleration. Assumes a mass of 1kg

        :param f_mag: Force magnitude (Newtons)
        :param f_dir: Force direction (deg)
        :return:
        """
        # 0.0174533 is the DEG to RAD conversion

        self.f_x = f_mag * cos(f_dir * 0.0174533)
        self.f_y = f_mag * sin(f_dir * 0.0174533)

        self.accel_x += self.f_x
        self.accel_y += self.f_y
