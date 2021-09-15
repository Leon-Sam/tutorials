import math

def solution(n):
    result='2'
    shouldContinue=True
    numb=3
    
    if (not isinstance(n,int)):
        return 'Wrong input type'

    if (n<0):
        return 'Please use non-negative number'

    while (shouldContinue): # Output all odd numbers up to N
        isPrime=True

        for testNumb in range(2,int(math.floor(math.sqrt(numb))+1)):
            if numb % testNumb == 0:
                isPrime=False

        if isPrime:
            result+=str(numb)
            
            if (len(result)>(n+5)):
                shouldContinue=False

        numb+=2 #Increment the number to next odd value
    return result[n:n+5]

print(solution(1))