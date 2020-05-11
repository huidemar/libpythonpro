from libpythonpro.spam.db.conexao import Conexao
from libpythonpro.spam.modelos.usuario import Usuario
import pytest

@pytest.fixture(scope='session')
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    #setup
    sessao_obj =conexao.gerar_sessao()
    yield sessao_obj
    #Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Foo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Foo'), Usuario(nome='Ticio')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

