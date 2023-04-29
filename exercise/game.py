print("Before we play everything tell me about you?")
print("What\'s your name?")
name = input(">> ")

print(f"Hello {name} let\'s play a game!")
print("I,m gonna ask you something!")
print(f"Whats your lucky number today {name}!")

print("Think of a number starting from zero")
print("It might be like 2 or 4 anything!")
num = input(">>>")

if num == "2":
    print(f"Are you sure to go with your {num}!")
    print("Yes?......")
elif num == "4":
    print(f"You picked your luck number which is {num}")
    print("Your lucky today!")
else:
    print("Today is not your lucky day because you chose this number")
