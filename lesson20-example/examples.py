import RestMenu as rest
if __name__ == "__main__":
    table = rest.Resterant()
    while True:
        item = input("Enter Item: ")
        if item in table.menu:
            count = int(input("Enter Count: "))
            more = input("More items to buy? ")
            table.add(item,count)
            if more.lower() == 'y':
                continue
            else:
                break
        else:
            print("Item not found in Menu")
            continue

    table.print_bill(2)