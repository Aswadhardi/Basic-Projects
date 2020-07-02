import random
print('hello welcome to dice')
print()
start = input('DO YOU WANT TO ROLL THE DICE Y/N?: ')

if start.capitalize() == 'Y':
    dice = random.randint(1, 6)

    for i in range(1, 4):
        predict = int(input('Predict the outcome: '))
        n=i

        if predict < dice:
            print("the number you guessed is less than the dice outcome number")
        elif predict > dice:
            print("the number you guessed is greater than the dice outcome number")
        else:
            print('Dice outcome is equal to your prediction {0}'.format(dice))
            break
    if predict != dice:
        print('wrong prediction')
        print('dice outcome : {0} '.format(dice))
    else:
        print('You predicted {0} times before getting the  dice outcome :{1} '.format(n , dice))
else:
    print('''DICE WILL NOT BE ROLL
    YOU CANT PREDICT TOO
    HAVE A NICE TIME ''')
exit(input('press any key to exit'))
