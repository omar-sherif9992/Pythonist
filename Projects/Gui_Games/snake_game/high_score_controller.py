
def clear_content(filename):
    with open(f"{filename}.txt",mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write("")

def read_content(filename):
    with open(f"{filename}.txt") as file:  # it opens a file without reading it's contents plus the word with it auto matically cose the file after it's body is finished and have the ability only to read
        contents = file.read()  # it reads the content of the file
        return contents
def append_content(filename,text):
    with open(f"{filename}.txt",mode="a") as file:  # it opens a file and have the ability only to append
        file.write(f"{text} \n") # this is appended text

def make_new_file(filename,file_content):
    with open(f"{filename}.txt",mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write(f"{file_content} \n")

def rewrite_content(filename,text):
    with open(f"{filename}.txt",mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write(f"{text} \n")











