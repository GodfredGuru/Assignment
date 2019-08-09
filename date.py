import datetime

myDate = datetime.datetime.now()
print(myDate)

lists = [1,2,3,4,5,6,7,8]
for list in lists:
    if list==3:
        print('yes the number is in',list)
        continue
#    print(list)


for num in range(1, 10):
    print(num)
