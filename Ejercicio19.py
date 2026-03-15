##Mostrar los primeros N números pares 

N1 = int(input("Por favor ingresa cuantos números enteros se mostrarán: "))

for i in range(1, N1 + 1):
    par = i * 2
    print(par)