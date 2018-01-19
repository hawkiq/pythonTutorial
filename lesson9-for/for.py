exp = [3200, 2300, 4000, 1590]
# total = exp[0] + exp[1]+exp[2]+exp[3]
# total = 0
# for price in exp:
# total = total + price
# print('Total : ',total)
# consoles = ['PS4','XBOX','PC','SEGA','ATARI']
# for i in range(len(consoles)):
# print('Location: ',i,'Item : ',consoles[i])
# locations = ['Chair','Bed','Kitchen','Drawer','Sofa']
# key = 'Kitchen'
# for location in locations:
# if key == location:
# print('Key Found in :',location)
# break
# else:
# print('Not found in',location)


numbers = [1, 2, 4, 7, 8, 9]
for number in numbers:
    if number % 2 == 0:
        continue
    else:
        print(number * number)
