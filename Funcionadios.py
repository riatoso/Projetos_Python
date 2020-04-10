# -*- coding:UTF-8 -*-
import time
from os import mkdir
def listar():
    lista = open("C:\\db\\lista.txt","r")
    arquivo = lista.readlines()
    print(20*"-+")
    print("FUNCIONARIOS CADASTRADOS".center(40))
    print(20 * "-+")
    for x in arquivo:
        x.replace("\n","")
        print(x)
    print(20 * "-+")
    time.sleep(5)

def apagar():
    lista_apagar = []
    lista_preenche = []
    palavra = input("Digite a palavra que deseja apagar: ")
    ler = open("c:\\db\lista.txt","r")
    ler_linhas = ler.readlines()
    for i in ler_linhas:
        if palavra in i:
            print(i)
            lista_apagar.append(i)
        else:
            lista_preenche.append(i+"\n")
    ler.close()
    abre = open("c:\\db\\lista.txt","w")
    for y in lista_preenche:
        abre.writelines(y)
    abre.close()
    return lista_preenche


def criar():
    lista = []
    while True:
        digite = input("Digite o diretorio e arquivo a ser criado: ").lower()
        try:
            diretorio = mkdir(digite)
            break
        except FileExistsError:
            print("Diretorio ja existe!")
            break
        except:
            print("Erro geral")
            continue
    arquivo = input("Digite o arquivo para ser criado: ")
    caminho = open(digite+"\\"+arquivo,"a")
    while True:
        num = 1
        nome = input("Digite seu nome completo: ").title()
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                break
            except:
                print("Digite a idade correta...")
                continue
        while True:
            try:
                altura = float(input("Digite sua altura: "))
                break
            except:
                print("Sua altura esta errado... seperação é por . e não , !")
        break
    ### PREENCHE O INDICE ###
    colunas = 1
    try:
        arquivo = open("C:\\db\\lista.txt", "r")
    except:
        print("Arquivo com erro ou não encontrado.")
    leitura = arquivo.readlines()
    for i in leitura:
        print(i)
        if "#" in i:
            colunas += 1
        else:
            continue
    arquivo.close()
    #### FIM DO PREENCHE COLUNAS ###
    lista.append(["#%s "%colunas ," %s "%nome , " %s "%str(idade) , " %s "%str(altura)+"\n"])
    for i in lista:
        caminho.writelines(i)
    caminho.close()
    return lista

def numero():
    colunas = 0
    arquivo = open("C:\\db\\lista.txt","r")
    leitura = arquivo.readlines()
    for i in leitura:
        #print(i)
        if "#" in i:
            colunas += 1
        else:
            continue
    print("Na tabela temos um total de %i"%colunas)
    return time.sleep(3)


###### LISTA DE ESCOLHA ####
while True:
    print(20*"-+")
    print("\033[1;32m"+"(S)air do SISTEMA"+"\033[0;0m")
    print("(I)ncluir novo funcionario.")
    print("(L)ista de cadastro de funcionarios.")
    print("(N)umero de cadastros.")
    print("(A)pagar registro de funcionarios"+"\033[0;0m")
    print(20*"-+")
    opcao = input("\033[1;31m"+"Digite a opcao deseja: "+"\033[0;0m").lower()[0]
    if opcao == "i":
        criar()
    elif opcao == "l":
        listar()
    elif opcao == "n":
        numero()
    elif opcao == "a":
        apagar()
    elif opcao == "s":
        print("Saindo do sistema!")
        break
    else:
        print("Digite uma opcao valida...")
        continue
