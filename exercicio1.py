# -*- coding: utf-8 -*-
"""
Created on Thu May 12 20:54:15 2016

@author: Pedro
"""
import numpy as np
import cv2

imagemArray = cv2.imread('Lenna.jpg', 0)

#vira a imagem de ponta cabeca
def pontaCabeca():
    upsideDown = imagemArray[::-1,::-1]
    upsideDownArray = np.array(upsideDown)
    cv2.imwrite('outputUpsidedown.png', upsideDownArray)

#multiplica a imagem usando tile
def multTile():
    upsideDown = imagemArray[::-1,::-1]
    upsideDownArray = np.array(upsideDown)
    matrixLenna = np.tile(upsideDownArray, (2,3))
    cv2.imwrite('outputTiled.png', matrixLenna)

#teste de contraste na imagem - nao usado para o trabalho
def contraste(contraste):
    imagemArray = cv2.imread('outputTiled.png', 0)
    fator = (100.0 + contraste)/ 100.0;
    fator *= fator;
    imagemArray = imagemArray / 255.0
    imagemArray = (imagemArray - 0.5) * fator
    imagemArray = (imagemArray + 0.5) * 255.0
    cv2.imshow('Output Contraste', imagemArray)
    #cv2.imwrite('outputContraste.png', imagemArray)
                        
#aplica gradiente em diagonal na imagem
def gradient(f):
    imagemArray = cv2.imread('outputTiled.png', 0)
    for i in range(0, len(imagemArray)):
        for j in range(0, len(imagemArray[i])):
            novoValor = imagemArray[i][j]
            novoValor -= (i+j)* f;
            imagemArray[i][j] = limitaVal(novoValor)  
    cv2.imshow('Output Gradiente', imagemArray)
    #cv2.imwrite('outputGradient.png', imagemArray)

def limitaVal(valor):
    if (valor < 0):
        valor = 0;
    if (valor > 255):
        valor = 255;
    return valor

pontaCabeca()
multTile()

contFator = 50.0
contraste(contFator)

gradFator = 0.15;
gradient(gradFator)

cv2.waitKey(0)
cv2.destroyAllWindows()
