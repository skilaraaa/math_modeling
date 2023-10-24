a = 1
b = 1
n = int(input("Введите киоличество чисел"))	

for i in range(n):
  
    c = a + b
    a = b
    b = c

    print(c, end=' ')