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
        separador = arquivo.read().split("---")
        #arquivo.close()
        #for conjunto in dataset:
            #print(conjunto) 
        dataset = separador[0]
        questoes = separador[1]
        print("Dataset: \n", dataset)
        print("")
        print("Questões: ", questoes)

        instancias = dataset.split("\n") # LE CADA UMA DAS LINHAS E SEPARA COM /N
        instancias.pop() 
        for i in instancias:
            print(i) # MOSTRA AS LINHAS	
        arquivo.close() # FECHA O ARQUIVO#

bayes()