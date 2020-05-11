from libpythonpro.spam.email_invalido import EmailInvalido


class Enviador(object):
    def __init__(self):
        self.qtde_email_enviados = 0
    def enviar(self, remetente, destinataro, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'E-mail de remetente inválido: {remetente}')
        self.qtde_email_enviados += 1
        return remetente