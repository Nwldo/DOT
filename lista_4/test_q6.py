""" 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False """

def verificar_order(lista):
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)!=int:
            return Exception
    if lista == sorted(lista):
        return True
    else:
        return False


assert verificar_order([1, 2, 3]) == True # testando valores válidos
assert verificar_order([3, 7, 2]) == False # testando valores válidos
assert verificar_order([1, 1, 1]) == True # testando valores válidos
assert verificar_order([0, 0, 0]) == True # testando valores válidos
assert verificar_order([5, -2, -2, -7, 3, 15, 10, -3]) == False # testando valores válidos
assert verificar_order([]) == Exception # testando valores inválidos <class 'Exception'>
assert verificar_order(["1", 2, 9]) == Exception # testando valores inválidos <class 'Exception'>

