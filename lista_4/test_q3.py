""" 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25 """

def maior_soma_segmento(lista):
    max_soma = 0
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for i in range(len(lista) - 1):
        if type(lista[i])!=int:
            return Exception
        soma = lista[i] + lista[i + 1]
        if soma > max_soma:
            max_soma = soma
    return max_soma



assert maior_soma_segmento([5, 2, 2, 7, 3, 15, 10, 3, 9, 6, 4, 1]) == 25 # testando valores válidos
assert maior_soma_segmento([5, 2, 2, 7, 3, 1, -6, 3, -9, 6, 4, 1]) == 10 # testando valores válidos
assert maior_soma_segmento([0, 0, 0, 0, 0, 0, 0, 0]) == 0 # testando valores válidos 
assert maior_soma_segmento([]) == Exception # testando valores inválidos
assert maior_soma_segmento(["*", 2, 9]) == Exception # testando valores inválidos 
print("testes ok")
