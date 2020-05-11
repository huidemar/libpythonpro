from libpythonpro.spam.modelos.usuario import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Foo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Foo'), Usuario(nome='Ticio')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

