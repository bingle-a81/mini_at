import os

def search_folder(folder,folder_name):
    for root, dirs, files in os.walk(folder):
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None


