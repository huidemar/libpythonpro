from libpythonpro.spam.modelos.usuario import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Foo', email='foo@bar.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Foo', email='foo@bar.com.br'), Usuario(nome='Ticio', email='foo@bar.com.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

