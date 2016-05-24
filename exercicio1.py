# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:54:15 2016

@author: Pedro
"""
import numpy as np
import cv2

imagemArray = cv2.imread('Lenna.jpg', 0)

#####################################################
  ################### FUNCOES ###################
#####################################################

def pontaCabeca():
    upsideDown = imagemArray[::-1,::-1]
    upsideDownArray = np.array(upsideDown)
    cv2.imwrite('outputUpsidedown.png', upsideDownArray)

def multTile():
    upsideDown = imagemArray[::-1,::-1]
    upsideDownArray = np.array(upsideDown)
    matrixLenna = np.tile(upsideDownArray, (2,3))
    cv2.imwrite('outputTiled.png', matrixLenna)


def contraste(contraste):
    imagemArray = cv2.imread('outputTiled.png', 0)
    fator = (100.0 + contraste)/ 100.0;
    fator *= fator;
    for i in range(0, len(imagemArray)):
        for j in range(0, len(imagemArray[i])):
            novoValor = imagemArray[i][j]                
            novoValor /= 255.0                
            novoValor -= 0.5                
            novoValor *= fator                
            novoValor += 0.5                
            novoValor *= 255.0                
            imagemArray[i][j] = limitaVal(novoValor)
    cv2.imwrite('outputContraste.png', imagemArray)
                        

def gradient(f):
    imagemArray = cv2.imread('outputTiled.png', 0)
    for i in range(0, len(imagemArray)):
        for j in range(0, len(imagemArray[i])):
            novoValor = imagemArray[i][j]
            novoValor -= (i+j)* f;
            imagemArray[i][j] = limitaVal(novoValor)  
    cv2.imwrite('outputGradient.png', imagemArray)

def limitaVal(valor):
    if (valor < 0):
        valor = 0;
    if (valor > 255):
        valor = 255;
    return valor


#####################################################
  ################### CHAMADAS ###################
#####################################################

pontaCabeca()

multTile()

contFator = 100
contraste(contFator)

gradFator = 0.15;
gradient(gradFator)
