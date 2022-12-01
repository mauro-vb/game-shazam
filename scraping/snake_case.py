import string

def snake(name:str):
    name = name.translate(str.maketrans(
    dict.fromkeys(string.punctuation, '')))
    # Snake Case
    name = '_'.join(name.replace('_', ' ').split()).lower()
    # Remove punctuation
    return name


# TEST:
# print(snake("Call of Duty: Black Ops!"))
