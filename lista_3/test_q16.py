""" 16. Faça uma função que leia um número não determinado de valores positivos
e retorna a média aritmética dos mesmos. """


def media_aritmetica(valores):
    if not all(v > 0 for v in valores):
        return Exception
    return sum(valores) / len(valores)

#valores = [1, 2, 3, 4, 5]


assert media_aritmetica(1, 2, 3, 4, 5) == 3.0
assert media_aritmetica(1, 1, 1, 1, 1) == 1.0
assert media_aritmetica(0, 0, 0, 0, 0) == Exception 
assert media_aritmetica("2", 20, 8, 3, 1) == Exception 
assert media_aritmetica("0"," 0", "0", "0", "0") == Exception 
