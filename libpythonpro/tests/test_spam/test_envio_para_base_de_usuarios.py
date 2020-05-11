from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
import pytest
from libpythonpro.spam.modelos.usuario import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtde_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('foo@bar.com.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos'
                                   )
    assert len(usuarios) == enviador.qtde_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Foo', email='foo@bar.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('mevio@bar.com.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos'
                                   )
    assert enviador.parametros_de_envio == (
        'mevio@bar.com.br',
        'foo@bar.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

