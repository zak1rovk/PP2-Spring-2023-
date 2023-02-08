import random
 
def guess_the_number():
        print('Hello! What is your name?')
        name=input()
        print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    
        number=random.randint(1, 20)
        tries=0
        while True:
            print("Take a guess.")
            guess=int(input())
            tries+=1
            if guess>number:
                print("Your number is too high.")
            elif guess<number:
                print("Your number is too low.")
            else:
                break
        print("Good job, " + name + "! You guessed my number in " + str(tries) + " tries!")