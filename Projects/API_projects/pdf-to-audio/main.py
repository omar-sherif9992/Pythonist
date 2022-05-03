import gtts
import os
import PyPDF2

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
def converter():
    folder_path = ""
    try:
        folder_path = str(input("The folder path that contain the PDFs :"))
    except:
        clear()
        print("Invalid input submitted ,Please Try again \n")
        converter()
    os.chdir(folder_path)
    try:
        os.makedirs(f"{os.path.dirname(folder_path)}/PDF-Audio-Files")
    except:
        pass
    language = 'en'

    for pdf in os.listdir("."):
        if pdf.endswith(".pdf"):
            filename, fileextension = os.path.splitext(pdf)
            with open(pdf,'rb') as file:
                pdfReader = PyPDF2.PdfFileReader(file)
                text_val = ""
                for i in range(0,pdfReader.numPages):
                    # creating a page object
                    pageObj = pdfReader.getPage(i)
                    text_val+=pageObj.extractText()
            # make a request to google to get synthesis
            t1 = gtts.gTTS(text=text_val, lang=language, slow=False)
            # play the aud io file
            # playsound("welcome.mp3")

            # save the audio file
            t1.save(f"{os.path.dirname(folder_path)}/PDF-Audio-Files/{filename}-converted.mp3")
        else:
            print("only PDF files are accepted")
    print("Process is Successfully Done 😄")


if __name__ == '__main__':
    converter()



