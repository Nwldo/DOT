""" 14. Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se
esses valores podem ser os comprimentos dos lados de um triângulo e, neste
caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um
triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento
de cada lado de um triângulo é menor do que a soma do comprimento dos outros
dois lados. O procedimento deve identificar o tipo de triângulo formado
observando as seguintes definições:
o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes """



def tipo_de_triangulo(x, y, z):
    if type(x)!= int or type(y)!= int or type(z)!= int:
        return Exception
    if x <= 0 or y <= 0 or z <= 0:
        return Exception
    if x < y + z or y < x + z or z < x + y:   # Verifique se os lados formam um triângulo
        if x == y == z: # Verifique se o triângulo é equilátero
            return "Triângulo Equilátero"
        elif x == y or y == z or z == x: # Verifique se o triângulo é isósceles
            return "Triângulo Isósceles"
        else: # Se o triângulo não for equilátero ou isósceles, é escaleno
            return "Triângulo Escaleno"
    else:
        return Exception


assert tipo_de_triangulo(1,1,1) == "Triângulo Equilátero"
assert tipo_de_triangulo(5,3,3) == "Triângulo Isósceles"
assert tipo_de_triangulo(3,1,2) == "Triângulo Escaleno"
assert tipo_de_triangulo(0,0,0) == Exception
assert tipo_de_triangulo("0","0","0") == Exception
