# Program To Read video
# and Extract Frames
import cv2


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
		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()
		#threshold is a hyperparameter which is to be tuned regularly
		# if previousimage==None or diff(previousimage,image)>threshold:
			#Saves the frames with frame-count
		cv2.imwrite("./frames/frame%d.jpg" % count, image)
		count+= 1
	print()
	print("*******************************************************************************")
	print("The video has been divided into frames.................")
	print("*******************************************************************************")
	# print(success,"at the end")
		

# Driver Code
if __name__ == '__main__':

	# Calling the function
	previousimage=None   
	threshold=558    #this hyperparameter is decided by the user for each video separately
	path=input("Enter full path of the video whose description is to be generated: \n")
	FrameCapture(path)
