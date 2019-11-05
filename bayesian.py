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
        dtst = sys.argv[1:]
        print(dtst)
        arquivo = open(dtst[0], "r")
        linhas = arquivo.read().split("\n")
        linhas.pop()
        for linha in linhas:
            print(linha)	
        arquivo.close()

bayes()
