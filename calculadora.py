import math

def calculadora():
    print("Calculadora Científica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Seno")
    print("6. Coseno")
    print("7. Tangente")
    print("8. Logaritmo")
    print("9. Exponencial")

    opcion = int(input("Elige una opción: "))
    if opcion in range(1, 5):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    else:
        num = float(input("Ingresa un número: "))

    if opcion == 1:
        print(num1 + num2)
    elif opcion == 2:
        print(num1 - num2)
    elif opcion == 3:
        print(num1 * num2)
    elif opcion == 4:
        print(num1 / num2)
    elif opcion == 5:
        print(math.sin(num))
    elif opcion == 6:
        print(math.cos(num))
    elif opcion == 7:
        print(math.tan(num))
    elif opcion == 8:
        print(math.log(num))
    elif opcion == 9:
        print(math.exp(num))
    else:
        print("Opción inválida")

calculadora()