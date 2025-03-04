import shutil

source_file = input("Enter source file path: ").strip()
destination_file = input("Enter destination file path: ").strip()

try:
    shutil.copyfile(source_file, destination_file)
    print("File copied successfully.")
except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("Error:", e)
