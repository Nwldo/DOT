""" 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
-6, 4, 1] = 34 """
def maior_soma_seguimento(lista):
    max_atual = max_total = lista[0]
    for i in lista:
        if type(i)!=int or len(lista)== 0:
            return Exception
    for num in lista[1:]:
        max_atual = max(num, max_atual + num)
        max_total = max(max_total, max_atual)
    return max_total

# Testando a função
print(maior_soma_seguimento([]))  # Deve retornar 34
#assert maior_soma_seguimento([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34 # testando valores válidos

