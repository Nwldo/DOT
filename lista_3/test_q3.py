"""
3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e
retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso
contrário.
"""
def e_inteiro(n):
    div = 0
    if type(n) != int or n <= 0:
        return Exception
    for i in range(2,n):
        if n % i == 0:
            div += 1
    if div == 0:
        return True
    else:
        return False

assert e_inteiro(7) == True # testando valor válido
assert e_inteiro(2) == True # testando valor válido
assert e_inteiro(3) == True # testando valor válido
assert e_inteiro(13) == True # testando valor válido
assert e_inteiro(6) == False # testando valor válido
assert e_inteiro('3') == Exception # testando valor inválido
assert e_inteiro(8.22) == Exception # testando valor inválido
print("todos os teste ok")