# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:19:30 2016

@author: Pedro
"""
import numpy as np
import sys
sys.path.append('C:/Python27/Lib/site-packages/')
import cv2

imagemArray = cv2.imread('imagem.png', 0)

def achaNovaRaiz(matriz):
    novaRaiz = np.where(matriz == 255)
    print "Nova raiz x =", novaRaiz[0][0], " y =", novaRaiz[1][0]
    return (novaRaiz[0][0], novaRaiz[1][0])

def identificaObjetos(matriz):
    numObjetos = 0
    raizBusca = (imagemArray.nonzero()[0][0], imagemArray.nonzero()[1][0])
    print "Primeira Raiz x =", raizBusca[0], " y =", raizBusca[1]
    
    cor = 0;   
    while (1):
        cor += 20
        numObjetos += 1
        print "Objeto Encontrado"
        print "Rótulo do Objeto:", cor, "\n"
        buscaEmLargura(raizBusca, matriz, cor)
        if (255 not in matriz):
            break
        raizBusca = achaNovaRaiz(matriz)
        
    return numObjetos

def buscaEmLargura(raiz, matriz, cor):
    fila = [(raiz[0], raiz[1])]
    
    visitados = []

    while (len(fila) != 0):
        v = fila.pop(0)
        if (v not in visitados):
            visitados.append(v)
            imagemArray[v[0]][v[1]] = cor
            fila.extend(checa8vizinhos(v, matriz))
    return visitados
    
def checa8vizinhos(v, matriz):
    x = v[0]
    y = v[1]
    vizinhos = []
    if (matriz[x][y-1] == 255):
        vizinhos.append((x, y-1))
    if (matriz[x][y+1] == 1):
        vizinhos.append((x, y+1))
    if (matriz[x-1][y] == 255):
        vizinhos.append((x-1, y))
    if (matriz[x+1][y] == 255):
        vizinhos.append((x+1, y))
    if (matriz[x-1][y+1] == 255):
        vizinhos.append((x-1, y+1))
    if (matriz[x-1][y-1] == 255):
        vizinhos.append((x-1, y-1))
    if (matriz[x+1][y+1] == 255):
        vizinhos.append((x+1, y+1))
    if (matriz[x+1][y-1] == 255):
        vizinhos.append((x+1, y-1))
    return vizinhos    

qtaObjs = identificaObjetos(imagemArray)    
print "QUANTIDADE DE OBJETOS:", qtaObjs
cv2.imwrite('output.png', imagemArray)

                
