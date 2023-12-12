import random 
n = 99
mass_1 = [random.randint(0, 100) for i  in range(n)] 
mass_2 = [random.randint(0, 100) for i  in range(n)] 
mass_3 = [random.randint(0, 100) for i  in range(n)] 
print(mass_1) 
print(mass_2) 
print(mass_3) 
print(max(mass_1+mass_2+mass_3)) 
print(sum(mass_1+mass_2+mass_3))