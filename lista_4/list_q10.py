def maior_soma_repetidos(lista):
    soma = 0
    for i in set(lista):
        if lista.count(i) > 1:
            soma_atual = i * lista.count(i)
            if soma_atual > soma:
                soma = soma_atual
    return soma

# Testando a função com o exemplo dado
print(maior_soma_repetidos([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]))  # Deve retornar 20
