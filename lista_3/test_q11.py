"""
11. Faça uma função que recebe, por parâmetro, a altura e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura
- 44.7.
"""
def pesoIdeal(s,alt):
    if type(s)!=int or type(alt)!=float:
        return Exception
    if s == 1:
        ph = (62.1 * alt) - 44.7
        return ph
    elif s == 2:
        pm = (72.7 * alt) - 58
        return pm
    else:
        return Exception



assert pesoIdeal(1, 1.63) == 56.522999999999996 # testando valores válidos
assert pesoIdeal(2,1.72) == 67.044 # testando valores válidos
assert pesoIdeal(0,1.0) == Exception # testando classe inválida
assert pesoIdeal(7,1) == Exception # testando classe inválida
assert pesoIdeal("2", 1.9) == Exception # testando valores inválidos
print("testes ok")