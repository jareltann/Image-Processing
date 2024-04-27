# Image Processer
# Starter code for cmpt120imageManip.py
# Author: Jarel Tan

# Import Modules
import cmpt120imageProjHelper
import numpy


# Define the first filter (Red Filter)
def red_filter(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            result[row][col][1] = 0 # no green
            result[row][col][2] = 0 # no blue
    return result

# Define the second filter (Green Filter)
def green_filter(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            result[row][col][0] = 0 # no red
            result[row][col][2] = 0 # no blue
    return result

# Define the third filter (Blue Filter)
def blue_filter(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            result[row][col][0] = 0 # no red
            result[row][col][1] = 0 # no green
    return result

# Define the fourth filter (Sepia Filter)
def sepia_filter(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    largest_num = 255
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            r = result[row][col][0]
            g = result[row][col][1]
            b = result[row][col][2]
            # Create the formula for the new value of each colour
            sepia_red = int((r*0.393)+(g*0.769)+(b*0.189))
            sepia_green = int((r*0.349)+(g*0.686)+(b*0.168))
            sepia_blue = int((r*0.272)+(g*0.534)+(b*0.131))
            # In case the result of the sepia colours are greater than 255
            if sepia_red > largest_num:
                sepia_red = largest_num
            if sepia_green > largest_num:
                sepia_green = largest_num
            if sepia_blue > largest_num:
                sepia_blue = largest_num
            result[row][col][0] = sepia_red
            result[row][col][1] = sepia_green
            result[row][col][2] = sepia_blue
    return result

### Define the fifth filter (Warm Filter)
# Scale up "R" value
def warm_filter_up(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            # Change the red values of every pixel
            if result[row][col][0] < 64:
                result[row][col][0] = int((result[row][col][0])/64*80)
            elif 64 <= result[row][col][0] and result[row][col][0] < 128:
                result[row][col][0] = int((((result[row][col][0])-64)/(128-64))*(160-80)+80)
            else:
                result[row][col][0] = int((((result[row][col][0])-128)/(255-128))*(255-160)+160)
    return result

# Scale down "B" value
def warm_filter_down(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            # Change the blue values of every pixel
            if result[row][col][2] < 64:
                result[row][col][2] = int((result[row][col][2])/64*50)
            elif 64 <= result[row][col][2] and result[row][col][2] < 128:
                result[row][col][2] = int((((result[row][col][2])-64)/(128-64))*(100-50)+50)
            else:
                result[row][col][2] = int((((result[row][col][2])-128)/(255-128))*(255-100)+100)
    return result

# Define the sixth filter (cold Filter)
# scale up "B" value
def cold_filter_up(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            # Change the blue values of every pixel
            if result[row][col][2] < 64:
                result[row][col][2] = int((result[row][col][2])/64*80)
            elif 64 <= result[row][col][2] and result[row][col][2] < 128:
                result[row][col][2] = int((((result[row][col][2])-64)/(128-64))*(160-80)+80)
            else:
                result[row][col][2] = int((((result[row][col][2])-128)/(255-128))*(255-160)+160)
    return result

# Scale down "R" value
def cold_filter_down(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            # Change the red value of every pixel
            if result[row][col][0] < 64:
                result[row][col][0] = int((result[row][col][0])/64*50)
            elif 64 <= result[row][col][0] and result[row][col][0] < 128:
                result[row][col][0] = int((((result[row][col][0])-64)/(128-64))*(100-50)+50)
            else:
                result[row][col][0] = int((((result[row][col][0])-128)/(255-128))*(255-100)+100)
    return result

# Time for the advanced options
# First option (Rotate left)
def rotate_left(pixels):
    height = len(pixels)
    width = len(pixels[0])
    new_height = width
    new_width = height
    result = cmpt120imageProjHelper.getBlackImage(new_width, new_height)
    for row in range(height):
        for col in range(width):
            # copy each row from the original image into a column in the result image
            # flip the column of the original image to rotate the image to the left
            result[col][row] = pixels[row][-col-1]
    return result

# Second option (Rotate right)
def rotate_right(pixels):
    height = len(pixels)
    width = len(pixels[0])
    new_height = width
    new_width = height
    result = cmpt120imageProjHelper.getBlackImage(new_width, new_height)
    for row in range(height):
        for col in range(width):
            # copy each row from the original image into a column in the result image
            # flip the row of the original image to rotate the image to the right
            result[col][row] = pixels[-row-1][col]
    return result

# Third option (Double Size)
def double_size(pixels):
    height = len(pixels)
    width = len(pixels[0])
    new_height = height*2
    new_width = width*2
    result = cmpt120imageProjHelper.getBlackImage(new_width, new_height)
    for row in range(height):
        for col in range(width):
            # Each pixel of original image becomes 2x2 block of pixels in the result image
            result[row*2][col*2] = pixels[row][col]
            result[row*2][col*2+1] = pixels[row][col]
            result[row*2+1][col*2] = pixels[row][col]
            result[row*2+1][col*2+1] = pixels[row][col]
    return result

# Fourth option (Half Size)
def half_size(pixels):
    height = len(pixels)
    width = len(pixels[0])
    new_height = int(height/2)
    new_width = int(width/2)
    result = cmpt120imageProjHelper.getBlackImage(new_width, new_height)
    for row in range(new_height):
        for col in range(new_width):
            # Average of each colour of original 2 by 2 pixels
            result[row][col][0] = int(((pixels[row*2][col*2][0])+(pixels[row*2][col*2+1][0])
            +(pixels[row*2+1][col*2][0])+(pixels[row*2+1][col*2+1][0]))/4)
            result[row][col][1] = int(((pixels[row*2][col*2][1])+(pixels[row*2][col*2+1][1])
            +(pixels[row*2+1][col*2][1])+(pixels[row*2+1][col*2+1][1]))/4)
            result[row][col][2] = int(((pixels[row*2][col*2][2])+(pixels[row*2][col*2+1][2])
            +(pixels[row*2+1][col*2][2])+(pixels[row*2+1][col*2+1][2]))/4)
    return result

### Fifth Option (Locate Fish)
# Create the function of the green box first
def green_line(pixels, min_row, max_row, min_col, max_col):
    height = len(pixels)
    width = len(pixels[0])
    # Create the sides of the rectangle
    for row in range(height):
        for col in range(min_col,max_col):
            pixels[max_row][col] = [0, 255, 0] # Bottom of rectangle
    for row in range(height):
        for col in range(min_col,max_col):
            pixels[min_row][col] = [0, 255, 0] # Top of the rectangle
    for row in range(min_row, max_row):
        for col in range(width):
            pixels[row][max_col] = [0, 255, 0] # left side of rectangle
    for row in range(min_row, max_row):
        for col in range(width):
            pixels[row][min_col] = [0, 255, 0] # right side of rectangle
    return pixels

# Now create the locate fish function that calls the green box function to find the fish
def locate_fish(pixels):
    height = len(pixels)
    width = len(pixels[0])
    result = cmpt120imageProjHelper.getBlackImage(width, height)
    row_total = []
    col_total = []
    for row in range(height):
        for col in range(width):
            result[row][col] = pixels[row][col]
            r = result[row][col][0]
            g = result[row][col][1]
            b = result[row][col][2]
            hsv = cmpt120imageProjHelper.rgb_to_hsv(r,g,b) # Detects the yellow!
            if 45 < hsv[0] < 75 and 45 < hsv[1] < 65 and 90 < hsv[2] < 105:
                row_total.append(row) # Add all the rows that have yellow
                col_total.append(col) # Add all the columns that have yellow
    max_row = max(row_total)
    min_row = min(row_total)
    max_col = max(col_total)
    min_col = min(col_total)
    return green_line(result, min_row, max_row, min_col, max_col)




