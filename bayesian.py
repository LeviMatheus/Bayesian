#!/usr/bin/env python3
import numpy as np
import sys

class bayes:

    def __init__(self):
        # dataset
        self.ds = None
        self.d = None
        self.carregaDs()

    def carregaDs(self):

        def column(self, matrix, i):
            return [row[i] for row in matrix]

        entrada = sys.argv[1:] # PEGA O SEGUNDO INDICE COMO ENTRADA
        print("\n Analisando base de dados: ", entrada, "\n") # MOSTRA A ENTRADA
        arquivo = open(entrada[0], "r") # ABRE O ARQUIVO DE ENTRADA
        separador = arquivo.read().split("---\n")
        arquivo.close()
        #for conjunto in dataset:
            #print(conjunto) 
        dataset = separador[0]
        questoes = separador[1]
        #print("Dataset: \n", dataset)
        #print("",end="")
        #print("Questões: ", questoes)

        #CRIANDO VETOR DE INSTANCIAS DO DATASET E DAS QUESTOES

        instancias_dataset = dataset.split("\n") # LE CADA UMA DAS LINHAS E SEPARA COM /N
        instancias_dataset.pop()
        print("Dataset: \n")
        for i in range(len(instancias_dataset)):
            if i != 0: #PARA N PRINTAR O TITULO DOS ATRIBUTOS
                print(instancias_dataset[i]) # MOSTRA AS LINHAS	DAS INSTANCIAS DO DATASET
        
        print("\n")

        instancias_questoes = questoes.split("\n") # LE CADA UMA DAS LINHAS E SEPARA COM /N
        instancias_questoes.pop()
        questoes = []
        print("Questões:") 
        for i in instancias_questoes:
            questoes.append(i.split(" "))
        print(questoes) # MOSTRA AS LINHAS	DAS INSTANCIAS DO DATASET

        print("\n Atributos da instância: \n")
        #CRIAR VETOR DE ATRIBUTOS DE INSTANCIAS (dados)
        dados = []
        for i in instancias_dataset:
            dados.append(i.split(" "))
        print(dados) #DADOS É O VETOR COM AS INSTANCIAS A SEREM UTILIZADAS
        
        rotulos = []
        rotulos = dados.pop(0)
        #print(rotulos) #TITULOS SEPARADOS EM UM VETOR A PARTE

        totalLinhas = len(dados) #CONTANDO QTD DE INSTANCIAS
        #print(totalLinhas)

        coluna = []
        for i in dados:
            coluna.append(i[-1])
        #print(classes)
        #classes = set(coluna) # set antigo
        classes = dict.fromkeys(coluna).keys() #set novo
        classes = list(classes)
        '''print("Classes: ", classes)
        print("Classe 0: ", classes[0])
        print("Classe 1: ", classes[1])'''
        qtd0 = coluna.count(classes[0])#countagem de instancias
        qtd1 = coluna.count(classes[1])

        print("\n")
        print("Classe 0: ", classes[0], "Frequência: ", qtd0)
        print("Classe 1: ", classes[1], "Frequência: ", qtd1)

        p0 = qtd0/totalLinhas #porcentagem classe 0
        p1 = qtd1/totalLinhas #porcentagem classe 1
        print("Porcentagem da classe 0: ", p0)
        print("Porcentagem da classe 1: ", p1)

        qtdatributos = len(rotulos)-1
        print("Quantidade de atributos: ", qtdatributos)

        valAtributos = []
        for i in range(qtdatributos):
            valAtributos.append(list(dict.fromkeys(column(self, dados,i)).keys()))#valAtributos.append(set(column(self, dados,i)))
        #print(set(column(self, dados,0)))
        #print(atributos2)
        #print(valAtributos)

        freq = 0
        probAtribC0 = [] # vetor com a probabilidade de cada atributo para classe 0
        probAtribC1 = [] # vetor com a probabilidade de cada atributo para classe 1
        #verificar se dados[i][-1] = determinada classe
        for instancia in dados:
            if instancia[-1] == classes[0]:#se for da classe 0
                if(questoes[0][0] == column(self,instancia,0)[0]):#valAtributos[0][0], column(self,dados,0
                    freq += 1#print("verificando", questoes[0][0], " igual", column(self,instancia,0)[0])

        #calculo das prob para classe 0 = freq do atrib/freq da classe
        probAtribC0.append(freq/qtd0) #P(S/NAO)
        
        #adicionar as probabilidades ao vetor de prob da classe 0            
        print(probAtribC0)

bayes()


#TODO:A FUNCAO SET ESTA ALEATORIAMENTE COLOCANDO ELEMENTOS PRIMEIRO, ASSIM ESTA DIFICULTANDO O 
#PROCESSAMENTO NAS FUNCOES POSTERIORES, ARRANJAR ALGUMA FORMA DE ORGANIZAR O SET PARA PADRONIZAR SEMPRE
#UMA ORDEM