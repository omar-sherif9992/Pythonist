import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator")
num_letters = int(input("please enter how many letters needed"))
num_symbols = int(input("please enter how many symbols needed"))
num_numbers = int(input("please enter how many numbers needed"))
password = ""
list = [num_letters, num_symbols, num_numbers]
flag = True
while flag:
    if list[0] == 0 and list[1] == 0 and list[2] == 0:
        break
    listIndex = random.randint(0, 2)
    if listIndex == 0 and list[0] != 0:
        password += str(letters[random.randint(0, len(letters) - 1)])
        list[0] -= 1;
    elif listIndex == 1 and list[1] != 0:
        password += str(symbols[random.randint(0, len(numbers) - 1)])
        list[1] -= 1
    elif listIndex == 2 and list[2] != 0:
        password += str(numbers[random.randint(0, len(symbols) - 1)])
        list[2] -= 1
print(password)
