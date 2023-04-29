def how_old(full_name):
    greeting = "Hello " + full_name
    print(f"{greeting} how are you!")
how_old("Ronnie Developer")

def biography(name,age,loc):
    about = f"My name is {name} and im {age} years old"
    print(f"{about} and i stay in {loc}")
biography("Ronie",20,"Nsambya")

def area(x, y):
    return x * y * y
area(4,6)

def split_words():
    word = "Get me wrong or not"
    sort = word.split(".^.")
    print(f"{sort}")
    print(word)
split_words()
def sort_words():
    words = "Ladies and gentlemen straight"
    print(sorted(words))
sort_words()