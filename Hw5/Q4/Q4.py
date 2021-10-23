def triangle(num):
    if num < 0:
        print('Invalid Input')
    elif isinstance(num, int):
        total = 0
        for i in range(1,num+1):
            total += i 
            layer = list(range(total-i+1,total+1))
            print(*layer)
    else:
        print('Invalid Input')
    
triangle(3)
triangle(6)
triangle(2.5)
triangle(-1)