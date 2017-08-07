from input import data
from Atmos_values import stability_values
import numpy as np

#calculates y and z direction plume standard deviation
#input: distance x and stability class
def plume_sd(x, stb_cls):

	#Dictionary to find the index for the stability_values
	dict = {'A': 0, 'B': 1, 'C': 2, 'D' : 3, 'E' : 4, 'F' : 5}
	i = dict[stb_cls]
	
	#coverts x in km. The values are evaluated based on x in km.
	x_km = np.true_divide(x, 1000)

	#values are categorised further based on the distance
	if np.less_equal(x_km,1).all():  #all or any?
		j = 0
	else:
		 j = 1

	#obtains a,c,d,f from the stability values list.
	a = stability_values[i][j][0]
	c = stability_values[i][j][1]
	d = stability_values[i][j][2]
	f = stability_values[i][j][3]
		
	#calculates y direction plume standard deviation
	sd_y = a * np.power(x_km , 0.894)
	
	##calculates z direction plume standard deviation.
	sd_z = c * np.power(x_km , d) + f

	return sd_y, sd_z	

#exponential part of eqn involving y.
#input: y in m  and y direction plume standard deviation.
def exp_y1(y,sd_y):
	y1 = (y*y)/(2*(sd_y*sd_y))
	return y1

#exponential part of eqn involving z+h.
#input: z in m, h in m and z direction plume standard deviation.
def exp_z1(z, h, sd_z):
	z1 = (z+h)*(z+h)/(2*(sd_z*sd_z))
	return z1

#exponential part of eqn involving z-h.
#input: z in m, h in m and z direction plume standard deviation.
def exp_z2(z, h, sd_z):
	z2 = (z-h)*(z-h)/(2*(sd_z*sd_z))
	return z2


#the function point_conc calculates the concetration at a point.
def point_conc(x, y, z):

	#y and z direction plume standard deviation
	sd_y, sd_z = plume_sd(x, stab_class)

	# y exponential term
	y1 = exp_y1(y, sd_y)

	# z+h exponential term
	z1 = exp_z1(z, h, sd_z)

	#z-h exponential term
	z2 = exp_z2(z, h, sd_z)

	# point source formula
	c = (Q/(2*np.pi*u*sd_y*sd_z))*np.exp(-y1)*(np.exp(-z1)+np.exp(-z2))
	return c


###### Main##########

#data from the user.
stab_class = data.atmos_stability
Q = data.emission_rate_Q
x = data.receptor_x
y = data.receptor_y
z = data.receptor_z
u = data.windspeed_u
deg = data.winddir_deg 
h = data.stack_height_h 


#calculates the concentration at the receptor.
c = point_conc(x, y, z)
print "Concentration at (",x,",",y,",",z,") :", c

#saves an output file
output = np.asarray([x, y, z, c])
output.tofile('output.txt',sep=',',format='%10.5f')
