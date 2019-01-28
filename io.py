import csv

class Leitor:

    def __init__(self):
        pass

    def busca(self,matricula):
        with open("dataset/aluno.csv","r") as csvfile:
            busca = csv.reader(file)
            for line in busca:
                if line[1] == matricula:
                    file.close
                    return line
        return []


class Escritor:
    def __init__(self):
        pass

    def inserir(self,lista):
        pass
    
