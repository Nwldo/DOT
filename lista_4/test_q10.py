""" Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
10, 3, 1] = 20 """

def maior_soma_repetidos(lista):
    soma = 0
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)!=int:
            return Exception
    for i in set(lista): # set(lista), é uma coleção de elementos únicos).
        if lista.count(i) > 1: # verifica se o elemento atual i aparece mais de uma vez na lista.
            soma_atual = i * lista.count(i)
            if soma_atual > soma:
                soma = soma_atual
    return soma

""" soma_atual = i * lista.count(i)
Se o elemento i aparece mais de uma vez na lista, calcula a soma dos valores 
repetidos multiplicando o elemento i pelo número de vezes que aparece na lista. 
Esta soma é armazenada na variável soma_atual """




assert maior_soma_repetidos([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20 # testando valores válidos
assert maior_soma_repetidos([1, 1, 1, 1]) == 4 # testando valores válidos
assert maior_soma_repetidos([0, 0, 0, 0]) == 0 # testando valores válidos
assert maior_soma_repetidos([]) == Exception # testando valores inválidos <class 'Exception'>
assert maior_soma_repetidos([5, -2, -2, 5, '3', 5, 10]) == Exception # testando valores inválidos <class 'Exception'>
assert maior_soma_repetidos([-2.1, 5.0, 10.0]) == Exception # testando valores inválidos <class 'Exception'>
print("testes ok")