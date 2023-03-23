import jogodaforca
import adivinhacao

def escolhe_jogo():

    print("*******************************************")
    print("****** Bem vindo escolha seu jogo ********!")
    print("*******************************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print('Carregando jogo da forca!')
        jogodaforca.jogar()
    elif (jogo == 2):
        print('Carregando jogo Adivinhação!')
        adivinhacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()