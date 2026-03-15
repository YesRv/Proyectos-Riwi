##Mayor de tres números 
num1 = int(input("Por favor ingresa un número entero  "))
num2 = int(input("Ahora ingresa otro número entero  "))
num3 = int(input("Ahora ingresa otro número entero  "))

if num1 >= num2 and num1 >= num3:
    print("El número mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El número mayor es:", num2)
else:
    print("El número mayor es:", num3)