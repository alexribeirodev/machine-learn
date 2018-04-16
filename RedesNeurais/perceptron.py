# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
import time

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0,0,1])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    timeInit = time.perf_counter()
    ciclos = 0
    erroTotal = 1
    while erroTotal != 0:
        ciclos += 1
        erroTotal = 0        
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.array(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print("Peso atualizado: " + str(pesos[j]))
        print("Total de erros: " + str(erroTotal))
    print("Time em segundos: {}".format((time.perf_counter() - timeInit)))        
    return ciclos;
        
r = treinar()
print("Rede neural treinada!")
print("Pesos definidos: {} {}".format(pesos[0], pesos[1]))
print(str(calculaSaida(entradas[0])))
print(str(calculaSaida(entradas[1])))
print(str(calculaSaida(entradas[2])))
print(str(calculaSaida(entradas[3])))
print("Total de ciclos: " + str(r))