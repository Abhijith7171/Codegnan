import random
def guess_the_number():
    try:
        n=int(input("upto which number you want to play the guessing game"))
        machine=random.randint(1,n)
        user=int(input("Enter the number that you have guessed: "))
        attempts=1
        while(True):
            if(machine==user):
                if(attempts>1):
                    print(f"Hurrah! You have guessed the correct number in {attempts} attempts")
                    break
                elif(attempts==1):
                    print(f"Hurrah! You have guessed the correct number in Single attempt")
                    break
            elif(machine>user):
                attempts+=1
                print(f"You have to guess a number greater than {user}")
                user=int(input("Enter the number that you have guessed: "))
            elif(machine<user):
                attempts+=1
                print(f"You have to guess a number less than {user}")
                user=int(input("Enter the number that you have guessed: "))
    except:
        print("Print please give the input according to the instructions you get\n Thankyou")
    
# guess_the_number()
def Rock_Papper_Scizzor():
    try:
        while(True):
            elements=["Rock","Papper","Scizzor"]
            machine=random.choice(elements)
            user=input("Rock Papper Scizzor ").lower()
            if(machine.lower()==user):
                print(f"machine:{machine}\nuser:{user}\nThat was a tough call its a Tie")
            elif((machine.lower()=="rock") and (user=="scizzor") ):
                print(f"machine:{machine}\nuser:{user}\n Hah! I Won this time ")
            elif((machine.lower()=="papper") and (user=="rock") ):
                print(f"machine:{machine}\nuser:{user}\n Hah! I Won this time ")
            elif((machine.lower()=="scizzor") and (user=="papper") ):
                print(f"machine:{machine}\nuser:{user}\n Hah! I Won this time ")
            else:
                print(f"machine:{machine}\nuser:{user}\n You have won")
            play_again = input("Do you want to play again? (yes/no) ").lower()
            if play_again != "yes":
                break
    except:
        print("please give the input according to the instructions you get\n Thankyou")
    


def main():
    print("Welcome! Choose a game to play:")
    while True:
        try:
            choice = int(input("1. Number Guessing\n2. Rock Paper Scissors\n3. Exit\nEnter your choice: "))
            if choice == 1:
                guess_the_number()
            elif choice == 2:
                Rock_Papper_Scizzor()
            elif choice == 3:
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except:
            print("please enter the correct values")
    
main()

    
    