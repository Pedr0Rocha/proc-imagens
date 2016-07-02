# -*- coding: utf-8 -*-
"""
Created on Sat Jul 2 13:12:42 2016

@author: Pedro
"""
import numpy as np
import cv2

imagemArray = cv2.imread('Creepy.jpg', 0)

gamma = 0.1
gammaCorrectionValue = 1.0 / gamma

def gammaCorrection(imgArray, gammaCorrection):
	imgArray = imgArray/255.0
	imgArray = cv2.pow(imgArray, gammaCorrection)
	return imgArray

imagemArray = gammaCorrection(imagemArray, gammaCorrectionValue)

cv2.imshow('Resultado Gamma Correction', imagemArray)
cv2.imwrite('outputGammaCorrection.jpg', imagemArray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#http://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/