"""
8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano
"""
def positivo_negativo(v):
    if type(v) != int or v == 0:
        return Exception
    if v > 0:
        return True
    else:
        return False
    
assert positivo_negativo(5) == True # testando valores válidos
assert positivo_negativo(-1) == False # testando valores válidos
assert positivo_negativo(0) == Exception # testando valores inválidos
assert positivo_negativo(0.1) == Exception # testando valores inválidos
assert positivo_negativo("#") == Exception # testando valores inválidos