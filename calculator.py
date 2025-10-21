# calculator.py
def add(a, b):
    """Suma dos números."""
    return a + b

def subtract(a, b):
    """Resta dos números."""
    return a - b

def multiply(a, b):
    """Multiplica dos números."""
    return a * b

def divide(a, b):
    """Divide dos números. Lanza error si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def chained_operations(operations):
    """
    Realiza operaciones encadenadas.
    Ejemplo: operations = [('add', 5, 3), ('multiply', None, 2)] -> (5 + 3) * 2
    """
    if not operations:
        raise ValueError("No hay operaciones para realizar.")
    
    op, a, b = operations[0]
    if op == 'add':
        result = add(a, b)
    elif op == 'subtract':
        result = subtract(a, b)
    elif op == 'multiply':
        result = multiply(a, b)
    elif op == 'divide':
        result = divide(a, b)
    else:
        raise ValueError(f"Operación desconocida: {op}")
    
    for op, _, next_b in operations[1:]:
        if op == 'add':
            result = add(result, next_b)
        elif op == 'subtract':
            result = subtract(result, next_b)
        elif op == 'multiply':
            result = multiply(result, next_b)
        elif op == 'divide':
            result = divide(result, next_b)
        else:
            raise ValueError(f"Operación desconocida: {op}")
    
    return result