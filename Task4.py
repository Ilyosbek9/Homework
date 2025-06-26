import random # random sonni topish

n = int(input("n ni kiriting: "))
sirli_son = random.randint(1, n)

for urinish in range(1, 4):
    taxmin = int(input(f"{urinish}-urinish. Sonni toping: "))
    
    if taxmin == sirli_son:
        print("Winner!")
        break
    elif taxmin < sirli_son:
        print("Yuqoriroq son o'ylangan.")
    else:
        print("Pastroq son o'ylangan.")
else:
    print(f"Looser! To'g'ri javob: {sirli_son}")