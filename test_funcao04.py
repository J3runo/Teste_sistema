from funcao import *

def test_email_valido():
    assert email_valido("jose-brunotj@hotmail.com") is True
    assert email_valido("jose-bruno.com") is False

def test_dividir():
    assert dividir(2,2) ==1
    assert dividir(2,0) ==None

def test_maiuscula():
    assert maiuscula("Bruno") == True
    