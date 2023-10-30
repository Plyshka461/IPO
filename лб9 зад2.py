import my_module
N = int(input("Введите число N: "))
pairs = my_module.poisk_druzei(N)
print("Пары дружественных чисел:")
for pair in pairs:
    print(pair)