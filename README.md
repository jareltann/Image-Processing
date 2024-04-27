In this project I created my own image processing software 
Using functionalities, including rotation, scaling, and applying filters, all presented in a nice stand-alone interface. 
Plus, I added a computer vision feature to “detect” a fish in water for a cat.

Some of the topics used to complete this project:

Loops to continue asking for user input to determine which functionality to use
Lists and Dictionaries to store the available functionalities and state of the program
Functions to process user input and generate instruction menus
Nested for-loop to access pixels of images to perform the modifications
Using modules defined
Utilize the event-loop of Pygame to accept user input

Two main components in this project.

Component 1: User Interface
The User Interface controls how information is being presented to the user, and how the program receives and processes user input. 
It uses some of the functions provided in the cmpt120imageProjHelper module. 
The most notable ones are:

getImage – loads an image from the computer into the program as a 2D R/G/B array
saveImage – saves an image represented as a 2D R/G/B array to the computer
showInterface – displays the image represented as a 2D R/G/B array to a window (user interface), together with the caption and the instruction text
At any point in time the user interface shows all possible options the user can choose from. 

There are two parts in the options:

The “system” options – these options include Quit, Open Image, Save Current Image, and Reload Original Image. They are always available to the user and are selected by the characters Q/O/S/R.
The “manipulation” options – these options vary depending on which mode the user is at: Basic, Intermediate, and Advanced. 


Component 2: Image Manipulation Module 
The Image Manipulation Module contains all the functions that perform a certain image manipulation functionality to an image represented by a 2D R/G/B array 
All functions return a newly created image represented by a 2D R/G/B array.
