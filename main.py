import sumar
import restar
import multiplicar
import dividir
import suma_avanzada

# Verificar que los módulos y funciones están importados correctamente
print("Sumar:", hasattr(sumar, 'sumar'))
print("Restar:", hasattr(restar, 'restar'))
print("Multiplicar:", hasattr(multiplicar, 'multiplicar'))
print("Dividir:", hasattr(dividir, 'dividir'))
print("Suma Avanzada:", hasattr(suma_avanzada, 'suma_avanzada'))

def menu():
    print("Seleccione una operación:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

while True:
    menu()
    choice = input("Ingrese una opción (1/2/3/4/5/6): ")

    if choice == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {sumar.sumar(a, b)}")

    elif choice == '2':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {restar.restar(a, b)}")

    elif choice == '3':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {multiplicar.multiplicar(a, b)}")

    elif choice == '4':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {dividir.dividir(a, b)}")

    elif choice == '5':
        nums = input("Ingrese los números separados por espacio: ")
        nums_list = list(map(float, nums.split()))
        print(f"Resultado: {suma_avanzada.suma_avanzada(*nums_list)}")

    elif choice == '6':
        print("Saliendo...")
        break

