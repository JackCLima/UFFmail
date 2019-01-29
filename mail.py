

class MotorMail:
    def __init__(self, nome, matricula):
        self.nome = nome
        #self.status = True #ativo/Inativo
        self.matricula = matricula
        #self.mail = ""


    def solicitarEmail(self):

        generator = GeradorMail(self.nome)
        listOptions = generator.opcoes()
        return listOptions


    def criarEmail(self, caminho, email, matricula):
        pass



'''
    @property
    def mail(email):
        return self.mail

    @mail.setter
    def mail(self, email):
        if email == '':
            #lancar exception
            pass
        self.mail = email

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
        ops1 = namelist[0]+'_'+namelist[1]+self.mail
        ops2 = namelist[0]+namelist[1][0]+namelist[2][0]+self.mail
        ops3 = namelist[0]+namelist[2]+self.mail
        ops4 = namelist[0][0]+namelist[2]+self.mail
        ops5 = namelist[0][0]+namelist[1]+namelist[2]+self.mail
        return [ops1,ops2,ops3,ops4,ops5]
