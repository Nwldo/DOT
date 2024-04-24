""" 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
[1,3,6] """

def soma_cumulativa(lista):
    soma = 0
    resultado = []
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)!=int:
            return Exception
        soma += num
        resultado.append(soma)
    return resultado



assert soma_cumulativa([1, 2, 3]) == [1, 3, 6] # Testando valoes válidos
assert soma_cumulativa([0, 0, 0]) == [0, 0, 0] # Testando valoes válidos
assert soma_cumulativa([1, 1, 1]) == [1, 2, 3] # Testando valoes válidos
assert soma_cumulativa([-1, -1, 1]) == [-1, -2, -1] # Testando valoes válidos
assert soma_cumulativa([]) == Exception # Testando classe inválida
assert soma_cumulativa([1.0, 2, 3.2]) == Exception # Testando classe inválida
assert soma_cumulativa(['1', 2, '3']) == Exception # Testando classe inválida
print("testes ok")