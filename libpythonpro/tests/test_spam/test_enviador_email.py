from libpythonpro.spam.enviador_email import Enviador

def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('huidemar@gmail.com',
                    'luciano@python.pro.br',
                    'Assunto - test Curso python PRo',
                    'Turma Luis Vital - teste e-mail')
    assert 'huidemar@gmail.com' in resultado