#Para poder usar los marcadores de la coonfiguracion de pytest tengo que importar mark
from pytest import mark

@mark.ui
def test_prueba01():
    assert True
@mark.ui
def test_prueba02():
    assert False == False

def test_prueba03():
    assert True == True