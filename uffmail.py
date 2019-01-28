
import jackio
import mail

matricula = input("Digite sua matricula: ")

reader = jackio.Leitor("dataset/alunos.csv")
listaAluno = reader.busca(matricula)
#verifica status da matricula
if (listaAluno[-1] == "Inativo"):
    #exibir menssagem de impossibilidade de criacao do uffmail
    #encerrar programa
    pass
else:
    criadorEmail = mail.MotorMail(listaAluno[0],matricula)
    opsEmail = criadorEmail.solicitarEmail()

    print(listaAluno[0],', por favor escolha uma das opções abaixo para o seu UFFMail')
    for i in range(1,1,len(opsEmail)+1):
        print(i,' - ',opsEmail[i])

    opcao = int(input())

    #chamada do escritor

    print("A criação de seu e-mail ",opsEmail[opcao],
          " será feita nos próximos minutos. Um SMS foi enviado para",
          listaAluno[2]," com a sua senha de acesso.")
