import random

print("ENTER 2 NUMBER TO FIND A RANDOM NUMBER IN THEIR RANGE ")
A = int(input("ENTER FIRST NUMBER: "))
B = int(input("ENTER SECOND NUMBER: "))
secret = random.randint(A,B)

for i in range(1,4):
    guess = int(input("GUESS A NUMBER IN BETWEEN THE 2 NUMBERS: "))
    if guess < secret:
        print("the number you guessed is less than the secret number")
    elif guess > secret:
        print("the number you guessed is greater than the secret number")
    else:
        break
if guess == secret:
    print("you guessed the right number")
else:
    print("the secret number is ", secret)


print("THANK YOU")
q=input("Press any key to exit")


