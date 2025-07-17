import random
import time

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pregunta = int(input("De cuantos caracteres desea que sea tu variable: "))

password = ""

for i in range(pregunta):
    passwordale = random.choice(caracteres)
    password += passwordale
print("Creando la contraseña...")
time.sleep(1)
print("Tu contraseña es :",password)