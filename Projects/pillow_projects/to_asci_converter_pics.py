from PIL import Image
import os


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


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

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)
def to_asci_picture():
    folder_path = ""
    try:
        folder_path = str(input("The folder path that contain the images :"))

    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        to_asci_picture()

    os.chdir(folder_path)
    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/ASCI-images")
    except:
        pass
    new_width=100
    for image in os.listdir("."):
        if image.endswith(".jpg") or image.endswith(".png"):
            curent_image = Image.open(image)

            new_image_data = pixels_to_ascii(grayify(resize_image(curent_image)))
            # format
            pixel_count = len(new_image_data)
            ascii_image = "\n".join(
                [new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
            filename, fileextension = os.path.splitext(image)
            with open(f"{os.path.dirname(folder_path)}/ASCI-images/{filename}-asci_image.txt", "w") as f:
                f.write(ascii_image)
            print(f"{filename} is turned  into Black & white images ")
        else:
            print("only jpg or png images are accepted")
    print("Process is Successfully Done 😄")


if __name__ == '__main__':
    to_asci_picture()
