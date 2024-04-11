"""
7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo: 
"""
def media_final(nota):
    if type(nota) != float or nota < 0 or nota > 10: # testa se o valor não int ou não está no intervalo
        return Exception
    if 0.0 <= nota <= 4.9:
        return f'D'
    elif 5.0 <= nota <= 6.9:
        return f'C'
    elif 7.0 <= nota <= 8.9:
        return f'B'
    elif 9.9 <= nota <= 10.0:
        return f'A'
   
    
assert media_final(0.0) == 'D' # testando valores válidos
assert media_final(6.2) == 'C' # testando valores válidos
assert media_final(10.0) == 'A' # testando valores válidos
assert media_final(7.1) == 'B' # testando valores válidos
assert media_final(10.1) == Exception # testando valores inválidos
assert media_final("20") == Exception # testando valores inválidos
assert media_final(-2) == Exception # testando valores inválidos
assert media_final(11.3) == Exception # testando valores inválidos
print("testes ok")