    
table={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
}

def romanToInt( s: str) -> int:
    result=0
    for index,letter in enumerate(s):
        
        # Look up value via table
        result+=table[letter]
       # local+=table[letter]
        # Check if the previous value was smaller then deduct value
        if ( index !=0 and table[s[index-1]]<table[s[index]]):
            result-=table[s[index-1]]*2
            print(index,table[s[index-1]]*2)
          #  local-=table[s[index-1]]*2
        
       ## print(f'local {local} and index {index}')
    
    return result


print(romanToInt('MCMXCIV'))