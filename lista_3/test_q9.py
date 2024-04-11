"""
9. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
ímpar. A função deve retornar um valor booleano.
"""
def e_par(n):
    if type(n) != int or n < 0:
        return Exception
    if n % 2 ==0:
        return True
    else:
        return False
    
assert e_par(5) == False # testando valores válidos
assert e_par(0) == True # testando valores válidos
assert e_par(-3) == Exception # testando valores inválidos
assert e_par(0.1) == Exception # testando valores inválidos
assert e_par("%") == Exception # testando valores inválidos
assert e_par(" ") == Exception # testando valores inválidos
