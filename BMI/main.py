def BMI():
    weight=float(input("Enter your weight"))
    height=float(input("Enter your height"))

    bmi=weight/height**2
    print(f"{bmi:.2f}")
    if(height>0 and weight>0):
        if(bmi<18.5):
            print("UnderWeight")
        elif(bmi>18 and bmi<=24):
            print("Wow Man You are so healthy")
        else:
            print("Obesity")
    else:
        print("Both Weight and height should be positive")
    q=input("Do U want to check Your BMI")
    if(q=="yes" or q=="YES"):
        BMI()
BMI()