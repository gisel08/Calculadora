# main.py

def main():
    print("Calculadora Simple")
    print("Operaciones disponibles: suma (+), resta (-), multiplicación (*), división (/)")
    print("Escribe 'salir' para terminar.")

    while True:
        operation = input("Ingresa la operación (ej. +, -, *, /) o 'salir': ").strip()
        if operation.lower() == 'salir':
            print("¡Adiós!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Operación no válida. Usa +, -, *, o /.")
            continue
        
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue
        
        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            print(f"Resultado: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()