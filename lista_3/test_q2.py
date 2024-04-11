"""
2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada.
"""
def calcular_media_notas(nota1, nota2, nota3, letra):
    if type(nota1) != int or type(nota2) != int or type(nota3) != int or not isinstance(letra, str):
        return Exception
    elif letra == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif letra == 'P':
        return (5 * nota1 + 3 * nota2 + 2 * nota3) / 3



assert calcular_media_notas(7,8,9, 'A') == 8 # testando valor válido

# Teste com média ponderada (letra 'P')
assert calcular_media_notas(7, 8, 9, 'P') == 25.666666666666668
assert calcular_media_notas('7',5,2, 'A') == Exception
assert calcular_media_notas('7','5',2, 'A') == Exception
assert calcular_media_notas(3,5,'2', 'A') == Exception

