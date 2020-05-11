from libpythonpro.spam.email_invalido import EmailInvalido


class Enviador(object):
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'E-mail de remetente inválido: {remetente}')
        return remetente