# MutPy_ej
# Ubicacion en Linux
/mnt/d/Proyectos_VSC/TG/DemoTG-addSecurity

# Pruebas unitarias de los tests
python3 -m unittest -v test/test_security.py

# Prueba MutPy-Pynguin
mut.py --target one_conf.py --unit-test test/test_security.py -m -c

mut.py -t one_conf.py -u test/test_security.py -m -c

# ejecutar mutaciones y generar reporte en un text
mut.py -t one_conf.py -u test/test_security.py -m --report reports/report_01.txt

# ejecutar mutaciones html
mut.py -t one_conf.py -u test/test_security.py -m -c --report-html

# ejecutar mutaciones más agresivas y extensas
mut.py -t one_conf.py -u test/test_security.py -m -c -e

# Significado de los comandos
**mut.py:** Es el comando principal para ejecutar MutPy.

**--target folder/doc.py:** La opción *--target* se utiliza para especificar el archivo de código fuente que se someterá a pruebas de mutación. En este caso, el archivo es *folder/doc.py*.

**--unit-test folder1/folder2/doc.py:** La opción *--unit-test* se utiliza para especificar el archivo de pruebas unitarias que se utilizará para probar el código fuente. En este caso, el archivo de pruebas es *folder1/folder2/doc.py*.

**-m:** Esta opción activa el modo de mutación. En este modo, MutPy genera mutantes (versiones del código fuente con pequeñas modificaciones) y los prueba utilizando las pruebas unitarias proporcionadas.

**-c:** Esta opción activa el modo de cobertura. En este modo, MutPy calcula la cobertura de las pruebas, es decir, qué porcentaje del código fuente es cubierto por las pruebas unitarias.

**-e:** Esta opción activa el modo de exportación. En este modo, MutPy exporta los resultados de las pruebas de mutación a un archivo.

# explicación del resumen de las pruebas de mutacion
**Mutation score [7.29935 s]:** 100.0%: El “Mutation score” o “Puntuación de mutación” es una métrica que indica qué porcentaje de mutantes fueron “matados” por las pruebas. En este caso, el puntaje de mutación es del 100%, lo que significa que todas las mutaciones introducidas fueron detectadas por las pruebas. El tiempo entre corchetes (7.29935 s) es el tiempo que tardó en ejecutarse la prueba de mutación.

**all: 114:** Este es el número total de mutaciones que se introdujeron en el código.

**killed: 6 (5.3%):** Este es el número y porcentaje de mutaciones que fueron “matadas” por las pruebas. Una mutación “matada” significa que la prueba falló cuando se introdujo la mutación, lo cual es el comportamiento deseado.

**survived: 0 (0.0%):** Este es el número y porcentaje de mutaciones que “sobrevivieron” a las pruebas. Una mutación “sobreviviente” significa que la prueba pasó a pesar de la mutación, lo cual no es el comportamiento deseado.

**incompetent: 108 (94.7%):** Este es el número y porcentaje de mutaciones que se consideran “incompetentes”. Una mutación “incompetente” es una que no pudo ser ejecutada debido a errores de sintaxis o semánticos.

**timeout: 0 (0.0%):** Este es el número y porcentaje de mutaciones que causaron que las pruebas se quedaran en un bucle infinito o excedieran el tiempo límite establecido.


# Python Debugger (pdb)

This library allows you to Debug your code, just using the terminal.

| **Intrucción** | **Descripción**                                                                       |
|----------------|---------------------------------------------------------------------------------------| 
| list (l)       | Lista 5 lineas arriba y debajo de la linea actual que se está ejecutando.             |
| where (w)      | Nos indica la linea actual que se está ejecutando.                                    |
| next (n)       | Continua a la siguiente linea.                                                        |
| step (s)       | Ingresa a la función que se encuentra en la linea actual para hacer debug sobre ella. |
| continue (c)   | Sigue la ejecución normalmente hasta el siguiente breakpoint.                         |


# Notas:
Instalé un clone de mutpy; este es editable y se puede hacer pruebas mientras se hace cambios sobre la misma libreria
Se instaló con esas caracteristicas con el siguiente comando:

/mnt/d/Proyectos_VSC/TG/mutpy-pynguin-flask-mut$ pip3 install -e .
