gender = input('What is your gender? ')
if gender == 'male':
    length = input('how tall are you in centimeters? ')
    if length >= '155':
        weight = int(input('What is your weight? '))
        if weight <= 99:
            mustache = input('Do you have a mustace? ')
            if mustache == 'yes':
                tv = int(input('How much hours a day do you spent behind the tv? '))
                if tv <= 4:
                    shoes = int(input('how much pair of shoes do u have? '))
                    if shoes >= 8:
                        print('Congrats u can play as professor pimpel! ')
                    else:
                        print('sorry u cant play any of these rolls')
            elif mustache == 'no':
                tv = int(input('How much hours a day do you spent behind the tv? '))
                if tv >= 6:
                    shoes = int(input('how much pair of shoes do u have? '))
                    if shoes >= 7:
                        print('congrats u can play as the kolonel! ')
                    elif shoes <= 6:
                        print('congrats you can play as the dominee')

                

elif gender == 'female':
    length = input('how tall are you in centimeters? ')
    if length >= '155':
        weight = int(input('What is your weight? '))
        if weight <= 99:
            Heels = input('Do you wear heels? ')
            if Heels == 'yes':
                tv = int(input('How much hours a day do you spent behind the tv? '))
                if tv <= 4:
                    shoes = input('how much pair of shoes do u have? ')
                    if shoes >= 8:
                        print('Congrats u can play as professor Roodhart! ')
                    else:
                        print('sorry u cant play any of these rolls')
            elif Heels == 'no':
                tv = int(input('How much hours a day do you spent behind the tv? '))
                if tv >= 6:
                    makeup = int(input('how much makeup do u have? '))
                    if makeup >= 16:
                        print('congrats u can play as the Mw. de Wit! ')
                    elif makeup <= 15:
                        print('congrats you can play as the Blaauw')
        
else:
    print('idk wat u are...')