import csv

class Leitor:

    def __init__(self, caminho):
        self.caminho = caminho

    def busca(self,atributo, posicao):
        with open(self.caminho,'r') as csvfile:
            busca = csv.reader(csvfile)
            for line in busca:
                if line[posicao] == atributo:
                    csvfile.close
                    return line
        return []


class Escritor:
    def __init__(self, caminho):
        pass

    def inserir(self,lista):
        pass
