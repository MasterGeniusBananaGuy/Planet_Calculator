import math

def mass_dens_vol_and_surf(maofchoice, r):     #material_of_choice and radius
    mass = r * r * r
    mass = mass * math.pi * 4/3
    mass = mass * int(maofchoice)
    mass = mass / 1000
    return mass