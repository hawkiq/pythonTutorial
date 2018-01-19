class Resterant:
    menu = {
        'meat':20000,'flafel':750,
        'water':250,'egg':500,
        'potato':1500,'rice':3000,
        'tea':1000,'bacha':25000
    }
    def __init__(self):
        self.total = 0
        self.items = {}

    def add(self,item,count):
        self.items[item] = count
        self.total += (self.menu[item] * count)

    def print_bill(self,service):
        service = (service/100)* self.total
        total = self.total + service

        for item in self.items:
            print(f'{item:20} {self.menu[item]} x {self.items[item]}')

        print("=================================")
        print(f"{'Service':20} {service}")
        print(f"{'Total':20} {total}")