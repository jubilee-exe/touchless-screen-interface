# TOUCHLESS SCREEN INTERFACE USING 3D COMPUTER VISION #


Objective: In the inspiration of the recent COVID pandemic, I and three other classmates teamed up together
	   to write a basic foundation of our prototype. It involves two major API implementations: Intel 
	   RealSense Stereo Depth Camera d345i's built-in library and Google's MediaPipe Hands. 

Tasks Accomplished:
	- Overlap the two images created by the camera to detect distances of objects and the captured image simultaneously
	- Properly implement hand recognition and extracting the tip of the pointer finger's data from the built hand skeletal model
   	- Set z-axis distance and time boundaries to indicate when the user has selected their option
   	- Created an initialization stage where every time the sofware begins or restarts, the user (typically the owner) has to intialize the corners of each menu option
    	- Prints out the desired results of the user

Caveats/Room for Improvement:
	- There are two manual inputs required during each initialization
		+ Corners of each menu - this is where the Harris Corner Detection or Edge Detection Convlution algorithm is handy, needs proper implementation
		+ Menu items - Tesseract was implemented to make text recognition and extraction easy however there were many bugs and inaccuracies
			> Common bug includes: repeated words, randomized words, unclear spelling, program crashing 
