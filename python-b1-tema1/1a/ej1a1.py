'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y 
-reciba como parámetro un valor numérico entero llamado 'fibonacci_number'
-devuelva el valor de la serie Fibonacci en esa posición.

Asimismo, 
    si el valor no es numérico, 
    o es menor a cero, 
se debe lanzar  una excepción ValueError("mensaje"), 
la cual puede incluir un mensaje que debería corresponder con el tipo de error durante la validación.

Ejemplo:
    Entrada:
    fibonacci(10)
    Salida:55
'''

def fibonacci(fibonacci_number):
    str_error = ""
    if not isinstance(fibonacci_number, int):    str_error = "error no int."
    elif fibonacci_number < 0:                  str_error = "error pos negatiu o zero."

    if(str_error):
       raise ValueError(str_error)

    else:
        if fibonacci_number == 0:   return 0
        if fibonacci_number == 1:   return 1

        else:
            seq_fibo=[]
            n1 = 0
            n2 = 1
            n3 = None
            for ordinal in range(2, fibonacci_number+1):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
            return(n3)
        

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
'''
f = fibonacci
print(f('1'))
print(f(-1))
print(f(0))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(6))
print(f(7))
print(f(8))
print(f(9))
print(f(10))
'''