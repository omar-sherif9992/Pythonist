def clear_content(filename):
    with open(f"{filename}.txt",
              mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write("")


def read_content(filename):
    with open(
            f"{filename}") as file:  # it opens a file without reading it's contents plus the word with it auto matically cose the file after it's body is finished and have the ability only to read
        contents = file.read()  # it reads the content of the file
        return contents


def append_content(filename, text):
    with open(f"{filename}.txt", mode="a") as file:  # it opens a file and have the ability only to append
        file.write(f"{text} \n")  # this is appended text


def make_new_file(filename, file_content):
    with open(f"{filename}.txt",
              mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write(f"{file_content} \n")


def rewrite_content(filename, text):
    with open(f"{filename}.txt",
              mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write(f"{text} \n")


##here ive read a file from the Desktop folder using the absolute file path

i = read_content("/home/omar/Desktop/new_file", )
print(i)

##here ive read a file from the Desktop folder using the relative file path ./ means in current folder ../ go to parent foldeer
k = read_content(
    "../../../../Desktop/new_file")  # went to parent folder : project folder then parent folder : python-projects then parent folder : pycharm_projects then parent folder : home then desktop folder
print(k)
