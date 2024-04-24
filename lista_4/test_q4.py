""" 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1] = 34 """
def maior_soma_seguimento(lista):
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)!=int:
            return Exception
    
    max_atual = max_total = lista[0]
    for num in lista[1:]:
        max_atual = max(num, max_atual + num)
        max_total = max(max_total, max_atual)
    return max_total


assert maior_soma_seguimento([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34 # testando valores válidos
assert maior_soma_seguimento([0, 0, 0, 0]) == 0 # testando valores válidos
assert maior_soma_seguimento([1, 1, 1, 1]) == 4 # testando valores válidos
assert maior_soma_seguimento([]) == Exception # testando valores inválidos <class 'Exception'>
assert maior_soma_seguimento([0.0, 0.1, 1, 2]) == Exception # testando valores inválidos <class 'Exception'>
assert maior_soma_seguimento(['10', '&', 9, -6, 4, 1]) == Exception # testando valores inválidos <class 'Exception'>
print("testes ok")
