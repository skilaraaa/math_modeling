a = int(input("Введите первое число"))
b = int(input("Введите количество чисел"))
c = int(input("Введите значенатель прогресии"))
	
for i in range(c):
    print(a, end=' ')
    a = c * b
    c = a


    