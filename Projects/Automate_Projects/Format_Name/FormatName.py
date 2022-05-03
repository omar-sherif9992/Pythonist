def format_name(f_name, l_name):
    """ Take a Kayne-tkinter-app and last name and format it to return the capitalized form."""
    if f_name == "" or l_name == "":
        return "invalid input"
    return (f"{f_name} {l_name}".title())


print(format_name("omar", "nour"))
