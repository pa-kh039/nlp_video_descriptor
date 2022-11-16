# Program To Read video
# and Extract Frames
import cv2
from diff import getdifference


# Function to extract frames
def FrameCapture(path):
	global previousimage
	# global threshold
	# 	
	# Path to video file
	vidObj = cv2.VideoCapture(path)

	# Used as counter variable
	count = 0
	# counter2=0

	# checks whether frames were extracted
	success = 1
    
	while success:
		try:
			# vidObj object calls read
			# function extract frames
			success, image = vidObj.read()
			#threshold is a hyperparameter which is to be tuned regularly
			# if previousimage==None or diff(previousimage,image)>threshold:
				#Saves the frames with frame-count
			cv2.imwrite("./frames/frame%d.jpg" % count, image)
			count+= 1
		except:
			print(count)
			break
	
	print()
	print("*******************************************************************************")
	print("The video has been divided into frames.................")
	print("*******************************************************************************")
	# print(success,"at the end")
	a = 0
	b = 1
	sum = 0
	while b<count:
		c = getdifference('frame'+str(a)+'.jpg','frame'+str(b)+'.jpg')
		sum = sum + c
		a = a + 1
		b = b + 1
	sum = 3*(sum/(count))
	print(sum)
	a = 0
	b = 1
	l = []
	l.append('frame'+str(a)+'.jpg')
	while b < count:
		c = getdifference('frame'+str(a)+'.jpg','frame'+str(b)+'.jpg')
		if (c>=sum):
			print(c)
			l.append('frame'+str(b)+'.jpg')
			a = b 
		b = b + 1
	print(l)

# Driver Code
if __name__ == '__main__':

	# Calling the function
	previousimage=None   
	threshold=558    #this hyperparameter is decided by the user for each video separately
	path=input("Enter full path of the video whose description is to be generated: \n")
	FrameCapture(path)
