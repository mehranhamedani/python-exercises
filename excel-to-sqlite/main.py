import pandas as pd
import helper as helper
import dto as dto


def getExcelFile():
    while True:
        try:
            filePath = input("Please enter AthleteInfos excel file path:")
            return pd.read_excel(filePath)
        except:
            print("Your file path doesn't valid, please try again \n")


def getAthleteFromExcelFile(excelFile):
    hasError = True
    message = ""
    athletes = []
    for rowIndex in excelFile.index:
        row = excelFile.loc[rowIndex].tolist()
        result, persianFirstName = helper.getPersianFirstName(row)
        if result != True:
            hasError = False
            message += "persianFirstName in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, persianLastName = helper.getPersianLastName(row)
        if result != True:
            hasError = False
            message += "persianLastName in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, englishFirstName = helper.getEnglishFirstName(row)
        if result != True:
            hasError = False
            message += "englishFirstName in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, englishLastName = helper.getEnglishLastName(row)
        if result != True:
            hasError = False
            message += "englishLastName in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, nationalCode = helper.getNationalCode(row)
        if result != True:
            hasError = False
            message += "nationalCode in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, mobileNumber = helper.getMobileNumber(row)
        if result != True:
            hasError = False
            message += "mobileNumber in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, jalaliBirthdate = helper.getJalaliBirthdate(row)
        if result != True:
            hasError = False
            message += "jalaliBirthdate in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, gregorianBirthdate = helper.getGregorianBirthdate(row)
        if result != True:
            hasError = False
            message += "gregorianBirthdate in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, province = helper.getProvince(row)
        if result != True:
            hasError = False
            message += "province in row " + str(rowIndex) + " doesn't valid \n"
        result, education = helper.getEducation(row)
        if result != True:
            hasError = False
            message += "education in row " + \
                str(rowIndex) + " doesn't valid \n"
        result, amount = helper.getAmount(row)
        if result != True:
            hasError = False
            message += "amount in row " + str(rowIndex) + " doesn't valid \n"
        result, gymName = helper.getGymName(row)
        if result != True:
            hasError = False
            message += "gymName in row " + str(rowIndex) + " doesn't valid \n"
        athlete = dto.Athlete(persianFirstName, persianLastName, englishFirstName, englishLastName, nationalCode,
                              mobileNumber, jalaliBirthdate, gregorianBirthdate, province, education, amount, gymName)
        athletes.append(athlete)
    return hasError, message, athletes


athleteInfosExcelFile = getExcelFile()
result, messsage, athletes = getAthleteFromExcelFile(athleteInfosExcelFile)
print(messsage + "\n")
