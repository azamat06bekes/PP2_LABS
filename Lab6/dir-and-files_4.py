import os

path = input("Enter a path: ")

if(os.path.exists(path)):
  if(os.path.isfile(path)):
    with open(path, 'r', encoding='utf-8') as file:
      line_cnt = len(file.readlines())
      print("Number of lines:", line_cnt)
  else:
    print("The path is a directory, not a file")
else:
  print("Path does not exist.")
