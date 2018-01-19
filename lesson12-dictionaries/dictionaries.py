dictionary = {}
def read_dic(dic):
    for k,v in dic.items():
        print(k,v)

while True:
    name = input('Enter Name: ')
    age = int(input('Enter Age: '))
    dictionary[name] = age
    con = input('Continue(Y/N): ')
    if con.lower() == 'y':
        continue
    else:
        break
read_dic(dictionary)
#print(dictionary)

#point = (30,41)
#print(point[1])





