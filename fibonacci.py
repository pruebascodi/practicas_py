def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

# Imprimir los primeros 25 números de la sucesión de Fibonacci
print("numeros fibonacci")
fibonacci(25)