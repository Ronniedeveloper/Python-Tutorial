from sys import argv
script, file_name = argv

print(f"Am going to open file for writing {file_name}")
input("ok?")

print("Opening file....")
target = open(file_name, "w+")

#print("Deleting content in file!")
#target.truncate()

print("Now im to ask for 3 lines")
print(f"and the 3 line are going to be written in {file_name}")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print(f"Writing {line1} {line2 } {line3}")
print(f"Now writing to file {file_name}........")
target.write(f"{line1}\n")
target.write(f"{line2}\n")
target.write(f"{line3}\n")

print(f"Opening the {file_name}")
print("Wait a sec.......")
print("a sec...........")
text = open(file_name)
print(text.read())