a = int(input("Введите первую сторону"))
b = int(input("Введите второю сторону"))
c = int(input("Введите третью сторону"))
 
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b or b == c or c == a: 
        print("равнеобедренный")
    if a == b == c : 
        print("равносторонний")
    if a != b != c : 
        print("разносторонний")
else:

    print("Треугольник не существует")   