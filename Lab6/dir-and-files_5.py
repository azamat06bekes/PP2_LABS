path = input("Enter a path: ").strip()
my_list = list(input("Enter a list (comma-separated): ").split(","))

with open(path, 'w', encoding='utf-8') as file:
  file.writelines("\n".join(my_list))

print("List has been written to the file")
