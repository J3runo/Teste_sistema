def email_valido(email):
    return "@" in email and '.com' in email

def dividir(a,b):
    if b ==0:
        return None
    return a/b    

def maiuscula(email):
    if any(x.isupper() for x in email):
        return True
    return False