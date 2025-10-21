# Documentación de Pruebas para la Calculadora

## 1. Prueba Unitaria
- **Descripción**: Verifica que la función de suma (`add`) funcione correctamente con diferentes valores.
- **Ejemplos probados**:
  - add(2, 3) → Esperado: 5
  - add(-1, 1) → Esperado: 0
  - add(0, 0) → Esperado: 0
- **Herramienta**: unittest en Python.
- **Resultado esperado**: Todas las pruebas pasan sin errores.
- **Código**: Ver `test_calculator.py` en la sección `test_add`.

## 2. Caso de Prueba de Integración
- **Descripción**: Prueba operaciones encadenadas usando múltiples funciones básicas (add, multiply, subtract).
- **Ejemplo probado**:
  - Operaciones: [('add', 5, 3), ('multiply', None, 2), ('subtract', None, 1)]
  - Resultado esperado: 15 ((5+3)*2 -1)
- **Herramienta**: unittest en Python.
- **Resultado esperado**: La secuencia se ejecuta sin errores y devuelve el valor correcto.
- **Código**: Ver `test_calculator.py` en la sección `test_chained_operations`.

## 3. Prueba de Rendimiento
- **Descripción**: Mide el tiempo para repetir una suma simple (1+1) 10,000 veces. Simula un escenario de alto volumen para verificar eficiencia.
- **Herramienta**: timeit en Python.
- **Umbral**: Si el tiempo >1 segundo, considerar optimizaciones (por ejemplo, usar operaciones nativas en lugar de funciones).
- **Resultado esperado**: Tiempo muy bajo (<0.01s en la mayoría de las máquinas), indicando buen rendimiento.
- **Posibles mejoras**: Si se escala a millones de repeticiones, monitorear uso de CPU/memoria con herramientas como `psutil`.
- **Código**: Ver `performance_test.py`.

## Ejecución General
- Ejecuta pruebas unitarias e integración: `python test_calculator.py`
- Ejecuta prueba de rendimiento: `python performance_test.py`
- Notas: Todas las pruebas asumen que no hay errores en la implementación básica. En un entorno real, integra con CI/CD como GitHub Actions.