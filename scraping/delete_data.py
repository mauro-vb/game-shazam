import os

def delete_vid(path):
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)

def delete_img(path):
    '''Deleting all files inside, then folder.
    Not using force deletion of folder to avoid problems'''

    # Delete all files inside
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)

    # Delete folder
    print(f"Deleting folder: {path}")
    os.rmdir(path, dir_fd = None)
