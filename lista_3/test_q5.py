"""
5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.
"""
def tempo_em_dia(a,m,d):
    if type(a) != int or type(m) != int or type(d) != int:
        return Exception
    if (a not in range(0, 120)) or (m not in range(0,13)) or (d not in range(0,31)):
        return Exception
    return a * 365 + m * 30 + d

assert tempo_em_dia(10,1,2) == 3682 # testando valores válidos
assert tempo_em_dia(0,1,2) == 32 # testando valores válidos


