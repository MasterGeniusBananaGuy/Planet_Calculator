from radius_and_diameter import rad_and_dia as radia
from mass_density_volume_and_surface_area import mass_dens_vol_and_surf as mdvs
import os
import time

def main():
	os.system('clear')
	shle1 = input("Shadow lenght 1: ")
	shle2 = input("Shadow lenght 2: ")
	maofchoice = input("Kilo's per cubic meter: ")

	r = radia(shle1, shle2)[0]
	d = radia(shle1, shle2)[1]
	plcic = radia(shle1, shle2)[2]
	mass = mdvs(maofchoice, r)

	print(r, d, plcic, mass)
	time.sleep(5)
	stop(r, d, plcic, mass)
	
def stop(r, d, plcic, mass):
	os.system('clear')
	save = input("Would you like to save this planet? (yes/no) ")
	if save == 'yes':
		planet = input("Name of the planet: ")
		with open('saves.txt', 'a') as f:
			f.write("Planet: " + str(planet) + "\n")
			f.write("Radius: " + str(r) + " km " + "\n")
			f.write("Diameter: " + str(d) + " km" + "\n")
			f.write("Planet Circumference: " + str(plcic) + " km" + "\n")
			f.write("Mass: " + str(mass) + "ton(s)" + "\n \n")
		os.system('clear')
		quit()
	else:
		os.system('clear')
		quit()
	
def start():
	os.system('clear')
	load = input("Would you like to load a previus planet? (yes/no) ")
	if load == 'yes':
		with open('saves.txt', 'r') as f:
			lines = [line.strip() for line in f]
			for line in lines:
				planet = lines[0] + "\n"
				r = lines[1] + " km" + "\n"
				d = lines[2] + " km" + "\n"
				plcic = lines[3] + " km" + "\n"
				mass = lines[4] + " ton(s)" "\n"
			print(planet + r + d + plcic + mass)
			time.sleep(5)
			os.system('clear')
			quit()
	else:
		main()


start()