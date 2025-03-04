import os

def list_directories(path):
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

def list_files(path):
    return [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]

def list_all(path):
    return os.listdir(path)

path = input("Enter a path: ")

if os.path.exists(path):
    print("Directories:", list_directories(path))
    print("Files:", list_files(path))
    print("All files and directories:", list_all(path))
else:
    print("The specified path does not exist.")
