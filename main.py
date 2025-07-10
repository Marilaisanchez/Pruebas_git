def calcular(a, b):
    return a + b, a - b, a / b if b else None

a = int(input("Primer dígito: "))
b = int(input("Segundo dígito: "))

s, r, d = calcular(a, b)
print("Suma:", s, "Resta:", r, "División:", d if d is not None else "Error")


