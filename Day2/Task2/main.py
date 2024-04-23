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
        decision=input("Do you want to play (yes/no)")
        while(decision.lower()=="yes"):
            elements=["Rock","Papper","Scizzor"]
            machine=random.choice(elements)
            user=input("Rock Papper Scizzor ").lower()
            if(machine.lower()==user):
                print(f"machine:{machine}\nuser:{user}\nThat was a tough call its a Tie")
                Rock_Papper_Scizzor()
            elif((machine.lower()=="rock") and (user=="scizzor") ):
                print(f"machine:{machine}\nuser:{user}\n Hah! I Won this time ")
                Rock_Papper_Scizzor()
            elif((machine.lower()=="papper") and (user=="rock") ):
                print(f"machine:{machine}\nuser:{user}\n Hah! I Won this time ")
                Rock_Papper_Scizzor()
            elif((machine.lower()=="scizzor") and (user=="papper") ):
                print(f"machine:{machine}\nuser:{user}\n Hah! I Won this time ")
                Rock_Papper_Scizzor()
            else:
                print(f"machine:{machine}\nuser:{user}\n You have won")
                Rock_Papper_Scizzor()
        else:
            print("thankyou for playing")
            main()
    except:
        print("please give the input according to the instructions you get\n Thankyou")
    

print("Welcome just type 1 or 2 to play the desired game or 3 to exit")
def main():
    print("If U dont want to play just type 'no'")
    play=int(input("Which game U want to play from the following\n1.Number Guessing\n2.Rock Papper Scizzor\n3.exit\n"))
    if(play==1):
        guess_the_number()
        n=input("Do u want to play again from start yes/no")
        if(n.lower()=="yes"):
            main()
    elif(play==2):
        Rock_Papper_Scizzor()
        n=input("Do u want to play again start yes/no")
        if(n.lower()=="yes"):
            main()
    else:
        print("Thankyou for playing the game")
main()

    
    