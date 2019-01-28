

class MotorMail:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.status = True #ativo/Inativo
        self.matricula = matricula
        self.mail = ""
        pass

    def solicitarEmail(self, nome):
        if listaAluno == []:
            #lancar exception.isEmpty
            pass

        generator = GeradorMail(listaAluno[0])
        listOptions = generator.opcoes()
        return listOptions

    @property
    def mail(email):
        return self.mail

    @mail.setter
    def mail(self, email):
        if email == '':
            #lancar exception
            pass
        self.mail = email
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
        self.nome = nome.lower()
        self.mail = "@id.uff.br"

    def opcoes(self):
        # acrescentar viabilidade para dois nomes ou mais de 3 nomes
        # implementar uma funcao que trabalhe sobre o len da namelist
        namelist = self.nome.split()
        ops1 = namelist[0]+'_'+namelist[1]
        ops2 = namelist[0]+namelist[1][0]+namelist[2][0]
        ops3 = namelist[0]+namelist[2]
        ops4 = namelist[0][0]+namelist[2]
        ops5 = namelist[0][0]+namelist[1]+namelist[2]
        return [ops1,ops2,ops3,ops4,ops5]
