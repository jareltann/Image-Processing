# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author: Jarel Tan (301463590)
# Date: December 6, 2021
# Description: CMPT 120 Final Project

# Import Modules
import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()


# list of system options
system = ["Q: Quit","O: Open Image",
"S: Save current Image","R: Reload Original Image"]

# list of basic operation options
basic = ["1: Apply Red Filter","2: Apply Green Filter",
"3: Apply Blue Filter","4: Apply Sepia Filter",
"5: Apply Warm Filter","6: Apply Cold Filter",
"7: Switch to Advanced Functions"]

# list of advanced operation options
advanced = ["1: Rotate Left", "2: Rotate Right",
"3: Double Size", "4: Half Size",
"5: Locate Fish", "6: Switch to Basic Functions"]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        elif userInput == "O":
            print("Log: Opening Image....")
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            img = cmpt120imageProjHelper.getImage(openFilename)
            cmpt120imageProjHelper.showInterface(img, "Opened Image", generateMenu(state))
            state["lastOpenFilename"] = openFilename
            return img
        elif userInput == "S":
            print("Log: Saving Image....")
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProjHelper.saveImage(img, saveFilename)
            cmpt120imageProjHelper.showInterface(img, "Saved Image" , generateMenu(state))
        elif userInput == "R": # Works after user inputs 'O'
            print("Log: Reloading Original Image...")
            img = cmpt120imageProjHelper.getImage(state["lastOpenFilename"])
            cmpt120imageProjHelper.showInterface(img, "Reloaded Image", generateMenu(state))
            return img

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        if state["mode"] == "basic":
            if userInput == "1":
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.red_filter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Red Filter", generateMenu(state))
            elif userInput == "2":
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.green_filter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Green Filter", generateMenu(state))
            elif userInput == "3":
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.blue_filter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Blue Filter", generateMenu(state))
            elif userInput == "4":
                print("Log: Performing " + basic[int(userInput)-1])
                img = cmpt120imageManip.sepia_filter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter", generateMenu(state))
            elif userInput == "5":
                print("Log: Performing " + basic[int(userInput)-1])
                # Apply both scale up and scale down warm filters to achieve the warm filter
                img = cmpt120imageManip.warm_filter_up(img)     # Scale up warm filter
                img = cmpt120imageManip.warm_filter_down(img)   # Scale down warm filter
                cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter", generateMenu(state))
                state["lastSaveFilename"] = img
            elif userInput == "6":
                print("Log: Performing " + basic[int(userInput)-1])
                # Similarly, apply both scale up + down cold filters to achieve the cold filter
                img = cmpt120imageManip.cold_filter_up(img)     # Scale up cold filter
                img = cmpt120imageManip.cold_filter_down(img)   # Scale down cold filter
                cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter", generateMenu(state))
                state["lastSaveFilename"] = img
            elif userInput == "7":
                state["mode"] = "advanced"
                print("Log: Performing " + basic[int(userInput)-1])
                cmpt120imageProjHelper.showInterface(img, "Switch Modes", generateMenu(state))
        elif state["mode"] == "advanced":
            if userInput == "1":
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.rotate_left(img)
                cmpt120imageProjHelper.showInterface(img, "Rotate Left", generateMenu(state))
            elif userInput == "2":
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.rotate_right(img)
                cmpt120imageProjHelper.showInterface(img, "Rotate Right", generateMenu(state))
            elif userInput == "3":
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.double_size(img)
                cmpt120imageProjHelper.showInterface(img, "Double Size", generateMenu(state))
            elif userInput == "4":
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.half_size(img)
                cmpt120imageProjHelper.showInterface(img, "Half Size", generateMenu(state))
            elif userInput == "5": # Will work if yellow is detected in img
                print("Log: Performing " + advanced[int(userInput)-1])
                img = cmpt120imageManip.locate_fish(img)
                cmpt120imageProjHelper.showInterface(img, "Locate Fish", generateMenu(state))
            elif userInput == "6":
                state["mode"] = "basic"
                print("Log: Performing " + advanced[int(userInput)-1])
                cmpt120imageProjHelper.showInterface(img, "Switch Modes", generateMenu(state))
    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img


# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues))

# ***this is the event-loop of the application***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program: click the close button
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
