while True:
    try:
        divisor = int(input("Ingrese el divisor: "))
        resultado = 10 / divisor
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por cero. Intente de nuevo")
    except ValueError:
        print("Debe ingresar un numero entero")

