import ast
import os
import sys
import time

# Ruta al archivo App.py que contiene la aplicación Flask
app_filename = "App.py"

# Cargar el contenido del archivo App.py
with open(app_filename, "r") as source:
    code = source.read()

# Analizar el árbol de sintaxis abstracta (AST)
program = ast.parse(code)

# Crear un archivo para guardar el AST
ast_output_filename = "ast_output_after_execution.txt"

# Crear un entorno de nombres para la ejecución del archivo con __name__ = "test"
namespace = {
    "__name__": "__test__",
    "__file__": os.path.abspath(app_filename),
}


# Ejecutar el código de App.py y capturar el contexto después de aplicar las configuraciones
try:
    exec(code, namespace)
    print("Ejecución completada en entorno de prueba ('test').")
except Exception as e:
    print(f"Error durante la ejecución del código: {e}")

# Obtener la instancia de Flask del entorno
app = namespace.get("app")

# Capturar las configuraciones cargadas en app.config después de la ejecución
if app:
    config_output_filename = "config_output_after_execution.txt"
    with open(config_output_filename, "w") as file:
        file.write(
            "Configuraciones encontradas en app.config después de la ejecución:\n"
        )
        for key, value in app.config.items():
            file.write(f"{key}: {value}\n")
            print(f"{key}: {value}")

    print(f"Configuraciones guardadas en {config_output_filename}")

    # Guardar el AST del programa después de la ejecución
    with open(ast_output_filename, "w") as file:
        file.write(ast.dump(program, indent=4))
    print(f"AST después de la ejecución guardado en {ast_output_filename}")
else:
    print("No se encontró la instancia de Flask 'app'.")
