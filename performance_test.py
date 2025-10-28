# performance_test.py
import timeit

def performance_add_repeated():
    """Prueba de rendimiento: suma repetida 10,000 veces."""
    setup = "from calculator import add"
    stmt = "add(1, 1)"
    time_taken = timeit.timeit(stmt, setup=setup, number=10000)
    print(f"Tiempo para 10,000 sumas: {time_taken} segundos")
    if time_taken > 1:  
        print("Rendimiento bajo: optimizar si es necesario.")
    else:
        print("Rendimiento aceptable.")

if __name__ == '__main__':
    performance_add_repeated()