def read_content(filename):
    with open(
            f"{filename}.txt") as file:  # it opens a file without reading it's contents plus the word with it auto matically cose the file after it's body is finished and have the ability only to read
        contents = file.read()  # it reads the content of the file
        return contents


def read_names(filename):
    file = open(f"{filename}.txt", "r")
    content = file.readline()
    names = []
    while content != "":
        content.strip("\n")
        names.append(content)
        content = file.readline()

    file.close()
    return names


def new_mails(filename, file_content):
    with open(f"/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/Mail Merge Project Start/Output/ReadyToSend/{filename}.txt",
            mode="w") as file:  # it opens a new file that didnt exist before  and have the ability only to write over it deleting the old file content
        file.write(f"{file_content}")


def create_mails():
    names = read_names(
        "/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/Mail Merge Project Start/Input/Names/invited_names")

    content = read_content(
        "/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/Mail Merge Project Start/Input/Letters/starting_letter")
    for name in names:
        mail = content.replace("[name]", name.strip())
        new_mails(f"To {name}", mail)


create_mails()
