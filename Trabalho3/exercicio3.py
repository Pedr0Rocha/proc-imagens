# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 23:31:37 2016

@author: juliano
"""

import numpy as np
import cv2

img = cv2.imread('Lenna_Colorido.jpg', 0)
#RGB no opencv -->> (Blue, Green, Red)

#Cor inicial aleatoria entre 0 e 255
b1 = np.random.randint(0,255)
g1 = np.random.randint(0,255)
r1 = np.random.randint(0,255)

#Cor final aleatoria entre 0 e 255
b2 = np.random.randint(0,255)
g2 = np.random.randint(0,255)
r2 = np.random.randint(0,255)

#retorna numeros dentro do intervalo RBG(inicia =b1 até final=b2 no intervalo de 256)
b = np.linspace(b1,b2,256) #atribuiu altura da paleta 
g = np.linspace(g1,g2,256)
r = np.linspace(r1,r2,256)

#retorna resp(altura, largura)....tile(ras...vai varrer a imagem 256 vezes no eixo largura)        
p1 = np.tile(b.reshape(256,1), 256)
p2 = np.tile(g.reshape(256,1), 256)
p3 = np.tile(r.reshape(256,1), 256)
       
#uint8 converter números para 8 bits para a paleta solicitada no trabalho
p1 = np.uint8(p1)
p2 = np.uint8(p2)
p3 = np.uint8(p3)

#concatena o vetor de 2 em 2 ... (p1,p2)...(p3)        
paleta = np.dstack((np.dstack((p1,p2)), p3))
cv2.imshow('Paleta de Cores', paleta)
cv2.imwrite('outputPaleta.jpg', paleta)

paleta = paleta[::, 0]

#cria matriz de tamanho da imagem e add dimensao(3) a imagem            
imagemPaleta = np.zeros((img.shape[0], img.shape[1], 3))

#for[::, ::]
imagemPaleta[::, ::] = paleta[img[::, ::]]
imagemPaleta = np.uint8(imagemPaleta)

cv2.imshow('Imagem Final', imagemPaleta)
cv2.imwrite('outputColorido.jpg', imagemPaleta)

cv2.waitKey(0)
cv2.destroyAllWindows()
