import random
a= random.randint(1,100)
c=0
print("Welcome to the Number Guessing Game! I am thinking of a number between 1 and 100.")

while True :
    b=int(input("Enter your guess: "))
    c+=1

    if a>b:
        print("Too low! Try guessing a higher number : ",b)

    elif a<b :
        print("Too high! Try guessing a lower number : ",b)

    elif a==b:
        print("Congratulations! You guessed it right in",b)
        break

    else:
        print("Invalid input. Please enter a valid whole number : ",b)


print("You Had",c,"To Guess The Number")
