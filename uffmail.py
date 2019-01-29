
import jackio
import mail
import sys

matricula = input("Digite sua matricula: ")

reader = jackio.Leitor("dataset/alunos.csv")
listaAluno = reader.busca(matricula, 1)
#verifica status da matricula
if not listaAluno:
    #lista vazia / matrícula inválida
    print("Matrícula digitada é inexistente.")
    sys.exit('Valor inválido')

elif listaAluno[-1] == "Inativo":
    #exibir menssagem de impossibilidade de criacao do uffmail
    #encerrar programa
    pass
else:
    criadorEmail = mail.MotorMail(listaAluno[0],matricula)
    opsEmail = criadorEmail.solicitarEmail()

    print(listaAluno[0],', por favor escolha uma das opções abaixo para o seu UFFMail')
    contador = 1
    for ops in opsEmail:
        print(contador,' - ',ops)
        contador += 1

    opcao = int(input())

    #chamada do escritor

    print("A criação de seu e-mail ",opsEmail[opcao-1],
          " será feita nos próximos minutos. Um SMS foi enviado para",
          listaAluno[2]," com a sua senha de acesso.")
