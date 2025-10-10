def Small(string):
    counter = 0
    for ch in string:
        if ch.islower():
            counter += 1

    return counter

def Capital(string):
    counter = 0
    for ch in string:
        if ch.isupper():
            counter += 1

    return counter


def Vowel(string):
    counter = 0
    string2 = "aeiou"
    for ch in string:
        if ch in string2:
            counter += 1

    return counter

def Digit(string):
    counter = 0
    for ch in string:
        if ch.isdigit():
            counter += 1

    return counter

string = input("enter a string: ")
print("Small: ", Small(string))
print("Capital: ", Capital(string))
print("Vowel: ", Vowel(string))
print("Digit: ", Digit(string))






