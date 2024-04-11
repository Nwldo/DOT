"""
4. Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.
"""
def tempo(seg):
    if type(seg)!=int or seg <= 0:
        return Exception
    th = seg // 3600
    tm = (seg % 3600) // 60
    ts = (seg % 3600) % 60
    return th,tm,ts

assert tempo(0) == Exception # testando valores inválidos
assert tempo(-2) == Exception # testando valores inválidos
assert tempo("qualquer coisa") == Exception # testando valores inválidos
assert tempo(1) == (0,0,1) # testando valores válidos
assert tempo(3600) == (1,0,0) # testando valores válidos

print("todos os teste ok")