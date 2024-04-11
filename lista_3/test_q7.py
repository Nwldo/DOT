"""
7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna
a categoria desse nadador de acordo com a tabela abaixo: 
"""
def categoria(idade):
    if type(idade) != int or idade not in range(5,120): # testa se o valor não int ou não está no intervalo
        return Exception
    if 5 <= idade <= 7:
        return f'Infantil A'
    elif 8 <= idade <= 10:
        return f'Infantil B'
    elif 11 <= idade <= 13:
        return f'Juvenil A'
    elif 14 <= idade <= 17:
        return f'Juvenil B'
    else:
        return f'Adulto'
    
assert categoria(5) == 'Infantil A' # testando valores válidos
assert categoria(6) == 'Infantil A' # testando valores válidos
assert categoria(10) == 'Infantil B' # testando valores válidos
assert categoria(11) == 'Juvenil A' # testando valores válidos
assert categoria(17) == 'Juvenil B' # testando valores válidos
assert categoria("20") == Exception # testando valores inválidos
assert categoria(2) == Exception # testando valores inválidos
print("testes ok")