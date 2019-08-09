import datetime
names = (input('PLEASE ENTER YOUR NAME: '),'kofi','kpogo','oriental')
for name in names:
    if name ==names[0]:
        print(name,'is at index of 0')
    if name ==names[1]:
        print(name,'is at index of 1')
    if name ==names[2]:
        print(name,'is at index of 2')
    if name ==names[3]:
        print(name,'is at index of 3')

nums = [10,3,4,5,7]
print(max(nums))
today = datetime.datetime.today()
print(today.day,today.month,today.year,today.hour,':',today.minute,today.second)
