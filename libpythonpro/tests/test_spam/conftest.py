import pytest

from libpythonpro.spam.db.conexao import Conexao


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