from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)
print(len(alphabet))


def caesar(text, shift, direction):
    result = ""
    if shift < 0:
        print("not allowed negative numbers")
        return None
    while shift >= len(alphabet):
        shift -= (len(alphabet))
    if direction == "decode":
        shift *= -1
    for letter in text:
        index = alphabet.index(letter)
        index = index + shift
        if index > len(alphabet):
            index = index - len(alphabet)
        while index < -1:
            index += len(alphabet)
        result += alphabet[index]
    print(result)


text = str(input("please enter the word"))
shift = int(input("shift by how much"))
direction = str(input("please enter the direction"))

caesar(text, shift, direction)
