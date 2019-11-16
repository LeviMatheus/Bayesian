#!/usr/bin/env python3
import numpy as np
import sys
import re

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
        #RETIRAR VAZIOS
        #dataset = " ".join(re.split("\s+", dataset, flags=re.UNICODE))
        #dataset.strip()
        #print(dataset)
        #questoes = " ".join(re.split("\s+", dataset, flags=re.UNICODE))
        #questoes.strip()
        #print(questoes)
        #print("Dataset: \n", dataset)
        #print("",end="")
        #print("Questões: ", questoes)

        #CRIANDO VETOR DE INSTANCIAS DO DATASET E DAS QUESTOES

        instancias_dataset = dataset.split("\n") # LE CADA UMA DAS LINHAS E SEPARA COM /N
        instancias_dataset.pop()
        #print(instancias_dataset)
        for i in range(len(instancias_dataset)):
            instancias_dataset[i] = " ".join(re.split("\s+", instancias_dataset[i], flags=re.UNICODE))
            instancias_dataset[i] = re.sub("^\s+|\s+$", "", instancias_dataset[i], flags=re.UNICODE)
        print(instancias_dataset)
        '''print("Dataset: \n")
        for i in range(len(instancias_dataset)):
            if i != 0: #PARA N PRINTAR O TITULO DOS ATRIBUTOS
                print(instancias_dataset[i]) # MOSTRA AS LINHAS	DAS INSTANCIAS DO DATASET'''
        
        print("\n")

        instancias_questoes = questoes.split("\n") # LE CADA UMA DAS LINHAS E SEPARA COM /N
        instancias_questoes.pop()
        for i in range(len(instancias_questoes)):
            instancias_questoes[i] = " ".join(re.split("\s+", instancias_questoes[i], flags=re.UNICODE))
            instancias_questoes[i] = re.sub("^\s+|\s+$", "", instancias_questoes[i], flags=re.UNICODE)
        questoes = []
        print("Questões:") 
        for i in instancias_questoes:
            questoes.append(i.split(" "))
        print(questoes) # MOSTRA AS LINHAS	DAS INSTANCIAS DO DATASET

        print("\n Valores dos atributos das instâncias: \n")
        #CRIAR VETOR DE ATRIBUTOS DE INSTANCIAS (dados)
        dados = []
        for i in instancias_dataset:
            dados.append(i.split(" "))
         
        rotulos = []
        rotulos = dados.pop(0)
        #print(rotulos) #TITULOS SEPARADOS EM UM VETOR A PARTE
        print(dados) #DADOS É O VETOR COM AS INSTANCIAS A SEREM UTILIZADAS

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
        
        if len(classes) <= 1:
            print("\n Erro: classes devem ser binárias, aplicação encerrada \n")
            exit()
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
        print("Quantidade de instancias na base: ", len(dados))
        print("Quantidade de questões: ", len(questoes))

        valAtributos = []
        for i in range(qtdatributos):
            valAtributos.append(list(dict.fromkeys(column(self, dados,i)).keys()))#valAtributos.append(set(column(self, dados,i)))
        #print(set(column(self, dados,0)))
        #print(atributos2)
        #print(valAtributos)

        print("\n")

        for q in range(len(questoes)):
            freq0 = 0
            freq1 = 0
            probAtribC0 = [] # vetor com a probabilidade de cada atributo para classe 0
            probAtribC1 = [] # vetor com a probabilidade de cada atributo para classe 1
            print("Questão: ", q)
            #calculo para classe 0
            for j in range(qtdatributos):
                for instancia in dados:
                    if instancia[-1] == classes[0]:#se for da classe 0
                        if(questoes[q][j] == column(self,instancia,0)[j]):#valAtributos[0][0], column(self,dados,0
                            freq0 += 1#print("verificando", questoes[0][j], " igual", column(self,instancia,0)[j])
                probAtribC0.append(freq0/qtd0)
                freq0 = 0
            #adicionando ao vetor
            probAtribC0.append(p0)#adicionar a probabilidade da classe 1 ao vetor de probabilidades
            totalC0 = 1
            for i in probAtribC0:
                totalC0 = totalC0*i
            
            #print("Probabilidades: ", probAtribC0)
            print(classes[0], "= ", totalC0)

            #calculo para classe 1
            for k in range(qtdatributos):
                for instancia in dados:
                    if instancia[-1] == classes[1]:#se for da classe 1
                        if(questoes[q][k] == column(self,instancia,0)[k]):#valAtributos[0][0], column(self,dados,0
                            freq1 += 1#print("verificando", questoes[0][j], " igual", column(self,instancia,0)[j])
                #print("Freq atrib: ", freq1)
                probAtribC1.append(freq1/qtd1)
                freq1 = 0
            #print("qtd: ", qtd1)
            #adicionando ao vetor
            probAtribC1.append(p1)#adicionar a probabilidade da classe 1 ao vetor de probabilidades
            #print(probAtribC1)
            totalC1 = 1
            for l in probAtribC1:
                totalC1 = totalC1*l
            
            #print("Probabilidades: ", probAtribC1)
            print(classes[1], "= ", totalC1)

            if(totalC1>totalC0):
                print("==> Jogar=",classes[1])
            else:
                print("==> Jogar=",classes[0])

            print("\n")

        '''for q in questoes:
            freq0 = 0
            freq1 = 0
            probAtribC0 = [] # vetor com a probabilidade de cada atributo para classe 0
            probAtribC1 = [] # vetor com a probabilidade de cada atributo para classe 1
            print("Questão: ", q)
            #calculo para classe 0
            for j in range(qtdatributos):
                for instancia in dados:
                    if instancia[-1] == classes[0]:#se for da classe 0
                        if(questoes[0][j] == column(self,instancia,0)[j]):#valAtributos[0][0], column(self,dados,0
                            freq0 += 1#print("verificando", questoes[0][j], " igual", column(self,instancia,0)[j])
                probAtribC0.append(freq0/qtd0)
                freq0 = 0
            #adicionando ao vetor
            probAtribC0.append(p0)#adicionar a probabilidade da classe 1 ao vetor de probabilidades
            totalC0 = 1
            for i in probAtribC0:
                totalC0 = totalC0*i
            
            #print("Probabilidades: ", probAtribC0)
            print(classes[0], "= ", totalC0)

            #calculo para classe 1
            for k in range(qtdatributos):
                for instancia in dados:
                    if instancia[-1] == classes[1]:#se for da classe 1
                        if(questoes[0][k] == column(self,instancia,0)[k]):#valAtributos[0][0], column(self,dados,0
                            freq1 += 1#print("verificando", questoes[0][j], " igual", column(self,instancia,0)[j])
                #print("Freq atrib: ", freq1)
                probAtribC1.append(freq1/qtd1)
                freq1 = 0
            #print("qtd: ", qtd1)
            #adicionando ao vetor
            probAtribC1.append(p1)#adicionar a probabilidade da classe 1 ao vetor de probabilidades
            #print(probAtribC1)
            totalC1 = 1
            for l in probAtribC1:
                totalC1 = totalC1*l
            
            #print("Probabilidades: ", probAtribC1)
            print(classes[1], "= ", totalC1)

            if(totalC1>totalC0):
                print("==> Jogar=",classes[1])
            else:
                print("==> Jogar=",classes[0])

            print("\n")'''

bayes()


#TODO:A FUNCAO SET ESTA ALEATORIAMENTE COLOCANDO ELEMENTOS PRIMEIRO, ASSIM ESTA DIFICULTANDO O 
#PROCESSAMENTO NAS FUNCOES POSTERIORES, ARRANJAR ALGUMA FORMA DE ORGANIZAR O SET PARA PADRONIZAR SEMPRE
#UMA ORDEM