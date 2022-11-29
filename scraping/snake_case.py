def snake(name:str):
    return '_'.join(name.replace('_', ' ').split()).lower()

# TEST:
# print(snake("Mortal Kombat"))
