from calculadora import sumar, multiplicar

def test_sumar_positivos():
    assert sumar(1,2)==3

def test_sumar_negativos():
    assert sumar(-1,-1)==-2

def test_multiplicar_positivos():
    assert sumar(10,0)==0

def test_multiplicar_negativos():
    assert sumar(4,5)==20


   