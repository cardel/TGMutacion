import pdb


def bubblesort(elms):
    for n in range(len(elms) - 1, 0, -1):
        for i in range(n):
            if elms[i] > elms[i + 1]:  # error a proposito para el debug
                elms[i], elms[i + 1] = elms[i + 1], elms[i]


elements = [39, 12, 18, 85, 72, 10, 2, 18]

print(f'Lista sin ordenar: {elements}')
#pdb.set_trace()  # breakpoint. Es permitido tener muchos (indefinidos).
bubblesort(elements)
print(f'Lista ordenada: {elements}')
