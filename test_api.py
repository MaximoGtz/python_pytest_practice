from pytest import mark

#El primer test separa los parámetros email y password usando dos decoradores @mark.parametrize. Esto provoca un producto cartesiano, generando todas las combinaciones posibles entre los emails y las contraseñas. Por ejemplo, "maximo@correo.com" se probará con "maximo123", "maximo2123" y "maximo3123". Esto puede causar que algunos tests fallen o pasen inesperadamente, porque no necesariamente se están probando los pares correctos.
@mark.api
@mark.parametrize("email", ["maximo@correo.com", "maximo2@correo.com", "maximo3@correo.com"])
@mark.parametrize("password", ["maximo123", "maximo2123", "maximo3123"])
def test_login(email, password):
    assert email == "maximo@correo.com"
    assert password == "maximo123"

#El segundo test combina email y password en una lista de tuplas, asegurando que cada email se pruebe solo con su contraseña correspondiente. Esto evita combinaciones incorrectas y refleja mejor escenarios reales de login. Además, las aserciones usan in para permitir cierta flexibilidad, aunque en este caso algunas combinaciones de la lista de emails y passwords podrían pasar incluso si no son exactamente correctas.
@mark.api
@mark.parametrize("email, password", [("maximo@correo.com", "maximo123"), ("maximo2@correo.com", "maximo2123"), ("maximo3@correo.com","maximo3123")])
def test_login2(email, password):
    assert email in ["maximo@correo.com", "maximo2@correo.com"]
    assert password in ["maximo123", "maximo2123"]