def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return -1, False

def getAthletesCount():
    inputValue = input("Please enter the number of athletes: \n")
    athletesCount, result = intTryParse(inputValue)
    if result == False:
        print("Your input value must be a 'number' \n")
        athletesCount = getAthletesCount()
    return athletesCount

def getAthleteInfo():
    athleteBeepNumber = 0
    athleteName = ""
    inputValue = input("Please enter beep number and name: \n")
    inputValues = inputValue.split(",")
    if len(inputValues) != 2:
        inputValue = input("Your input value must be like this: [BeepNumber,Name] \n")
        athleteBeepNumber, athleteName = getAthleteInfo()
    athleteBeepNumber, result = intTryParse(inputValues[0])
    athleteName = inputValues[1]
    if result == False:
        inputValue = input("BeepNumber must be a 'number' \n")
        athleteBeepNumber, athleteName = getAthleteInfo()
    
    return athleteBeepNumber, athleteName

athletesCount = getAthletesCount()
print("athletesCount:" + str(athletesCount))
for i in range(athletesCount):
    athleteBeepNumber, athleteName = getAthleteInfo()
    print("athleteBeepNumber:" + str(athleteBeepNumber))
    print("athleteName:" + athleteName)
