class MyStuff(object):
    def __init__(self):
        self.name = "Ronnie Developer"
    def greeting(self):
        print("Hello everyone!")
    def biogaphy(self):
        self.name = self.name
        self.location = "Nsambya Avenue Block C"
        print(f"My name is {self.name} and i\'m from {self.location}")

class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
        self.title = title
    def sing_for_me(self):
        for lyric in self.lyrics:
            print(lyric)


user = MyStuff()

print("_"*15)
print(user.greeting())
print(user.biogaphy())
#print(user.name)

