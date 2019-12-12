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
def save_img(img_save, filename): #img_save is the image to be saved, and filename is the name you want the image to be saved with
    img_save.save(filename, 'jpeg')
    show_img(img_save) #show the image after you save it

#Function to apply Obamicon filter to an image
def obamicon(img_obj):
    #get original image's width and height attributes
    w = img_obj.width
    h = img_obj.height

    #create a new empty image of the same size
    filtered_img = Image.new("RGB", (w,h))

    #########filter the pixels##############
    new_pixels = [] #new list to store the new pixels

    pixels = img_obj.getdata() #get the rgb values as a list of lots of tuple

    for pixel in pixels: #go thro every pixel in the image

        intensity = 0 #variable to store the sum of the rgb values (inside the loop so that it resets every time)

        for value in pixel: #for every three value in the rgb tuple for a pixel
            intensity += value  #add the three values and store them in intensity variable

        #create a new rgb  value for a pixel according to the intensity of the original value
        if intensity < 182:
            new_rgb_values = (0, 51, 76) #dark blue
        elif intensity >= 182 and intensity < 364:
            new_rgb_values = (217, 26, 33) #red
        elif intensity >= 364 and intensity < 546:
            new_rgb_values = (112, 150, 158) #light blue
        elif intensity >= 546:
            new_rgb_values = (252, 227, 166) #yellow
        new_pixels.append(new_rgb_values) #store the new tuples (rgb values in an empty list)

    filtered_img.putdata(new_pixels) #put all the new pixels into the empty image

    #return the new image
    return filtered_img

#Apply Greyscale filter in the image
def greyscale(img_obj):
    #get original image's width and height attributes
    w = img_obj.width
    h = img_obj.height

    #create a new empty image of the same size
    filtered_img = Image.new("RGB", (w,h))

    ###########filter the pixels##############
    new_pixels = [] #new list to store the new pixels

    pixels = img_obj.getdata() #get a list of tuples with rgb values

    for pixel in pixels: #go thro one pixel at a time and do the following for every of them
        intensity = 0 #reset intensity
        new_rgb_values = [] #empty list to store new rgb
        tuple_new_rgb = () #empty tuple

        for value in pixel:
            intensity += value #adding all the rgb values inside the tuple

        intensity = intensity // 3 #get average of the rgb values

        new_rgb_values = [intensity] * 3 #the new rgb value will be a tuple of the same intensity for each three values
        tuple_new_rgb = tuple(new_rgb_values)

        new_pixels.append(tuple_new_rgb)

    filtered_img.putdata(new_pixels) #put all the new pixels into the empty image

    #return the new image
    return filtered_img

#Apply Invert filter in the image
def invert(img_obj):
    #get original image's width and height attributes
    w = img_obj.width
    h = img_obj.height

    #create a new empty image of the same size
    filtered_img = Image.new("RGB", (w,h))

    ###########filter the pixels##############
    new_pixels = [] #new list to store the new pixels

    pixels = img_obj.getdata() #get a list of tuples with rgb values

    for pixel in pixels: #go thro one pixel at a time and do the following for every of them
        intensity = 0 #reset intensity
        new_rgb_values = [] #empty list to store new rgb
        tuple_new_rgb = () #empty tuple

        for value in pixel:
            intensity = 255 - value #adding all the rgb values inside the tuple
            new_rgb_values.append(intensity)

        tuple_new_rgb = tuple(new_rgb_values)

        new_pixels.append(tuple_new_rgb)

    filtered_img.putdata(new_pixels) #put all the new pixels into the empty image

    #return the new image
    return filtered_img

#Apply emphasize a color filter in the image
def emphasize_yellow(img_obj, target):
    #get original image's width and height attributes
    w = img_obj.width
    h = img_obj.height

    #create a new empty image of the same size
    filtered_img = Image.new("RGB", (w,h))

    ###########filter the pixels##############
    new_pixels = [] #new list to store the new pixels
    # target = [243, 250, 25]
    distance_desired = 130

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
            new_rgb_values = greyscale_only_rgb(pixel) #get the new greyscale rgb values
            tuple_new_rgb = tuple(new_rgb_values) #transform list into tuple
        else:
            tuple_new_rgb = pixel #don't change the color

        new_pixels.append(tuple_new_rgb) #add the new rgb values into new pixels list for the image

    filtered_img.putdata(new_pixels) #put all the new pixels into the empty image

    #return the new image
    return filtered_img

#get greyscale rgb values
def greyscale_only_rgb(pixel):
    intensity = 0 #reset intensity
    new_rgb_values = [] #empty list to store new rgb
    tuple_new_rgb = () #empty tuple

    for value in pixel:
        intensity += value #adding all the rgb values inside the tuple

    intensity = intensity // 3 #get average of the rgb values

    new_rgb_values = [intensity] * 3 #the new rgb value will be a tuple of the same intensity for each three values
    tuple_new_rgb = tuple(new_rgb_values)

    return tuple_new_rgb
