import ast
import re


class WordFinder(ast.NodeVisitor):
    def __init__(self, target_word):
        self.target_word = target_word
        self.found_lines = []
        self.variable_values = {}

    def visit_Str(self, node):
        if re.search(self.target_word, node.s):
            self.found_lines.append(node.lineno)
        self.generic_visit(node)

    def visit_Name(self, node):
        if re.search(self.target_word, node.id):
            self.found_lines.append(node.lineno)
            # Intentar obtener el valor de la variable
            try:
                value = eval(node.id, globals(), locals())
                self.variable_values[node.id] = value
            except NameError:
                self.variable_values[node.id] = 'Valor no disponible'
        self.generic_visit(node)


def find_word_in_file(file_path, target_word):
    with open(file_path, 'r') as file:
        file_content = file.read()

    tree = ast.parse(file_content)
    finder = WordFinder(target_word)
    finder.visit(tree)

    return finder.found_lines, finder.variable_values


# Ejemplo de uso
file_path = 'configuration/configuration.py'
target_word = 'SUPPORTS_CREDENTIALS'
lines, variable_values = find_word_in_file(file_path, target_word)
if lines:
    print(f'La palabra "{target_word}" fue encontrada en las siguientes líneas: {lines}')
    print(f'Valores de las variables encontradas: {variable_values}')
else:
    print(f'La palabra "{target_word}" no fue encontrada en el archivo.')
