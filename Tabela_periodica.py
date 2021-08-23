import csv
import os

tabela_periodica = {}

#Funçoes:

def dado():
    if dados == "1":
            print(elemento['nome'])
    elif dados == "2":
            print(elemento['atomico'])
    elif dados == "3":
            print(elemento['simbolo'])
    elif dados == "4":
            print(elemento['linha'])
    elif dados == "5":
            print(elemento['coluna'])
    elif dados == "6":
            print(elemento['estado'])
    else:
            print("Dado Invalido!!! (Digite os Numeros!)")
def cls():
    os.system("cls")
def escolhas():
    print("Mercurio\nHidrogenio\nLitio\nCalcio\nRutenio\nZinco\nAfnio\nCarbono\nCloro\nArsenio")

    
dadozinho = ("Quais dados quer saber?\n1-Nome\n2-Número Atômico\n3-Símbolo\n4-Linha\n5-Coluna\n6-Estado\n:")




arq = csv.reader(open('tabela.txt'), delimiter=';')
for i,dado_linha in enumerate(arq):
    if i == 0: 
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] # simbolo
    dados['nome'] = dado_linha[1] # nome
    dados['atomico'] = dado_linha[2] # nome
    dados['linha'] = dado_linha[3] # nome
    dados['coluna'] = dado_linha[4]
    dados['estado'] = dado_linha[5]
    tabela_periodica[dados['simbolo']] = dados

while True:
    cls()
    escolhas()
    escolher = input("Digite Algum dos Elementos Acima: ")
    cls()
    if escolher == "Mercurio":
        elemento = tabela_periodica['Hg']
        dados = input(dadozinho)
        dado()

    elif escolher == "Hidrogenio":
        elemento = tabela_periodica['H']
        dados = input(dadozinho)
        dado()
    elif escolher == "Litio":
        elemento = tabela_periodica['Li']
        dados = input(dadozinho)
        dado()
    elif escolher == "Calcio":
        elemento = tabela_periodica['C']
        dados = input(dadozinho)
        dado()
    elif escolher == "Rutenio":
        elemento = tabela_periodica['Ru']
        dados = input(dadozinho)
        dado()
    elif escolher == "Zinco":
        elemento = tabela_periodica['Zn']
        dados = input(dadozinho)
        dado()
    elif escolher == "Hafnio":
        elemento = tabela_periodica['Hf']
        dados = input(dadozinho)
        dado()
    elif escolher == "Carbono":
        elemento = tabela_periodica['C']
        dados = input(dadozinho)
        dado()
    elif escolher == "Cloro":
        elemento = tabela_periodica['Cl']
        dados = input(dadozinho)
        dado()
    elif escolher == "Arsenio":
        elemento = tabela_periodica['As']
        dados = input(dadozinho)
        dado()


    input()