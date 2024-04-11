""" 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3] """
import random

def eliminar_repeticoes(lista):
    lista_sem_repeticoes = []
    if len(lista)==0: # testar se a lista é vazia
        return Exception
    for elemento in lista:
        if type(elemento)!=int or elemento < 0:
            return Exception
        if elemento not in lista_sem_repeticoes:
            lista_sem_repeticoes.append(elemento)
    return lista_sem_repeticoes


lista = []

""" for item in range(6):
    lista.append(random.randint(0,6))

print(lista)
print(eliminar_repeticoes(lista)) """

assert eliminar_repeticoes([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3] # testando valores válidos
assert eliminar_repeticoes([5, 3, 1, 3, 4, 6]) == [5, 3, 1, 4, 6] # testando valores válidos
assert eliminar_repeticoes([-1]) == Exception # testando valores inválidos
assert eliminar_repeticoes(["%", 3]) == Exception # testando valores inválidos
print("testes ok")