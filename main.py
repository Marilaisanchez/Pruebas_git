def par_impar(n):
    return "par" if n % 2 == 0 else "impar"

a = int(input("Primer dígito: "))
b = int(input("Segundo dígito: "))

print(f"El primer dígito:{a} es {par_impar(a)}")
print(f"El segundo dígito: {b} es {par_impar(b)}")

