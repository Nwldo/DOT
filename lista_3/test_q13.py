""" 13. Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
O procedimento deve retornar, também por parâmetro, a duração do jogo em
horas e minutos, considerando que o tempo máximo de duração de um jogo é
de 24 horas e que o jogo pode começar em um dia e terminar no outro. """


def duracao_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    if type(hora_inicio)!=int or type(minuto_inicio)!=int or type(hora_fim)!=int or type(minuto_fim)!=int:
        return Exception
    if hora_inicio < 0 or minuto_inicio < 0 or hora_fim < 0 or minuto_fim < 0:
        return Exception
    # Convertendo tudo para minutos
    inicio = hora_inicio * 60 + minuto_inicio
    fim = hora_fim * 60 + minuto_fim

    # Caso o jogo comece em um dia e termine no outro
    if fim < inicio:
        fim += 24 * 60

    # Calculando a duração
    duracao = fim - inicio

        # Convertendo de volta para horas e minutos
    duracao_horas = duracao // 60
    duracao_minutos = duracao % 60

  
    return f'{duracao_horas} horas e {duracao_minutos} minutos'



assert duracao_jogo(23, 50, 0, 20) == '0 horas e 30 minutos' # testando classe válida
assert duracao_jogo(2, 0, 0, 200) == '1 horas e 20 minutos'
assert duracao_jogo(0, 0, 0, 1) == '0 horas e 1 minutos'
assert duracao_jogo(0, 0, 0, 0) == '0 horas e 0 minutos'
assert duracao_jogo(0, 0, 0, 0) == '0 horas e 0 minutos'
assert duracao_jogo(1, 1, 1, 1) == '0 horas e 0 minutos'
assert duracao_jogo(-1, 0, 0, 0) == Exception
assert duracao_jogo("0", 0, 0, 0) == Exception
assert duracao_jogo(-1, -1, -1, -1) == Exception
