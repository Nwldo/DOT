""" 8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5 """
def valor_mais_proximo(lista):
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for num in lista:
        if type(num)==str:
            return Exception
        

    media = sum(lista) / len(lista)

    mais_proximo = 0
    menor_diferenca = float('inf') # cria um número infinito
  
    for valor in lista:
        # Calcula a diferença entre o valor atual e a média
        diferenca = abs(valor - media) 
        # Verifica se a diferença é menor que a menor diferença atual (número infinito)
        if diferenca < menor_diferenca:
            # Atualiza o valor mais próximo e a menor diferença
            mais_proximo = valor
            menor_diferenca = diferenca
    
    return mais_proximo



assert valor_mais_proximo([2.5, 7.5, 10.0, 4.0]) == 7.5 # testando valores válidos 
assert valor_mais_proximo([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 3 # testando valores válidos 
assert valor_mais_proximo([]) == Exception # testando valores inválidos <class 'Exception'> 
assert valor_mais_proximo(['@', 2.5, 7.5]) == Exception # testando valores inválidos <class 'Exception'>
print("testes ok")
