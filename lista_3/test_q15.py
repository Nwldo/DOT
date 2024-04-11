""" A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
coletando dados sobre o salário e número de filhos. Faça uma função que leia
esses dados para um número não determinado de pessoas e retorne a média de
salário da população, a média do número de filhos, o maior salário e o percentual
de pessoas com salário até R$ 350,00. """

def calcular_estatisticas(pessoas):
    total_salario = 0
    total_filhos = 0
    maior_salario = 0
    pessoas_com_salario_ate_350 = 0

    for pessoa in pessoas:
        salario = pessoa['salario']
        filhos = pessoa['filhos']

        total_salario += salario
        total_filhos += filhos

        if salario > maior_salario:
            maior_salario = salario

        if salario <= 350:
            pessoas_com_salario_ate_350 += 1

    media_salario = total_salario / len(pessoas)
    media_filhos = total_filhos / len(pessoas)
    percentual_pessoas_com_salario_ate_350 = (pessoas_com_salario_ate_350 / len(pessoas)) * 100

    return {
        'media_salario': media_salario,
        'media_filhos': media_filhos,
        'maior_salario': maior_salario,
        'percentual_pessoas_com_salario_ate_350': percentual_pessoas_com_salario_ate_350
    }

pessoas = [
    {'salario': 500, 'filhos': 2},
    {'salario': 300, 'filhos': 1},
    {'salario': 800, 'filhos': 3},
    # adicione mais pessoas aqui
]

estatisticas = calcular_estatisticas(pessoas)

print('Média de salário:', estatisticas['media_salario'])
print('Média de número de filhos:', estatisticas['media_filhos'])
print('Maior salário:', estatisticas['maior_salario'])
print('Percentual de pessoas com salário até R$350:', estatisticas['percentual_pessoas_com_salario_ate_350'])

