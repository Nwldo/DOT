""" 9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
[7, 3] """
def eliminar_ocorrencias_numeros(lista):
    nova_lista = []
    
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)!=int:
            return Exception
    for num in lista:
        if lista.count(num) == 1:
            nova_lista.append(num)
    return nova_lista




assert eliminar_ocorrencias_numeros([5, 4, 5, 7, 3, 4]) == [7,3] # testando valores válidos
assert eliminar_ocorrencias_numeros([5, 4, 7, 3]) == [5, 4, 7, 3] # testando valores válidos
assert eliminar_ocorrencias_numeros([-1, -2, 3, 5, -1, -2]) == [3, 5] # testando valores válidos
assert eliminar_ocorrencias_numeros([]) == Exception # testando valores inválidos <class 'Exception'>
assert eliminar_ocorrencias_numeros([-1, -2, 3.5, 5, -1.1, -2]) == Exception # testando valores inválidos <class 'Exception'>