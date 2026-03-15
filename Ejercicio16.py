##Validar una contraseña 
contraseña = "123Abc"

mensaje = input(str("Por favor ingresa la contraseña:  "))

while mensaje != contraseña:
    mensaje = input(str("Error, ingresa la contraseña correcta:  "))
print ("Contraseña correcta")
