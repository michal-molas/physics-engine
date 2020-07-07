import numpy as np
import math
from settings import *

def collide_walls(shapes):
    for s in shapes:
        s.collide_walls()

def collide_shapes(shapes):
    for i in range(len(shapes)-1):
        for j in range(i+1, len(shapes)):
            s1 = shapes[i]
            s2 = shapes[j]
            if s1.t == "Circle" and s2.t == "Circle":
                dist = math.sqrt((s2.S[0]-s1.S[0])**2 + (s2.S[1]-s1.S[1])**2)
                if dist <= s1.r + s2.r:
                    x = s1.r + s2.r - dist
                    vec = np.array([s1.S[0]-s2.S[0],s1.S[1]-s2.S[1]])
                    vec = (vec/np.linalg.norm(vec))*(x/2)
                    s1.rel_pos += vec
                    s2.rel_pos -= vec
                    cc_collide(s1, s2)

def cc_collide(s1, s2):
    m1 = DENS*math.pi*pow(s1.r, 2)
    m2 = DENS*math.pi*pow(s2.r, 2)
        
    n = np.array([s2.S[0]-s1.S[0], s2.S[1]-s1.S[1]])
    un = n/np.linalg.norm(n)
    ut = np.array([-un[1], un[0]])
        
    v1n_s = np.dot(un, s1.vel)
    v1t_s = np.dot(ut, s1.vel)
    v2n_s = np.dot(un, s2.vel)
    v2t_s = np.dot(ut, s2.vel)

    v1n_sp = (v1n_s*(m1-m2)+2*m2*v2n_s)/(m1+m2)
    v1t_sp = v1t_s
    v2n_sp = (v2n_s*(m2-m1)+2*m1*v1n_s)/(m1+m2)
    v2t_sp = v2t_s

    v1n_p = v1n_sp*un
    v1t_p = v1t_sp*ut
    v2n_p = v2n_sp*un
    v2t_p = v2t_sp*ut

    v1_p = v1n_p + v1t_p
    v2_p = v2n_p + v2t_p
    
    s1.vel = v1_p
    s2.vel = v2_p

def perform_collisions(shapes):
    collide_walls(shapes)
    collide_shapes(shapes)
    
