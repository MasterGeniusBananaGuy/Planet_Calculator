
def rad_and_dia(shle1, shle2):
	shdi = int(shle2) - int(shle1)		#shadow_diff
	if shdi > 360:
		print("Max 360 degrees accepted more were given, changed to 1 degrees")
		shdi = 1
	depki = shdi 						#degres_per_kilometer
	mufci = 360 / depki 				#multiplier_for_circumference
	plcic = 100000 * mufci 				#planet_circu
	r = plcic / 6.28 					#radius
	d = r * 2 							#diameter
	return r, d, plcic