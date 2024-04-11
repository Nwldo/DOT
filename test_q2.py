""" 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
o número de vezes que cada número ocorre na sequência. """

def ocorrencia_numeros(lista):
    qdt_numeros = {}
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for elemento in lista:
        if type(elemento)!=int or elemento < 0:
            return Exception
        if elemento in qdt_numeros:
            qdt_numeros[elemento] = qdt_numeros[elemento] + 1
        else:
            qdt_numeros[elemento] = 1
    return qdt_numeros


assert ocorrencia_numeros([5, 4, 5, 7, 3, 4]) == {5: 2, 4: 2, 7: 1, 3: 1} 
assert ocorrencia_numeros([2, 2, 2, 1, 1, 4]) == {2: 3, 1: 2, 4: 1} 
assert ocorrencia_numeros([]) == Exception
assert ocorrencia_numeros([-1,6]) == Exception
assert ocorrencia_numeros(["*", 2, 9]) == Exception # testando valores inválidos
print("testes ok")