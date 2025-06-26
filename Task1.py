n = int(input("n ni kiriting: "))

if n < 1:
    print("n 1 dan katta yoki teng bo'lishi kerak.")
else:
    yigindi = 0
    for i in range(1, n+1):
        yigindi += i ** i
    print("Yig'indi:", yigindi)