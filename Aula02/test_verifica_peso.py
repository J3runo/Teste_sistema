import pytest
from funcao_verifica_peso_altura import calcular_imc

@pytest.mark.parametrize("peso,altura,esperado", [
    (400, 1.75, "Obesidade grau 3 (mórbida)"),
    (70, 1.75, "Peso normal")]) 


def test_imc(peso, altura, esperado):
    assert calcular_imc(peso, altura) == esperado
        
        