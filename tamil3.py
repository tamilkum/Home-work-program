class Person:
    def __init__(self,myname,game):
        self.myname=myname
        self.game=game
    def name(self):
        print(self.myname)

    def sports(self):
        print(self.game)



name=input("your name pls: ")
game=input("your fav game: ")
w1=Person(name,game)
print(w1.sports())
print(w1.name())