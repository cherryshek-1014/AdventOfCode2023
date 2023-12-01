import re

wordToInt = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def findNumberInString(dataLine: str) -> list:
    regexFind = re.findall(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))", dataLine
    )
    return regexFind


def getCaliValue(numberList: list) -> int:
    firstVal = convertVal(numberList[0])
    lastVal = convertVal(numberList[-1])

    caliVal = int(str(firstVal) + str(lastVal))
    return caliVal


def convertVal(valInput):
    try:
        return int(valInput)
    except:
        return wordToInt[valInput]


sumCaliValue = 0

with open(r"Day1\Part1\inputData1.txt") as data:
    for line in data:
        cleanLine = line.rstrip()
        getNumbers = findNumberInString(cleanLine)
        caliValue = getCaliValue(getNumbers)
        sumCaliValue += caliValue

print(sumCaliValue)
