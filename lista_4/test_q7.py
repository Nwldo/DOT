""" 7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False """
def encontrar_elemento_repetido(lista):
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)!=int:
            return Exception
    if len(lista) != len(set(lista)): #O método set() é usado para criar um conjunto, que é uma coleção não ordenada de elementos únicos
        return True
    else:
        return False
    
""" print(encontrar_elemento_repetido([2.1, 3, 2.1, 4, 4])) """

assert encontrar_elemento_repetido([3, 7, 2, 4]) == False # testando valores válidos
assert encontrar_elemento_repetido([1, 2, 3, 1]) == True # testando valores válidos
assert encontrar_elemento_repetido([0, 0, 0, 0, 0]) == True # testando valores válidos
assert encontrar_elemento_repetido([-3, -2, 3, 1, 2]) == False # testando valores válidos
assert encontrar_elemento_repetido([]) == Exception # testando valores inválidos <class 'Exception'>
assert encontrar_elemento_repetido([2.1, 3, 2.1, 4, 4]) == Exception # testando valores inválidos <class 'Exception'>