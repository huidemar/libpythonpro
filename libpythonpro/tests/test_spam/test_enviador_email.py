import pytest

from libpythonpro.spam.email_invalido import EmailInvalido
from libpythonpro.spam.enviador_email import Enviador


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['huidemar@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
                                remetente,
                                'luciano@python.pro.br',
                                'Assunto - test Curso python PRo',
                                'Turma Luis Vital - teste e-mail'
                                )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
                        remetente,
                        'luciano@python.pro.br',
                        'Assunto - test Curso python PRo',
                        'Turma Luis Vital - teste e-mail'
                        )