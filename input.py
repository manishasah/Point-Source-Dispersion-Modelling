
class input(object):
	emission_rate_Q = 0.0
	receptor_x = 0.0
	receptor_y = 0.0
	receptor_z = 0.0
	windspeed_u = 0.0
	winddir_deg = 0.0 
	stack_height_h = 0.0
	atmos_stability = ""
	

	#Intializer 
	def __init__(self,atmos_stability,emission_rate_Q, receptor_x, receptor_y, receptor_z, windspeed_u, winddir_deg, stack_height_h):
		self.emission_rate_Q = emission_rate_Q
		self.receptor_x = receptor_x
		self.receptor_y = receptor_y
		self.receptor_z = receptor_z
		self.windspeed_u = windspeed_u
		self.winddir_deg = winddir_deg
		self.stack_height_h = stack_height_h
		self.atmos_stability = atmos_stability




#########  Main ###############

# Read Input from the input.txt file
 
F=open('input.txt','r')
inputs= []
for line in iter(F):
	for values in iter(line.split(',')):
		inputs.append(values)
F.close()

#Initialize the object. The order corresponds to the input file.
data = input(inputs[0], int(inputs[1]), int(inputs[2]), int(inputs[3]), int(inputs[4]), int(inputs[5]), int(inputs[6]), int(inputs[7]))








