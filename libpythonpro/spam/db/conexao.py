from libpythonpro.spam.db.sessao import Sessao
from time import sleep

class Conexao:
    def __init__(self):
        sleep(1)

    def gerar_sessao(self):
        return Sessao()


    def fechar(self):
        pass
