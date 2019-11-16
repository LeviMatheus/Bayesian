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

        classes = []
        for i in dados:
            classes.append(i[-1])
        #print(classes)

bayes()