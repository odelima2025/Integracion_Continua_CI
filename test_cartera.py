# test_cartera.py
import pytest
from cartera import Cartera, SaldoInsuficiente
#
# Pruebas a ser ejecutadas sobre el archivo cartera.py
# test_crear_cartera_saldo_inicial_positivo: Prueba que al crear una Cartera con un saldo inicial positivo, el saldo se establece correctamente.
# test_crear_cartera_saldo_inicial_negativo: Prueba que al crear una Cartera con un saldo inicial negativo, el saldo se establece a 0.
# test_ingresar_dinero: Prueba que al ingresar dinero, el saldo se actualiza correctamente.
# test_gastar_dinero: Prueba que al gastar dinero, el saldo se reduce correctamente.
# test_gastar_dinero_saldo_insuficiente: Prueba que al intentar gastar más dinero del disponible, se lanza una excepción SaldoInsuficiente.
# test_gastar_todo_el_saldo: Prueba que al gastar todo el saldo, el saldo se reduce a 0.

def test_crear_cartera_saldo_inicial_positivo():
    cartera = Cartera(100)
    assert cartera.saldo == 100

def test_crear_cartera_saldo_inicial_negativo():
    cartera = Cartera(-100)
    assert cartera.saldo == 0

def test_ingresar_dinero():
    cartera = Cartera(100)
    cartera.ingresar(50)
    assert cartera.saldo == 150

def test_gastar_dinero():
    cartera = Cartera(100)
    cartera.gastar(50)
    assert cartera.saldo == 50

def test_gastar_dinero_saldo_insuficiente():
    cartera = Cartera(100)
    with pytest.raises(SaldoInsuficiente):
        cartera.gastar(150)

def test_gastar_todo_el_saldo():
    cartera = Cartera(100)
    cartera.gastar(100)
    assert cartera.saldo == 0

if __name__ == "__main__":
    pytest.main()
