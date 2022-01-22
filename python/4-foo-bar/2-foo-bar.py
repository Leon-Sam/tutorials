def solution(n, b):
    length = 1
    hashmap = {}
    index = 1
    id = n
    hashmap[id] = 0
    while True:
        id = generateID(id, b)
        if id in hashmap:
            break
        else:
            hashmap[id] = index
            index += 1
    length = index - hashmap[id]
    return length


def generateID(n, b):
    k = len(n)
    nArray = [int(char) for char in n]
    n = int(n)
    x = int("".join([str(numb) for numb in sortNumberArray(nArray, "descending")]), b)
    y = int("".join([str(numb) for numb in sortNumberArray(nArray, "ascending")]), b)
    z = x - y
    z = intToBaseNString(z, b)
    z = padOutputString(z, k)
    return z


def sortNumberArray(numberArray, order="descending"):
    fullySorted = False

    while not fullySorted:

        fullySorted = True
        for index in range(len(numberArray) - 1):
            numb1 = numberArray[index]
            numb2 = numberArray[index + 1]

            if order == "descending" and numb1 < numb2:
                numberArray[index] = numb2
                numberArray[index + 1] = numb1
                fullySorted = False

            if order == "ascending" and numb1 > numb2:
                numberArray[index] = numb2
                numberArray[index + 1] = numb1
                fullySorted = False

    return numberArray


def intToBaseNString(numberInput, base):
    output = []
    while True:
        output.append(str(numberInput % base))
        numberInput = numberInput / base
        if numberInput < 1:
            break

    return "".join(output)[::-1]


def padOutputString(inputString, length):
    targetPadding = length - len(inputString)

    for i in range(targetPadding):
        inputString = "0" + inputString

    return inputString
