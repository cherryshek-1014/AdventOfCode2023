import re


def findNumberInString(dataLine: str) -> list:
    regexFind = re.findall(r"\d", dataLine)
    numberList = list(map(int, regexFind))
    return numberList


def getCaliValue(numberList: list) -> int:
    firstVal = numberList[0]
    lastVal = numberList[-1]

    caliVal = int(str(firstVal) + str(lastVal))
    return caliVal


sumCaliValue = 0

with open(r"Day1\inputData1.txt") as data:
    for line in data:
        cleanLine = line.rstrip()
        getNumbers = findNumberInString(cleanLine)
        caliValue = getCaliValue(getNumbers)
        sumCaliValue += caliValue

print(sumCaliValue)
