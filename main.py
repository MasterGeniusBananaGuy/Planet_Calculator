from radius_and_diameter import rad_and_dia as radia
import os

def main():
	shle1 = input("Shadow lenght 1:")
	shle2 = input("Shadow lenght 2:")

	r = radia(shle1, shle2)[0]
	d = radia(shle1, shle2)[1]
	plcic = radia(shle1, shle2)[2]

	print(r, d, plcic)

	restart(r, d, plcic)
	
def restart(r, d, plcic):
	save = input("Would you like to save this planet? (yes/no) ")
	planet = input("Name of the planet: ")
	if save == 'yes':
		with open('saves.txt', 'a') as f:
			f.write("Planet: " + str(planet) + "\n")
			f.write("Radius: " + str(r) + "\n")
			f.write("Diameter: " + str(d) + "\n")
			f.write("Planet Circumference: " + str(plcic) + "\n \n")
	os.system('clear')
	main()
	
main()