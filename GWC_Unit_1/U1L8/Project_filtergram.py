import filters

def main():
    file = "flowers.jpg"
    myimage = filters.load_img(file)
    filters.show_img(myimage)

    color = input("What color do you want to emphasize? ")
    color_list = color.split(',')
    target_color =  [int(value) for value in color_list]

    # filtered = filters.emphasize_yellow(myimage, target_color)
    filtered = filters.obamicon(myimage)
    filters.save_img(filtered, "cool_puppy.jpg")

if __name__ == "__main__":
    main()
