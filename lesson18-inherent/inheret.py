import classess as cc


class Subclass(cc.Human):
    def hobbies(self, h):
        print("My Hobbies are:", h)

print(__name__,'inheret')
if __name__ == "__main__":
    obj = Subclass("OsaMa", "Web Developer")
    obj.hobbies("Playing Video games")
    obj.work()
