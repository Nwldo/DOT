"""
6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano.
"""
def valor_perfect(n):
    div = 0
    if type(n) != int or n <= 0:
        return Exception
    for i in range(1,n):
        if n % i == 0:
            div += i
 
    if div == n:
        return True
    else:
        return False

assert valor_perfect(6) == True # testando valores válidos
assert valor_perfect(4) == False # testando valores válidos
assert valor_perfect("texto") == Exception # testando valores inválidos
assert valor_perfect(7.2) == Exception # testando valores inválidos