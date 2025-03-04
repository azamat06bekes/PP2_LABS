text = input("Enter a string: ")

list_upper = []
list_lower = []

for char in text:
  if(char.isupper() == True):
    list_upper.append(True)
    
  elif(char.islower() == True):
    list_lower.append(True)

  else:
    continue

cnt_upper = sum(list_upper)
cnt_lower = sum(list_lower)

print("Number of upper case letters:", cnt_upper)
print("Number of lower case letters:", cnt_lower)
