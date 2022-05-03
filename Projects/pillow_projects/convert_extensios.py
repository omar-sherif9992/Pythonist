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


def picture_converter():
    """you give the folder path that contains the images  and the file type extension you like
    and it will create a folder of that filetype extension and the converted images into it """

    folder_path = ""
    filetype = ""
    try:
        folder_path = str(input("The folder path that contain the images :"))
        filetype = str(input("Desired file type :"))
    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        picture_converter()

    os.chdir(folder_path)
    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/{filetype}-images")
    except:
        pass

    for image in os.listdir("."):
        if image.endswith(".jpg") or image.endswith(".png"):
            curent_image = Image.open(image)
            filename, fileextension = os.path.splitext(image)
            print(f"{filename} is converted into {filetype} ")
            curent_image.save(f"{os.path.dirname(folder_path)}/{filetype}-images/{filename}-converted.{filetype}")
        else:
            print("only jpg or png images are accepted")
    print("Process is Successfully Done 😄")

if __name__ == '__main__':
    picture_converter()