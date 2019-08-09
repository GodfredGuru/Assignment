scores = int(input('ENTER YOUR SCORE TO SEE YOUR GRADE: '))
if scores in range(1,50):
    print('your grade is  E')
elif scores==50:
    print('your grade is  D')
elif scores in range(50,61):
    print('your grade is  C')
elif scores in range(61,71):
    print('your grade is  B')
elif scores in range(71,101):
    print('your grade is  A')
