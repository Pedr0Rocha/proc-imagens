# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:19:30 2016

@author: Pedro
"""
import numpy as np
import cv2

imagemArray = cv2.imread('imagem.png', 0)
listaObjetos = []

class Objeto:
    def __init__(self, rotulo, id, coord):
        self.rotulo = rotulo
        self.id = id 
        self.coord = []

def achaNovaRaiz(matriz):
    novaRaiz = np.where(matriz == 255)
    print "Nova raiz x =", novaRaiz[0][0], " y =", novaRaiz[1][0]
    return (novaRaiz[0][0], novaRaiz[1][0])

def identificaObjetos(matriz):
    numObjetos = 0
    raizBusca = (imagemArray.nonzero()[0][0], imagemArray.nonzero()[1][0])
    print "Primeira Raiz x =", raizBusca[0], " y =", raizBusca[1]
    
    rotulo = 0;   
    while (1):
        rotulo += 1
        numObjetos += 1
        print "Objeto Encontrado"
        print "Rótulo do Objeto:", rotulo, "\n"
        listaObjetos.append(Objeto(numObjetos, rotulo, []))
        buscaEmLargura(raizBusca, matriz, rotulo)
        if (255 not in matriz):
            break
        raizBusca = achaNovaRaiz(matriz)
        
    return numObjetos

def buscaEmLargura(raiz, matriz, rotulo):
    fila = [(raiz[0], raiz[1])]
    
    visitados = []

    while (len(fila) != 0):
        v = fila.pop(0)
        if (v not in visitados):
            visitados.append(v)
            imagemArray[v[0]][v[1]] = rotulo
            vizinhos = checa8vizinhos(v, matriz)
            listaObjetos[rotulo-1].coord.extend(vizinhos)
            fila.extend(vizinhos)
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

def achaLimites(coord):
    listaX, listaY = zip(*coord)
    maxX = max(listaX)
    minX = min(listaX)
    maxY = max(listaY)
    minY = min(listaY)
    return [maxX, minX, maxY, minY]

def adicionaMargem(matriz, largura, iaxis, kwargs):
    matriz[:largura[0]] = 0
    matriz[-largura[1]] = 0
    return matriz

qtaObjs = identificaObjetos(imagemArray)    
print "Quantidade de Objetos:", qtaObjs
cv2.imwrite('outputRotulado.png', imagemArray)

objetoRecortar = -1
while ((objetoRecortar < 1) | (objetoRecortar > len(listaObjetos))):
    objetoRecortar = raw_input("Qual dos objetos deseja recortar? \n>")
    objetoRecortar = int(objetoRecortar)

limiteInferior, limiteSuperior, limiteDireita , limiteEsquerda  = achaLimites(listaObjetos[objetoRecortar-1].coord)

objRecortado = imagemArray[limiteSuperior:limiteInferior+1, limiteEsquerda:limiteDireita+1]
objRecortado = np.where(objRecortado!=0, 255, objRecortado)
objRecortado = np.lib.pad(objRecortado, 3, adicionaMargem)

cv2.imwrite('objRecortado.png', objRecortado)