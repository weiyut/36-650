def pyramid(n):
    s = n - 1
    for i in range(n):
        for j in range(s):
            print(end = " ")
        for k in range(n-s):
            print('* ', end = "")
        print("\r")
        s-=1
        
pyramid(5)
pyramid(3)