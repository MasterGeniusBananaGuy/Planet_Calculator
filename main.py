from radius_and_diameter import rad_and_dia as radia
from mass_density_volume_and_surface_area import mass_dens_vol_and_surf as mdvs
import os
import time
import json



def stop():
	quit()



def start():
	os.system('clear')
	load = input("Would you like to load a previus planet? (yes/no) ")
	if load == 'yes':
		name = input("what planet would you like to load: ")
		with open("saves.json", "r") as file:
			saves = json.load(file)
			planets = saves["planets"]

			if name in planets:
				planet = planets[f"{name}"]
				r = planet["Radius"]
				d = planet["Diameter"]
				plcic = planet["Planet Circumference"]
				vol = planet["Volume"]
				mass = planet["Mass"]
				surf = planet["Surface Area"]
			else:
				print("Planet not saved or misspelled!")
				time.sleep(5)
				stop()
			print(r, d, plcic, vol, mass, surf)
	else:
		main()



def main():
	os.system('clear')
	shle1 = input("Shadow lenght 1: ")
	shle2 = input("Shadow lenght 2: ")
	density = input("Kilo's per cubic meter: ")

	r = radia(shle1, shle2)[0]
	d = radia(shle1, shle2)[1]
	plcic = radia(shle1, shle2)[2]
	vol = mdvs(density, r)[0]
	mass = mdvs(density, r)[1]
	surf = mdvs(density, r)[2]

	print(r, d, plcic, vol, mass, surf)
	time.sleep(5)

	os.system('clear')
	save = input("Would you like to safe? (yes/no) ")
	if save == "yes":
		save(r, d, plcic, vol, mass, surf)
	else:
		stop()



def save(r, d, plcic, vol, mass, surf):
	os.system('clear')
	planet = input("Name of the planet: ")
	with open('saves.txt', 'a') as f:
			f.write("Planet: " + str(planet) + "\n")
			f.write("Radius: " + str(r) + " km " + "\n")
			f.write("Diameter: " + str(d) + " km" + "\n")
			f.write("Planet Circumference: " + str(plcic) + " km" + "\n")
			f.write("Mass: " + str(mass) + "ton(s)" + "\n")
			f.write("Volume: " + str(vol) + " km3" + "\n")
			f.write("Surface Area: " + str(surf) + " km2" + "\n")
	stop()



start()