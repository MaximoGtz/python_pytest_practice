from pytest import mark


@mark.api
@mark.parametrize("email", ["maximo@correo.com", "maximo2@correo.com", "maximo3@correo.com"])
@mark.parametrize("password", ["maximo123", "maximo2123", "maximo3123"])
def test_login(email, password):
    assert email == "maximo@correo.com"
    assert password == "maximo123"


@mark.api
@mark.parametrize("email, password", [("maximo@correo.com", "maximo123"), ("maximo2@correo.com", "maximo2123"), ("maximo3@correo.com","maximo3123")])
def test_login2(email, password):
    assert email in ["maximo@correo.com", "maximo2@correo.com"]
    assert password in ["maximo123", "maximo2123"]