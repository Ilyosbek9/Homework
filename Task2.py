age = int(input("Yoshingizni kiriting: "))

if age > 0 and age < 201:
    for i in range(1, age):
        print(i)

    print(f"{age} - Bu sizning yoshingiz!")

    for i in range(age + 1, 201):
        print(i)
else:
    print("Bunday qiymat bo'lishi mumkin emas!")