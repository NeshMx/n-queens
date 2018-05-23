import sys
import os
import random
from itertools import permutations


def nqueens(s):
    n = s
    cols = range(n)
    count = 0
    solutions = []
    for vec in permutations(cols):
        if n == len(set(vec[i] + i for i in cols)) \
             == len(set(vec[i] - i for i in cols)):
            count += 1
            solutions.append(vec)    
    return solutions, count


def menu(vec, count):
    print('Se encontraron ' + str(count) + ' soluciones')
    print('¿Deseas obtener solo una o todas las soluciones?')
    print('1. Una\n2. Todas')
    option = int(input())
    fname = open('soluciones.txt', 'w')
    if option == 1:
        pos = random.randrange(count + 1)
        fname.write(str(vec[pos]))
    elif option == 2:
        fname.write('\n'.join(str(i) for i in vec))
    print('El archivo con las soluciones está listo en ' + os.path.realpath('soluciones.txt'))


def main():
    size = int(input('Introduce el número de reinas: '))
    x, y = nqueens(size)
    menu(x,y)
    sys.exit()


if __name__ == '__main__':
    main()
