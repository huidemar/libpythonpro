from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
import pytest
from libpythonpro.spam.modelos.usuario import Usuario
from unittest.mock import Mock

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Foo', email='foo@bar.com.br'),
            Usuario(nome='Ticio', email='foo@bar.com.br')
        ],
        [
            Usuario(nome='Foo', email='foo@bar.com.br')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('foo@bar.com.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos'
                                   )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Foo', email='foo@bar.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('mevio@bar.com.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos'
                                   )
    enviador.enviar.assert_called_once_with == (
        'mevio@bar.com.br',
        'foo@bar.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

