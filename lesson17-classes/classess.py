class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def work(self):
        if self.occupation == "singer":
            print(self.name, " Singing at parties")
        else:
            print(self.name, " Playing football")

    def speak(self):
        if self.occupation == "singer":
            print(self.name, " I won many Music awards")
        else:
            print(self.name, " I have 5 titles")

print(__name__)

if __name__ == "__main__":
    amr = Human("Amr Diab", "singer")
    amr.work()
    amr.speak()
    misse = Human("Lionel Misse", "player")
    misse.speak()
    misse.work()
