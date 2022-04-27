i = 30

while i <= 60:
    j = 2
    isPrime = False
    
    while j < i:
        if i % j == 0:
            break
        j += 1
        
    if i == j:
        isPrime = True
        
    if isPrime:
        print('prime')
    else:
        print(i)
        
    i += 1
