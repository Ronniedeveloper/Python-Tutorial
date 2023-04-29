from sys import argv

script, user_name = argv

print(f"Hi there {user_name}, wanna ask you something with the {script}?")
print(f"And you can tell me everything {user_name}")
print(f"Do you like me {user_name}")
like = input(">> ")

print("Where do you stay?")
live = input(">> ")

print(f"""Thank you {user_name} for letting us know that you 
stay in {live} and you love me {like}""")
