print('THIS PROGRAM TAKES A LIST AND RETURNS THE TWO MINIMAL VALUES')
list = []
while len(list) !=6:
    name = int(input('Enter your list of numbers: '))
    #list.append(name)

    list.append(name)

else:
    print(list)
    list.sort()
    print('The FIRST Value is: ',list[0])
    print('The SECOND Value is: ',list[1])
