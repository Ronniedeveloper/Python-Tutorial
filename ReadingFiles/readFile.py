from sys import argv
script, file_name = argv

text = open(file_name)
print(f"This is your file {file_name}")
print(text.read())

print("Enter the file again")
file_again = input(">>")
file = open(file_name)
print(file.read())
