def factorial_recursivo(numero: int):
    # Caso base
    if numero == 1:
        return 1
    # Paso recursivo
    else:
        return numero * factorial_recursivo(numero-1)

print(factorial_recursivo(4))
# Salida: 6