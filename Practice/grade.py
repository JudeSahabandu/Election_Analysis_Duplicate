#What is the score?

score = int(input("What is your test score?"))

if score >= 90:
    print ("Your grade is an A")
else:
    if score >= 80:
        print ("Your grade is a B")
    else:
        if score >=70:
            print ("Your grade is an C")
        else:
            if score >=60:
                print ("Your grade is an D")
            else:
                print ("Your grade is an F")