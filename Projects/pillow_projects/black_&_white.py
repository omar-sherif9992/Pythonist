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
def filter_picture():
    folder_path = ""
    try:
        folder_path = str(input("The folder path that contain the images :"))

    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        filter_picture()

    os.chdir(folder_path)
    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/Black & White-images")
    except:
        pass

    for image in os.listdir("."):
        if image.endswith(".jpg") or image.endswith(".png"):
            curent_image = Image.open(image)
            filename, fileextension = os.path.splitext(image)
            print(f"{filename} is turned  into Black & white images ")

            curent_image.convert("L").save(f"{os.path.dirname(folder_path)}/Black & White-images/{filename}-converted{fileextension}")
        else:
            print("only jpg or png images are accepted")
    print("Process is Successfully Done 😄")


if __name__ == '__main__':
    filter_picture()