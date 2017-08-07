'''
	 The list stability_values contains values of a, c, d, f corresponding to respective Atmospheric Stability class and distance x in km.
The list contains the values in the following format:
[ [a, c, d, f] for x<=1km , [a, c, d, f] for x > 1 km ]. Index from 0 to 5 represents class from A to F.

'''


stability_values = [
			 [ [213, 440.8, 1.941, 9.27], [213, 459.7, 2.094, -9.6] ],
			 [ [156, 100.6, 1.149, 3.3], [156, 108.2, 1.098, 2] ],
			 [ [104, 61, 0.911, 0], [104, 61, 0.911, 0] ],
			 [ [68, 33.2, 0.725, -1.7], [68, 44.5, 0.516, -13.0] ],
			 [ [50.5, 22.8, 0.678, -1.3],[50.5, 55.4, 0.305, -34.0] ],
			 [ [34, 14.35, 0.740, -0.35], [34, 2.6, 0.18, -48.6] ] 
		   ]
