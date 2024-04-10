import turtle

def dibujar_cuadrado(num_asteriscos):
    for _ in range(4):
        for _ in range(num_asteriscos):
            turtle.write("*", font=("Arial", 12, "normal"))  # Dibujar un asterisco
            turtle.forward(20)  # Longitud del lado de cada segmento de línea
        turtle.left(90)

# Obtener el número de asteriscos por lado del usuario
while True:
    try:
        num_asteriscos = int(input("Ingrese el número de asteriscos por lado (debe ser mayor o igual a 2): "))
        if num_asteriscos >= 2:
            break
        else:
            print("Error: El número de asteriscos debe ser mayor o igual a 2.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

# Configuración inicial
turtle.speed(1)  # Velocidad baja para visualizar mejor

# Dibujar cuadrado
dibujar_cuadrado(num_asteriscos)

# Mantener la ventana abierta
turtle.done()
