def Grade(scores):
    if scores == 49:
         print('your grade is E')
    elif scores <= 59:
        print('your grade is D')
    elif scores <= 69:
        print('your grade is C')
    elif scores <= 79:
        print('your grade is B')
    elif scores >=80:
        print('your grade is A')
    else:
        print('You failed the Exams')
Grade(scores = int(input('Enter your score: ')))
