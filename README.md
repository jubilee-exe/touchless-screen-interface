# TOUCHLESS SCREEN INTERFACE USING 3D COMPUTER VISION #

<dl>

<dt> Objective: </dt> In the inspiration of the recent COVID pandemic, I and three other classmates teamed up together to write a basic foundation of our prototype. 
		      It involves two major API implementations: Intel RealSense Stereo Depth Camera d345i's built-in library and Google's MediaPipe Hands.

<dt> Tasks Accomplished: </dt>

<dd> - Overlap the two images created by the camera to detect distances of objects and the captured image simultaneously </dd>
<dd> - Properly implement hand recognition and extracting the tip of the pointer finger's data from the built hand skeletal model </dd>
<dd> - Set z-axis distance and time boundaries to indicate when the user has selected their option </dd>
<dd> - Created an initialization stage where every time the sofware begins or restarts, the user (typically the owner) has to intialize the corners of each menu option </dd>
<dd> - Prints out the desired results of the user </dd>

<dt> Caveats/Room for Improvement: </dt>

<dd> - There are two manual inputs required during each initialization <dd>
<dd><dd> + Corners of each menu - this is where the Harris Corner Detection or Edge Detection Convlution algorithm is handy, needs proper implementation </dd></dd>
<dd><dd> + Menu items - Tesseract was implemented to make text recognition and extraction easy however there were many bugs and inaccuracies </dd></dd> 
<dd><dd><dd> Common bug includes: repeated words, randomized words, unclear spelling, program crashing </dd></dd></dd> 

</dl>
