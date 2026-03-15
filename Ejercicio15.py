##Adivinar un número secreto
numero_secreto = 7 

n1 = int(input("Adivina el número secreto "))

while n1 != 7:
     n1 = int(input("Incorrecto, ingresa otro número  ")) 

print("Adivinaste el número secreto es:  ", numero_secreto)