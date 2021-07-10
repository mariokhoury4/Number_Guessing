import random

number = random.randint(1,100)
guess = 7
print("You have 7 guesses to found the Random Number")
predicted = int(input("Enter a Number between 1and 100: "))
while (guess > 0):
    if (predicted < number):
        predicted = int(input("The Number is bigger: "))
    elif (predicted > number):
        predicted = int(input("The Number is smaller: "))
    else:
        print("You Found the number and still have: " + str(guess) + " guess")
        break
    guess -= 1

if(guess == 0):
    print("You have lost the game and don't have any more guess")
        
