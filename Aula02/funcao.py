

def IMC(peso, altura):

    imc_calculado = peso / (altura * altura)
    
    if (imc_calculado <= 17):
        return "Muito abaixo do peso ideal"
    elif(imc_calculado >=17 and imc_calculado <=18.49):
        return "Abaixo do peso"
    elif(imc_calculado >=18.5 and imc_calculado<=24.99):
        return "Peso normal"
    elif(imc_calculado >=25 and imc_calculado<=29.99):
        return "Acima do peso"
    elif(imc_calculado >=30 and imc_calculado<=34.99):
        return "Obesidade grau 1"    
    elif(imc_calculado >=35 and imc_calculado<=39.99):
        return "Obesidade grau 2"    
    else:
        return "Obesidade grau 3(Mórbida)"

print (IMC (20,1.75))