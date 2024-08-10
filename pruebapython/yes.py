num1 = int(input("Ingrese el primero número: "))
num2 = int(input("Ingrese el primero número: "))


es_valida = (num1 % 2 == 0) and (num1 > 0) and (num1 > num2)

print(f"Número {num1} es par, positivo y el mayor que {num2} ? {es_valida}")
