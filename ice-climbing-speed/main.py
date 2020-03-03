athletes = {}


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return -1, False


def floatTryParse(value):
    try:
        return float(value), True
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
    inputValue = input(
        "Please enter beep number and name like this: [BeepNumber,Name]: \n")
    inputValues = inputValue.split(",")
    if len(inputValues) != 2:
        inputValue = input(
            "Your input value must be like this: [BeepNumber,Name] \n")
        athleteBeepNumber, athleteName = getAthleteInfo()
    athleteBeepNumber, result = intTryParse(inputValues[0])
    athleteName = inputValues[1]
    if result == False:
        inputValue = input("BeepNumber must be a 'number' \n")
        athleteBeepNumber, athleteName = getAthleteInfo()

    return athleteBeepNumber, athleteName


def getResultValue(value):
    if value == "Fall":
        return 1000
    elif value == "Fs":
        return 2000
    elif value == "DNS":
        return 3000
    else:
        return value


def getResultText(value):
    if value == 1000:
        return "Fall"
    elif value == 2000:
        return "Fs"
    elif value == 3000:
        return "DNS"
    else:
        return str(value)


def getAthleteResults(beepNumber):
    results = (0.0, 0.0, 0.0)
    inputValue = input("Please input " + str(beepNumber) +
                       " results like  this: [Value,Value,Value] \n")
    inputValues = inputValue.split(",")
    if len(inputValues) != 3:
        print("Your Values format is not correct, Plase try again \n")
        results = getAthleteResults(beepNumber)
    value_1, result_1 = floatTryParse(getResultValue(inputValues[0]))
    value_2, result_2 = floatTryParse(getResultValue(inputValues[1]))
    value_3, result_3 = floatTryParse(getResultValue(inputValues[2]))
    if (not result_1) or (not result_2) or (not result_3):
        print("Your every value must be a number, Plase try again \n")
        results = getAthleteResults(beepNumber)
    return value_1, value_2, value_3


def getAthletesInfo(athletesCount):
    for i in range(athletesCount):
        hasBeepNumber = True
        while hasBeepNumber:
            athleteBeepNumber, athleteName = getAthleteInfo()
            hasBeepNumber = athleteBeepNumber in athletes
            if hasBeepNumber:
                print("Your BeepNumber is exist, please try again")
        athlete = (athleteName, 0.0, (0.0, 0.0, 0.0))
        athletes[athleteBeepNumber] = athlete


def setAthleteResults():
    for beepNumber, athlete in athletes.items():
        results = getAthleteResults(beepNumber)
        resultsList = list(results)
        resultsList.sort()
        athleteList = list(athlete)
        athleteList[1] = resultsList[0]
        athleteList[2] = results
        athletes[beepNumber] = tuple(athleteList)


def getSpaceChar(count):
    result = ""
    for i in range(count):
        result = result + " "
    return result


def printFinalResults():
    print("--------------------------------")
    print("Rank|BeepNumber|   Name   |Score")
    print("--------------------------------")
    rank = 0
    for beepNumber, athleteInfo in sorted(athletes.items(), key=lambda athlete: athlete[1]):
        rank = rank + 1
        print(str(rank) + getSpaceChar(4 - len(str(rank))) + "|" + str(beepNumber) + getSpaceChar(10 - len(str(beepNumber))) + "|" +
              athleteInfo[0] + getSpaceChar(10 - len(athleteInfo[0])) + "|" + getResultText(athleteInfo[1]))
    print("--------------------------------")


getAthletesInfo(getAthletesCount())
setAthleteResults()
printFinalResults()
