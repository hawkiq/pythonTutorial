total = 0
order = int(input("Enter Order No. : "))
while True:
    num = int(input("Enter Price: "))
    if num > 0:
        total = total + num
        continue
    else:
        break
with open("result.txt","r") as f:
    #f.write("\nOrder Number: "+str(order) + " Total Price: "+ str(total))
    for line in f:
        print(line.upper())
#print(f.read())
print(f.closed)