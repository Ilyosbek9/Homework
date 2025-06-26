for son in range(100, 1000):
    a = son // 100          
    b = (son // 10) % 10     
    c = son % 10            

    if (a == b != c) or (a == c != b) or (b == c != a):
        print(son)