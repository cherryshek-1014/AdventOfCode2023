import re


def getNumberList(dataLine):
    return re.findall(r"\d+", dataLine)


def getNumberIndex(dataLine, number: str):
    return [dataLine.index(number), dataLine.index(number) + len(number) - 1]


def getVerticalCoords(x: int, y, operator, maxlen):
    yaxis = [y - 1, y, y + 1]
    coordsToCheck = set()
    if x <= 1 or x == maxlen:
        return set()
    for axis in yaxis:
        if axis >= 0:
            coordsToCheck.add((eval("x" + operator + "1"), axis))

    return coordsToCheck


def getHorizontalCoords(x: list, y: int):
    coordsToCheck = set()
    for xaxis in range(x[0], x[1] + 1):
        if y - 1 >= 1:
            coordsToCheck.add((xaxis, y - 1))
        if y + 1 >= 1:
            coordsToCheck.add((xaxis, y + 1))
    return coordsToCheck


def getSymbolCoords(data):
    symbolCoords = set()
    for yidx, line in enumerate(data):
        for xidx, value in enumerate(line):
            if not value.isnumeric() and value != ".":
                symbolCoords.add((xidx, yidx))
    return symbolCoords


# for line in data:
#     numberList = getNumberList(line)
#     if len(numberList) > 0:
#         for number in numberList:
#             numberIndex = getNumberIndex(line, number)

with open(r"day3/testData2.txt") as rawData:
    data = []
    for line in rawData:
        line = line.rstrip()
        data.append(line)


symbolCoords = getSymbolCoords(data)
maxlen = len(data[0]) - 1
totalPartNumber = 0
for idx, line in enumerate(data):
    getNumber = getNumberList(line)
    for number in getNumber:
        idxList = getNumberIndex(line, number)
        leftCoords = getVerticalCoords(idxList[0], idx, "-", maxlen)
        rightCoords = getVerticalCoords(idxList[1], idx, "+", maxlen)
        HorizontalCoords = getHorizontalCoords(idxList, idx)
        coordsToCheck = HorizontalCoords.union(*[leftCoords, rightCoords])
        # print(f"idx list: {idxList}")
        print(f"{number}: {coordsToCheck}")
        if len(symbolCoords.intersection(coordsToCheck)) > 0:
            totalPartNumber += int(number)


print(f"symbol coords: {symbolCoords}")
print(f"total part number: {totalPartNumber}")
