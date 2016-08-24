# -*- coding: utf-8 -*-
"""
    Este programa vem implementar o algoritmo da bissecção para uma dada função
    F(x).
"""

import sys

start = -2.5
end = 0
erro = 0.0000000001

def math_function(x):
    return x**2 + 5*x + 6


def main():
    global start
    global end
    global erro

    if(math_function(start) * math_function(end) > 0):
        raise ValueError('Não existe raiz no intervalo dado')
    else:
        current_error = (end - start)/2

        while(current_error > erro):
            middle = (start + end)/2
            f_start = math_function(start)
            f_end = math_function(end)
            f_middle = math_function(middle)

            if(f_middle*f_start <= 0):
                end = middle
            else:
                start = middle

            current_error = (end - start)/2
            if(current_error < erro):
                print("A raiz se encontra em " + str((start + end)/2))


if __name__ == "__main__":
    main()
