#!/usr/bin/env python3

import jackio
import mail
import sys


#metodo de interface com o usuário, para selecao de opcao de email

def printOps(nome, listaOps):
    print(nome,', por favor escolha uma das opções abaixo para o seu UFFMail')
    contador = 1
    for ops in listaOps:
        print(contador,' - ',ops)
        contador += 1

#inicio do codigo principal

matricula = input("Digite sua matricula: ")

#busca as informacoes do Aluno
reader = jackio.Leitor("dataset/alunos.csv")
listaAluno = reader.busca(matricula, 1)

#verifica status da matricula
if not listaAluno:
    #lista vazia / matrícula inválida
    print("Matrícula digitada é inexistente.")
    sys.exit('ERRO - Valor inválido')

#verifica status da matricula do aluno
elif listaAluno[-1] == "Inativo":
    #exibir menssagem de impossibilidade de criacao do uffmail
    #encerrar programa
    print('Somente alunos ativos podem solicitar uffmail')
    sys.exit('ERRO - Aluno inativo')
else:

    criadorEmail = mail.MotorMail(listaAluno[0],matricula)
    opsEmail = criadorEmail.solicitarEmail()

    printOps(listaAluno[0], opsEmail)

    opcao = int(input())

    while opcao <= 0 or opcao >= 6:
        print (opcao,' não é um numero válido ')
        printOps(listaAluno[0], opsEmail)
        opcao = int(input())

    #chamada do escritor

    print("A criação de seu e-mail ",opsEmail[opcao-1],
          " será feita nos próximos minutos. Um SMS foi enviado para",
          listaAluno[2]," com a sua senha de acesso.")
