
def calcular_imc(peso, altura):
    if altura <= 0:
        return "Altura inválida"
    
    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    
    if imc < 17:
        classificacao = "Muito abaixo do peso"
    elif 17 <= imc <= 18.49:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.99:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.99:
        classificacao = "Sobrepeso"
    elif 30 <= imc <= 34.99:
        classificacao = "Obesidade grau 1"
    elif 35 <= imc <= 39.99:
        classificacao = "Obesidade grau 2 (severa)"
    else:
        classificacao = "Obesidade grau 3 (mórbida)"
    
    return classificacao

# Exemplo de uso
peso = 70
altura = 1.75
resultado = calcular_imc(peso, altura)
print(resultado)

