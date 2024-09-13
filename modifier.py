import ast
import re


class WordFinder(ast.NodeVisitor):
    def __init__(self, target_word):
        self.target_word = target_word
        self.found_lines = []
        self.variable_values = {}
        self.strings = []
        self.functions = []

    def visit_Str(self, node):
        if re.search(self.target_word, node.s):
            self.found_lines.append(node.lineno)
            self.strings.append(node.s)
        self.generic_visit(node)

    def visit_Name(self, node):
        if re.search(self.target_word, node.id):
            self.found_lines.append(node.lineno)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and re.search(self.target_word, target.id):
                self.found_lines.append(node.lineno)
                try:
                    value = eval(compile(ast.Expression(node.value), filename="<ast>", mode="eval"))
                    self.variable_values[target.id] = value
                except Exception as e:
                    self.variable_values[target.id] = f'Error al evaluar: {e}'
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if re.search(self.target_word, node.name):
            self.found_lines.append(node.lineno)
            self.functions.append(node.name)
        self.generic_visit(node)


def find_word_in_file(file_path, target_word):
    with open(file_path, 'r') as file:
        file_content = file.read()

    tree = ast.parse(file_content)
    finder = WordFinder(target_word)
    finder.visit(tree)

    return finder.found_lines, finder.variable_values, finder.strings, finder.functions


# Ejemplo de uso
file_path = 'configuration/configuration.py'
target_word = 'DEBUG'
lines, variable_values, strings, functions = find_word_in_file(file_path, target_word)
if lines:
    print(f'La palabra "{target_word}" fue encontrada en las siguientes líneas: {lines}')
    if variable_values:
        print(f'Variables encontradas y sus valores: {variable_values}')
    if strings:
        print(f'Cadenas de texto encontradas: {strings}')
    if functions:
        print(f'Funciones encontradas: {functions}')
else:
    print(f'La palabra "{target_word}" no fue encontrada en el archivo.')
