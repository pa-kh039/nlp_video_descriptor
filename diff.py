import cv2

def getdifference(a, b):
	# test image 
	#a, b should be image.jpeg
	image = cv2.imread('./frames/'+str(a))
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	histogram = cv2.calcHist([gray_image], [0],
							None, [256], [0, 256])
	# data1 image
	image = cv2.imread('./frames/'+str(b))
	gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	histogram1 = cv2.calcHist([gray_image1], [0],
							None, [256], [0, 256])
	c1 = 0
	# Euclidean Distance between data1 and test
	i = 0
	while i<len(histogram) and i<len(histogram1):
		c1+=(histogram[i]-histogram1[i])**2
		i+= 1
	c1 = c1**(1 / 2)
	return c1
