# THIS CODE TAKES A LIST OF ITEMS FROM THE USER AND DISPLAY THEM IF THE NO. OF ITMES IS EQUAL TO 5 THE ENTIRE LIST IS THEN DISPLAYED.
list = []
def Take():
    while len(list) !=4:
        name = input('Enter a Grocery Item: ')
        #list.append(name)

        list.append(name.capitalize())
        print('\nCURRENT LIST: ',list)

    else:
        print('\n Final Grocery Items: ',list)
Take()
