# wireless-sound-control-using-hand
<br>
<h3><b>ABSTRACT</h3><br>
<p>The project is all about controlling the volume by hand gestures. The volume can be controlled by moving the index and thumb fingers. Volume increases when the fingers are farther away and decreases when they are nearer. We use the OpenCV library to take the video input from the camera, show the image, and add some additional features to add some shapes and text to the image. Mediapipe library is used for hand recognition and to find landmarks on the hand. AndreMiras library is used to get the volume interface from the system. NumPy gives the mapping of different values.</p>
<br>
<h3><b>INTRODUCTION</h3><br>
<p>Gesture recognition helps computers to understand human body language. This helps to build a more potent link between humans and machines. In this project for gesture recognition, the human body’s motions are read by a computer camera. The computer then makes use of this data as input to handle applications. This project aims to develop an interface that will capture human hand gestures dynamically and control the volume level.<br>
NumPy is a library for the Python programming language, that adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.<br>
Pycaw: Python Audio Control Library
Mediapipe is an open-source machine learning library of Google, which has some solutions for face recognition and gesture recognition and provides encapsulation of Python, JS, and other languages. MediaPipe Hands is a high-fidelity hand and finger tracking solution. It uses machine learning (ML) to infer 21 key 3D hand information from just one frame. We can use it to extract the coordinates of the key points of the hand.
<br>The camera in our device is used for this project. It detects our hand with points in it to see the distance between our thumb fingertip and index fingertip. The distance between points 4 and 8 is directly proportional to the volume of the device.<br>
Firstly, hand recognition and then the landmarks of thumb and index have to be found as well as the distance between them. Map the distance of the thumb tip and index fingertip with volume range by using the NumPy library. In my case, the distance between the thumb tip and index fingertip was within the range of 50 – 250 and the volume range was from -65.25 – 0.0. Create a rectangle to see the sound box and add text to get the volume in percentage.<br>
</p>
<br>
<h3><b>CONCLUSION</h3><br>
<p>Wireless sound control can be used to control the sound by hand gestures. This hand gesture sound controller can be used by anyone as it is more interactive and easier to use. It is also a good exercise for the hand and more fun to use.</p>
<br>
