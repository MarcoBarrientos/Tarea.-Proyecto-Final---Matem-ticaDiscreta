def euclides(a, b):
    while b != 0:
        print(f"{a} = {b} * {a // b} + {a % b}")
        a, b = b, a % b
    return a

num1 = 19
num2 = 35

print(f"Calculando el MCD de {num1} y {num2} usando el algoritmo de Euclides:")
mcd = euclides(num1, num2)
print(f"El MCD de {num1} y {num2} es {mcd}")
