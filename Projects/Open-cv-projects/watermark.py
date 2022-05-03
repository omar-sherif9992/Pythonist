# https://www.youtube.com/watch?v=rrh-4NtuK-w
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from past.builtins import raw_input


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


def show_image(file_path:str):
    # read image
    image = Image.open(file_path)
    # this open the photo viewer
    #image.show()
    plt.imshow(image)
    x_location = int(input("Specifies the center of the logo on the x-axis of the selected image :"))
    y_location = int(input("Specifies the center of the logo on the y-axis of the selected image:"))
    _ = raw_input("Press [enter] to continue.")

    plt.close('all')
    return (x_location,y_location)


def watermark_picture():
    folder_path = ""
    logo_path=""
    try:
        folder_path ="/home/omar/PycharmProjects/Python-Project/learning/pillow-learn/images" #str(input("The folder path that contain the images :"))
        logo_path="/home/omar/PycharmProjects/Python-Project/learning/pillow-learn/images"#str(input("The logo path :"))

    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        watermark_picture()

    os.chdir(folder_path)
    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/watermarked-images")
    except:
        pass


    for image in os.listdir("."):
        if image.endswith(".jpg") or image.endswith(".png"):
            try:
                img_path=f"{folder_path}/{image}"
                curent_image = cv.imread(img_path)
                print(img_path)
                w_img=curent_image.shape[1]
                h_img=curent_image.shape[0]
                print("/home/omar/PycharmProjects/Python-Project/learning/pillow-learn/images")

                print(show_image(file_path=image))
                # logo_img = cv.imread(filename=logo_path)
                # h_logo, w_logo = logo_img.shape
            except:
                clear()
                print("sssInvalid input submitted ,Please Try again \n")
                watermark_picture()

            filename, fileextension = os.path.splitext(image)
            print(f"{filename} is turned  into Watermarked image ")

            #curent_image.convert("L").save(f"{os.path.dirname(folder_path)}/Black & White-images/{filename}-converted{fileextension}")
        else:
            print("only jpg or png images are accepted")
    print("Process is Successfully Done 😄")


if __name__ == '__main__':
    watermark_picture()