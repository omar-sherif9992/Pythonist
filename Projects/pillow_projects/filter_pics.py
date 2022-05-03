from PIL import Image, ImageFilter
import os


def clear():
    i = 0

    while i > 2:
        try:
            if i == 0:
                # for windows
                os.system('cls')
            elif i == 1:
                os.system("clear")
        except:
            pass
        i += 1


def filter_picture():
    """This method resizes pictures it needs the folder path that contain the images and the desired width and height to be converted to """
    folder_path = ""
    num = 0
    intensity=0
    try:
        folder_path = str(input("The folder path that contain the images :"))
        num = int(input("Choose Your Desired Type by typing it's number :\n"
                        "1:BlUR\n"
                        "2:CONTOUR\n"
                        "3:DETAIL\n"
                        "4:EDGE_ENHANCE\n"
                        "5:EDGE_ENHANCE_MORE\n"
                        "6:EMBOSS\n"
                        "7:SHARPEN\n"
                        "8:SMOOTH\n"
                        "9:SMOOTH_MORE\n"
                        "10:FIND_EDGES\n----------------------- \n"
                        "Enter a number :"
                        ))
        intensity = int(input("choose your intensity 1-100:"))
    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        filter_picture()
    type=""
    if num == 1:
        type = ImageFilter.BLUR
    elif num == 2:
        type = ImageFilter.CONTOUR
    elif num == 3:
        type = ImageFilter.DETAIL
    elif num == 4:
        type = ImageFilter.EDGE_ENHANCE
    elif num == 5:
        type = ImageFilter.EDGE_ENHANCE_MORE
    elif num == 6:
        type = ImageFilter.EMBOSS
    elif num == 7:
        type = ImageFilter.SHARPEN
    elif num == 8:
        type = ImageFilter.SMOOTH
    elif num == 9:
        type = ImageFilter.SMOOTH_MORE
    elif num == 10:
        type = ImageFilter.FIND_EDGES
    else:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        filter_picture()

    os.chdir(folder_path)

    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/{type.name}-images")
    except:
        pass

    for image in os.listdir("."):
        filename, fileextension = os.path.splitext(image)
        if fileextension == "":
            print("This file has no extension ")
            continue
        curent_image = Image.open(image)
        curent_image.filter(type).save(f"{os.path.dirname(folder_path)}/{type.name}-images/{filename}-converted{fileextension}")
        print(f"{filename} is converted into {type.name}\n")

    print("Process is Successfully Done 😄")


if __name__ == '__main__':
    filter_picture()
