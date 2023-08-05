data = input("Enter the data to be encrypted: ")
key = int(input("Enter the key: "))

data_characters = list(data)
print(data_characters)

for i in data_characters:
    #print(ord(i), end=" ")
    if i == " ":
        print(" ", end="")
    elif ord(i) + key > 122 or ord(i) + key > 90 and ord(i) + key < 97:
        print(chr(ord(i)+key-26), end="")   
    else:
        print(chr(ord(i)+key), end="")