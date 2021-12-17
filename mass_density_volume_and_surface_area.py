import math

def mass_dens_vol_and_surf(density, r):     #material_of_choice and radius
    vol = r * r * r * math.pi * 4/3
    mass = int(vol) * int(density) / 1000
    surf = 4 * math.pi * r
    
    return vol, mass, surf