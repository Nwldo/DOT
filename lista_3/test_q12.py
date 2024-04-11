"""
12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente
"""
def ordenacao(x,y):
    if type(x)!=int or type(y)!=int or x < 0 or y < 0:
        return Exception
    if y < x:
        return y, x
    else:
        return x, y

#print(ordenacao(2,4))

assert ordenacao(1, 2) == (1, 2) # testando valores válidos
assert ordenacao(2, 1) == (1, 2) # testando valores válidos
assert ordenacao(0,1.0) == Exception # testando classe inválida
assert ordenacao("2", 10) == Exception # testando valores inválidos
assert ordenacao(-10, 3) == Exception # testando valores inválidos
print("testes ok")