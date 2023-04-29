top = 0
nums = []
while top < 14:
    nums.append(top)
    top = top + 2
print(f"{nums}")

ten_things = "Let me go to the beach with you"
splitted = ten_things.split(' ')

sentence = ["Apple","Melon","Orange","Mango"]
while len(splitted) != 10:
    next_one = sentence.pop()
    splitted.append(next_one)
print(f"All splitted {splitted}")

print(splitted.pop(), splitted)
print(splitted.append("Guava"), splitted)