rowNumber = 0
persianFirstName = 1
persianLastName = 2
englishFirstName = 3
englishLastName = 4
nationalCode = 5
mobileNumber = 6
jalaliBirthdate = 7
gregorianBirthdate = 8
province = 9
education = 10
amount = 11
gymName = 12


def getPersianFirstName(row):
    result = True
    value = ""
    try:
        value = row[persianFirstName]
    except:
        result = False
    return result, value


def getPersianLastName(row):
    result = True
    value = ""
    try:
        value = row[persianLastName]
    except:
        result = False
    return result, value


def getEnglishFirstName(row):
    result = True
    value = ""
    try:
        value = row[englishFirstName]
    except:
        result = False
    return result, value


def getEnglishLastName(row):
    result = True
    value = ""
    try:
        value = row[englishLastName]
    except:
        result = False
    return result, value


def getNationalCode(row):
    result = True
    value = ""
    try:
        value = str(row[nationalCode])
        result = value.isnumeric()
        result = len(value) == 10
    except:
        result = False
    return result, value


def getMobileNumber(row):
    result = True
    value = ""
    try:
        value = str(row[mobileNumber])
        result = value.isnumeric()
    except:
        result = False
    return result, value


def getJalaliBirthdate(row):
    result = True
    value = ""
    try:
        value = row[jalaliBirthdate]
    except:
        result = False
    return result, value


def getGregorianBirthdate(row):
    result = True
    value = ""
    try:
        value = row[gregorianBirthdate]
    except:
        result = False
    return result, value


def getProvince(row):
    result = True
    value = ""
    try:
        value = row[province]
    except:
        result = False
    return result, value


def getEducation(row):
    result = True
    value = ""
    try:
        value = row[education]
    except:
        result = False
    return result, value


def getAmount(row):
    result = True
    value = ""
    try:
        value = str(row[amount])
        result = value.isnumeric()
    except:
        result = False
    return result, value


def getGymName(row):
    result = True
    value = ""
    try:
        value = row[gymName]
    except:
        result = False
    return result, value
