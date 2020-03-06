# Task_1

userName = input("What is your name?\n")
userSurname = input("What is your surname?\n")
print(f"Hello, {userName} {userSurname}!")
userAge = input ("How old are you?\n")
print(f"Your age is {userAge} years old!\n")
#
# Task_2

timeInput = input("Enter time in seconds\n")
timeInput = int(timeInput)
hours = timeInput // 3600
minutes = (timeInput // 60) % 60
seconds = timeInput % 60
if hours < 10:
    spaceHours = 0
else: spaceHours = ''
if minutes < 10:
    spaceMin = 0
else: spaceMin = ''
if seconds < 10:
    spaceSec = 0
else:
    spaceSec = ''
print(str('Time in hours is ')+str(spaceHours)+str(hours)+':'+str(spaceMin)+str(minutes)+':'+str(spaceSec)+str(seconds))

# Task_3

userNumber = input("Insert the number 'n'\n")
userNumber = int(userNumber)
SecUserNumber = str(userNumber)*2
ThrUserNumber = str(userNumber)*3
SecUserNumber = int(SecUserNumber)
ThrUserNumber = int(ThrUserNumber)
SumUserNumber = userNumber + SecUserNumber + ThrUserNumber
print(f"{userNumber} + {SecUserNumber} + {ThrUserNumber} =",SumUserNumber)

# Task_4

while (True):
    usNum = input("Enter a number from 0 to 100.000\n")
    if usNum.isdigit():
        usNum = int(usNum)
        if usNum < 10:
            fNum = usNum // 10
            print(fNum)
            break
        elif usNum < 100:
            fNum = usNum // 10
            sNum = usNum % 10
            print(fNum, sNum)
        elif usNum < 1000:
            fNum = usNum // 100
            sNum = usNum % 100 // 10
            tNum = usNum % 10
            print(fNum, sNum, tNum)
            break
        elif usNum < 10000:
            fNum = usNum // 1000
            sNum = usNum % 1000 // 100
            tNum = usNum % 100 // 10
            foNum = usNum % 10
            print(fNum, sNum, tNum, foNum)
            break
        elif usNum < 100000:
            fNum = usNum // 10000
            sNum = usNum % 10000 // 1000
            tNum = usNum % 1000 // 100
            foNum = usNum % 100 // 10
            fiNum = usNum % 10
            print(fNum, sNum, tNum, foNum, fiNum)
            break
        else: print ("You entered number more than 100.000")
    else:
        print("You entered not a number")

# Task_5

while(True):
    revenu = input("Enter company revenu\n")
    costs = input("Enter company costs\n")
    employers = input("Enter the numbers of employees\n")
    if revenu.isdigit() and costs.isdigit() and employers.isdigit():
        revenu = int(revenu)
        costs = int(costs)
        employers = int(employers)
        break
    else:
        print("Enter number from 1 to 100.000.000")
revenueProfit = round(revenu / costs,2)
profitEmpl = round(revenu / employers,2)

if revenu > costs:
    print(f"The company works profitably! The profitability of the company's revenues is {revenueProfit}.\nProfit per employee is {profitEmpl}.")
else:
    print(f"The company is operating at a loss. Profit per employee is {profitEmpl}.")

# Task_6

while True:
    distance = input("Enter the distance of the first day in km\n")
    desDistance = input("Enter the desired distance in km\n")
    if desDistance.isdigit() and distance.isdigit():
        distance = int(distance)
        desDistance = int(desDistance)
        break
    else:
        print("Enter distances by numbers")
day = 1
nDistance = distance

while nDistance < desDistance:
    nDistance = round(nDistance * 1.1, 2)
    day = day + 1
    print(f"Day {day} - {nDistance} km.")
print(f"On Day {day} the athlete achieved a result of at least {desDistance} km.")

