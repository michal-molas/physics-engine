import numpy as np
import math

def collide_walls(shapes, walls, sett):
    for s in shapes:
        if s.t == "Circle":
            s.collide_walls(walls, sett)

def collide_shapes(shapes, sett):
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
                    cc_collide(s1, s2, sett)

def cc_collide(s1, s2, sett):
    m1 = sett.DENS*math.pi*pow(s1.r, 2)
    m2 = sett.DENS*math.pi*pow(s2.r, 2)
        
    n = s1.S-s2.S
    un = n/np.linalg.norm(n)
    ut = np.array([-un[1], un[0]])
        
    v1n_s = np.dot(un, s1.vel)
    v1t_s = np.dot(ut, s1.vel)
    v2n_s = np.dot(un, s2.vel)
    v2t_s = np.dot(ut, s2.vel)

    v1n_sp = (v1n_s*(m1-m2)+2*s2.m*v2n_s)/(s1.m+s2.m)
    v1t_sp = v1t_s
    v2n_sp = (v2n_s*(m2-m1)+2*s1.m*v1n_s)/(s1.m+s2.m)
    v2t_sp = v2t_s

    v1n_p = v1n_sp*un
    v1t_p = v1t_sp*ut
    v2n_p = v2n_sp*un
    v2t_p = v2t_sp*ut

    v1_p = v1n_p + v1t_p
    v2_p = v2n_p + v2t_p
    
    s1.vel = v1_p
    s2.vel = v2_p

def perform_collisions(shapes, walls, sett):
    collide_walls(shapes, walls, sett)
    collide_shapes(shapes, sett)
    
