import lec_3_ypr_4 as l4
a = int(input("Первый столбец"))
b = int(input("Второй столбец"))
for i in range(l4.N):
    l4.NxM[i,a], l4.NxM[i,b] = l4.NxM[i,b], l4.NxM[i,a]
print(l4.NxM[i])