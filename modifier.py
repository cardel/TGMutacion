import ast
import re


class VariableReassigner(ast.NodeTransformer):
    def __init__(self, target_variable, new_value):
        self.target_variable = target_variable
        self.new_value = new_value
        self.original_value = None
        self.found_line = None

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and re.search(self.target_variable, target.id):
                # Capturar el valor original y la línea
                if self.original_value is None:
                    try:
                        self.original_value = eval(compile(ast.Expression(node.value), filename="<ast>", mode="eval"))
                    except Exception as e:
                        self.original_value = f'Error al evaluar: {e}'
                    self.found_line = node.lineno

                # Crear un nuevo nodo de valor
                new_value_node = ast.Constant(value=self.new_value)
                node.value = new_value_node
        return self.generic_visit(node)


def reassign_variable_in_file(file_path, target_variable, new_value):
    with open(file_path, 'r') as file:
        file_content = file.read()

    tree = ast.parse(file_content)
    reassigner = VariableReassigner(target_variable, new_value)
    modified_tree = reassigner.visit(tree)

    # Convertir el AST modificado de vuelta a código
    modified_code = ast.unparse(modified_tree)

    with open(file_path, 'w') as file:
        file.write(modified_code)

    return reassigner.original_value, new_value, reassigner.found_line


# Ejemplo de uso
file_path = 'configuration/configuration.py'  # 'ruta/al/archivo.py'
target_variable = 'pruebaX'  # 'variable_a_reasignar'
new_value = ['DESDE SEPTIEMBREEEEE!!!']  # 'DESDE SEPTIEMBREEEEE!!!'
original_value, new_value, found_line = reassign_variable_in_file(file_path, target_variable, new_value)
print(f'El valor original de la variable "{target_variable}" era: {original_value} type: {type(original_value)}')
print(f'El nuevo valor de la variable "{target_variable}" es: {new_value} type: {type(new_value)}')
print(f'La variable fue encontrada en la línea: {found_line}')
