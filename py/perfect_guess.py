import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    
    a=int(input("Guess a number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
    guesses+=1

print(f"You guess the number {n} correctly in {guesses} attempts")     