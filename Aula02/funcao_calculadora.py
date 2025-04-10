
def Calculadora(valor1, valor2, sinal):

    
    if (sinal == "+" ):
        return valor1 + valor2
    elif(sinal == "-"):
        return valor1 - valor2
    elif(sinal == "*"):
        return valor1 * valor2
    elif(sinal == "/"):
        if(valor1 > 0 and valor2 > 0 ):
            return valor1 / valor2
   
print(Calculadora(45,45,"+"))