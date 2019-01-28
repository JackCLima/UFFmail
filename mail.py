

class MotorMail:
    def __init__(self, matricula):
        self.nome = ""
        self.status = True
        self.matricula = matricula
        pass

    def criarEmail(self, listaAluno):
        
'''
    @property
    #getStatus
    def status(status):
        return self.status

    @status.setter
    def status(self,status):
        pass

    @property
    def nome(self):
        retunr self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome
'''
class GeradorMail:

    def __init__(self, nome):
        self.nome = nome
        self.mail = "@id.uff.br"

    def opcoes(self):
        pass
