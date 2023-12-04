def getPoints(dataLine: str) -> int:
    winningNumbers = set(dataLine.split(":")[1].split("|")[0].strip().split(" "))
    scratchCard = set(dataLine.split(":")[1].split("|")[1].strip().split(" "))

    if "" in winningNumbers:
        winningNumbers.remove("")

    if "" in scratchCard:
        scratchCard.remove("")

    # print(f"winningNumber Set: {winningNumbers}")
    # print(f"scratchCard Set: {scratchCard}")

    matchedNumber = winningNumbers.intersection(scratchCard)

    points = 2 ** (len(matchedNumber) - 1)
    # print(f"Points: {points}, matched numbers: {matchedNumber}")

    if len(matchedNumber) == 0:
        return 0
    return points


# Part 2
def howManyMatched(dataLine: str) -> int:
    winningNumbers = set(dataLine.split(":")[1].split("|")[0].strip().split(" "))
    scratchCard = set(dataLine.split(":")[1].split("|")[1].strip().split(" "))

    if "" in winningNumbers:
        winningNumbers.remove("")

    if "" in scratchCard:
        scratchCard.remove("")

    matchedNumber = winningNumbers.intersection(scratchCard)

    return len(matchedNumber)


with open(r"day4/inputData.txt") as rawData:
    lines = rawData.readlines()
    cardCounter = [0] * len(lines)


with open(r"day4/inputData.txt") as rawData:
    for idx, line in enumerate(rawData):
        # plus 1 for original card
        cardCounter[idx] += 1
        copies = howManyMatched(line)
        for i in range(idx + 1, idx + copies + 1):
            cardCounter[i] += cardCounter[idx]

        print(f"Card {idx+1}: copies: {copies} current counter: {cardCounter}")

print(sum(cardCounter))
