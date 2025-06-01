import time

start = time.time() # medición de tiempo de ejecución
user_num = 40

print("::: SERIE DE FIBONACCI :::\n")
# calcula de forma recursiva el número de la secuencia de Fibonacci según la posición indicada en el parámetro "num"
def fibonacci(num):
    if num == 0 or num == 1:    # caso base. si se cumple, retorna el parámetro "num"
        return num
    else:                       # a partir de ser mayor a 1, se llama a sí misma para calcular el valor según la suma de sus dos anteriores
        return fibonacci(num - 1) + fibonacci(num - 2)   

# imprime la serie de Fibonacci desde la posición 0 hasta 'num', utilizando recursión.
def mostrar_serie(num):
    if num >= 0:
        mostrar_serie(num - 1)
        print(f"Posición {num} - Valor {fibonacci(num)}") # al volver de la recursión, se imprime la posición y el valor

# ejecuta el cálculo y muestra los resultados
print(f"En la posición nro {user_num}, el valor en la serie de Fibonacci es {fibonacci(user_num)}.")
print(f"Serie de Fibonacci completa hasta la posición {user_num}: ")
mostrar_serie(user_num)

print("\n--")
end = time.time()
print(f"Tiempo total de ejecución: {end - start:.2f} segundos.")
print("--")


