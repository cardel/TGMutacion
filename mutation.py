import ast
import os
import sys

# Ruta al archivo App.py que contiene la aplicación Flask
app_filename = "App.py"

# Cargar el contenido del archivo App.py
with open(app_filename, "r") as source:
    code = source.read()

# Analizar el árbol de sintaxis abstracta (AST)
program = ast.parse(code)


# Definir un visitante para modificar la configuración ORIGINS
class MutationVisitor(ast.NodeTransformer):
    def visit_If(self, node):
        # Busca el bloque __main__ para insertar la mutación
        if (
            isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "__name__"
        ):
            # Verificar que se está comparando con '__main__'
            if isinstance(node.test.ops[0], ast.Eq) and isinstance(
                node.test.comparators[0], ast.Constant
            ):
                # Comprobar que el valor del comparador es "__main__"
                if node.test.comparators[0].value == "__main__":
                    # Crear la mutación para app.config["ORIGINS"] = ["*"]
                    mutation_assignment = ast.parse(
                        'app.config["ORIGINS"] = ["*"]\n'
                    ).body[0]
                    # Insertar la mutación justo antes de imprimir las configuraciones
                    node.body.insert(0, mutation_assignment)
        return node


# Aplicar la mutación al árbol de sintaxis
mutant_program = MutationVisitor().visit(program)

# Convertir el AST modificado de nuevo a código
mutant_code = ast.unparse(mutant_program)

# Guardar el código mutado en un archivo
mutated_filename = "mutated_app.py"
with open(mutated_filename, "w") as file:
    file.write(mutant_code)

print(f"Archivo mutado guardado en {mutated_filename}.")

# Ejecutar programa mutado
context = {"__file__": os.path.abspath(mutated_filename), "__name__": "__main__"}

exec(compile(mutant_code, mutated_filename, "exec"), context)
