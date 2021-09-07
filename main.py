import random


y='y'
a = random.randint(1,10)
print("Guessing game by Likhith")
print("Decided on a number between 1 to 10")
b=0
d=3
while y.lower()!='n':
    if b > 2:
        print("Sorry your chances are over :( " )
        print("The number was",a)
    else:
        n=int(input(f"Guess the Number(You Have {d} chances) :"))

        if a<n:
            print(f"lower than {n}")
            b=b+1
            d=3-b
            continue
        elif a>n:
            print(f"higher than {n}")
            b=b+1
            d=3-b
            continue
        elif a==n:
            print("Yay!!!!  You Guessed Right :)")
            print(f"The number is {n}!!")

    y = input("Do you want to play again:(y/n): ")
    if y.lower() =='y':
        b=0
        d=3
        a = random.randint(1, 10)
        print("Guessing game by Likhith")
        print("Decided on a number between 1 to 10")
print("Thanks for playing XD")



