import csv

class Leitor:

    def __init__(self, caminho):
        self.caminho = caminho

    def busca(self,atributo, posicaoAtributo):
        with open(self.caminho,'r') as csvfile:
            busca = csv.reader(csvfile)
            for line in busca:
                if line[posicaoAtributo] == atributo:
                    csvfile.close
                    return line
        return []


class Escritor:
    def __init__(self, caminho):
        self.caminho = caminho

'''
    def inserir(self,lista,atributo,posicaoAtributo):
        #with open(self.camiho,)

'''
