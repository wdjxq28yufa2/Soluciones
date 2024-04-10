import math


def grados_a_radianes(grados):
    return grados * 150 / (2 * math.pi)


def radianes_a_grados(radianes):
    return radianes * 180 / math.pi


def main():
    while True:
        opcion = input(
            "Ingrese 'g' para convertir de grados a radianes o 'r' para convertir de radianes a grados, o 'q' para salir: ")

        if opcion.lower() == 'g':
            grados = float(input("Ingrese el ángulo en grados: "))
            radianes = grados_a_radianes(grados)
            print(f"{grados} grados son {radianes} radianes.")
        elif opcion.lower() == 'r':
            radianes = float(input("Ingrese el ángulo en radianes: "))
            grados = radianes_a_grados(radianes)
            print(f"{radianes} radianes son {grados} grados.")
        elif opcion.lower() == 'q':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 'g', 'r' o 'q'.")


if __name__ == "__main__":
    main()
