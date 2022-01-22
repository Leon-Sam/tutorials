def solution(xs):
    if len(xs) is 1:
        return str(xs[0])

    

    x=removeZeros(xs)
    if not x:
        return "0"

    x=sortValues(x)
    x=filterForMaxSumProduct(x)
    
    if not x:
        return str(xs[0])

    x=multiplyInputArray(x)
    
    return x

def removeZeros(inputArray):
    result=[]
    for s in inputArray:
        if int(s) is not 0:
            result.append(s)



    return result

def sortValues(inputArray):

    inputArray.sort()
    return inputArray

def filterForMaxSumProduct(inputArray):
    x=map(lambda x : x<0, inputArray)
    count = sum(x)
    if count%2 is not 0:    
        filtered=filter(lambda x: x<0, inputArray)
        filtered.sort(reverse=True)
        leastNegative=filtered[0]
        inputArray.remove(leastNegative)
        return inputArray
    else: 
        return inputArray
        
def multiplyInputArray(inputArray):

    sum=1

    for number in inputArray:
        sum*=number

    return str(sum)


x=solution([0]*50)
print(x)

x=solution([2, 0, 2, 2, 0])
print(x)

x=solution([2,-3,1,0,-5])
print(x)


x=solution([-2, -3, 4, -5])
print(x)   

x=solution([1000])
print(x)   

x=solution([1000]*50)
print(x)   

x=solution([0])
print(x)   

x=solution([-1,0]*3)
print(x)   

x=solution([-1,0])
print(x)   


x=solution([-1])
print(x)   