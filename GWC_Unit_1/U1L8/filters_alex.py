from PIL import Image #Import the Pillow library (images stuff)
import math #import the math library

#open the image file in the program
def load_img(filename):
    im = Image.open(filename) #stores image object it in a tempt variable
    return im #return the image

#Function to display the image
def show_img(img_obj):
    img_obj.show()

#Function to save the image
def save_img(img_save, filename):
    img_save.save(filename, 'jpeg')
    show_img(img_save) #show the image after you save it

#Apply emphasize a color filter in the image
###INSTRUCTIONS
    #For this program you need to input your own RGB VALUE that you want to emphasize

    # For example, you could do this:
    # color = input("What color do you want to emphasize? ")
    # color_list = color.split(',')
    # target_color =  [int(value) for value in color_list]
    #
    # filtered = filters.emphasize_yellow(myimage, target_color)

    #There is another function inside the emphasize function to grayscale the pixels you dont want to emphasize
    #There were some complicated math calculations so you need to import the math library!

def emphasize_alex(img_obj, target):
    #get original image's width and height attributes
    w = img_obj.width
    h = img_obj.height

    #create a new empty image of the same size
    filtered_img = Image.new("RGB", (w,h))

    ###########filter the pixels##############
    new_pixels = [] #new list to store the new pixels
    distance_desired = 130 #how far away from the desired color pixel should the program tolerate

    pixels = img_obj.getdata() #get a list of tuples with rgb values

    for pixel in pixels: #go thro one pixel at a time and do the following for every of them
        difference = 0 #reset intensity
        sum = 0
        distance = 0
        new_rgb_values = [] #empty list to store new rgb
        tuple_new_rgb = () #empty tuple

        for i in range (len(pixel)): #x index and increments by one each time
            difference = ( target[i] - pixel[i] ) ** 2 #substract value in x index from pixel from target
            sum += difference #add all the differences

        distance = math.sqrt(sum) #square root the sum

        if distance > distance_desired: #if the distance is larger than then
            new_rgb_values = greyscale_only_rgb_alex(pixel) #get the new greyscale rgb values
            tuple_new_rgb = tuple(new_rgb_values) #transform list into tuple
        else:
            tuple_new_rgb = pixel #don't change the color

        new_pixels.append(tuple_new_rgb) #add the new rgb values into new pixels list for the image

    filtered_img.putdata(new_pixels) #put all the new pixels into the empty image

    #return the new image
    return filtered_img

#this is the function to get greyscale rgb values
def greyscale_only_rgb_alex(pixel):
    intensity = 0 #reset intensity
    new_rgb_values = [] #empty list to store new rgb
    tuple_new_rgb = () #empty tuple

    for value in pixel:
        intensity += value #adding all the rgb values inside the tuple

    intensity = intensity // 3 #get average of the rgb values

    new_rgb_values = [intensity] * 3 #the new rgb value will be a tuple of the same intensity for each three values
    tuple_new_rgb = tuple(new_rgb_values)

    return tuple_new_rgb
