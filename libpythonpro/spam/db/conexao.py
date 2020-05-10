from libpythonpro.spam.db.sessao import Sessao


class Conexao:
    def gerar_sessao(self):
        return Sessao()


    def fechar(self):
        pass
