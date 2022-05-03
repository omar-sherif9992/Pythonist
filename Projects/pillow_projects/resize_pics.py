from PIL import Image
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


def resize_picture():
    """This method resizes pictures it needs the folder path that contain the images and the desired width and height to be converted to """
    folder_path =""
    width = 0
    height = 0
    try:
        folder_path=str(input("The folder path that contain the images :"))
        width=int(input("Desired width :"))
        height=int(input("Desired Height :"))
    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")

        resize_picture()


    os.chdir(folder_path)
    size = (width, height)
    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/{width}x{height}-images")
    except:
        pass
    for image in os.listdir("."):
        filename, fileextension = os.path.splitext(image)
        if fileextension == "":
            print("This file has no extension ")
            continue
        curent_image = Image.open(image)
        curent_image.thumbnail(size)  # resize method that accepts a tuple (width,height)
        print(f"{filename} is resized into {width}x{height}")
        curent_image.save(f"{os.path.dirname(folder_path)}/{width}x{height}-images/{filename}-converted{fileextension}")
    print("Process is Successfully Done 😄")


if __name__ == '__main__':
    resize_picture()