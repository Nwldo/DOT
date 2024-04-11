"""
1.Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R**3)
"""
import pytest

PI = 3.14
def calcular_volume(r):
    if not isinstance(r, float) or r <= 0:
        return Exception

    v = 4/3 * PI * r**3
    return f'{v:.2f}'

def test_calcular_volume_return_Exception():
    result = calcular_volume(0)

    assert result == Exception

def test_calcular_volume_not_int():
    assert calcular_volume("texto")