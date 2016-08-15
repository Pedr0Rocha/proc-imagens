# -*- coding: utf-8 -*-
"""
Created on Sat Jul 2 13:12:42 2016

@author: Pedro
"""
import numpy as np
import cv2

imagemArray = cv2.imread('Creepy.jpg', 1)
imagemHsv = cv2.cvtColor(imagemArray, cv2.COLOR_BGR2HSV)
imagemLab = cv2.cvtColor(imagemArray, cv2.COLOR_BGR2LAB)

gamma = 5
inputGamma = float(input('Digite o valor de gamma para aplicar a correção > '))

def normalize(imgArray):
	maxValue = float(np.max(imgArray))
	minValue = float(np.min(imgArray))
	imgArray = (imgArray - minValue) / (maxValue - minValue)
	return imgArray

def gammaCorrection(imgArray, gammaValue):
	maxValue = float(np.max(imgArray))
	imgArray = normalize(imgArray)
	imgArray = imgArray**gammaValue
	imgArray = maxValue * imgArray
	return imgArray

# aplica somente no channel 2
def gammaCorrectionHSV(imgArray, gammaValue):
	maxValue = float(np.max(imgArray))
	imgArray = normalize(imgArray)
	imgArray[:, :, 2] = imgArray[:, :, 2]**gammaValue
	imgArray = maxValue * imgArray
	return imgArray

# aplica somente no channel 0
def gammaCorrectionLAB(imgArray, gammaValue):
	maxValue = float(np.max(imgArray))
	imgArray = normalize(imgArray)
	imgArray[:, :, 0] = imgArray[:, : , 0]**gammaValue
	imgArray = maxValue * imgArray
	return imgArray

outputRGB = gammaCorrection(imagemArray, inputGamma)
outputHSV = gammaCorrectionHSV(imagemHsv, inputGamma)
outputLAB = gammaCorrectionLAB(imagemLab, inputGamma)

outputRGB = np.uint8(outputRGB)
outputHSV = np.uint8(outputHSV)
outputLAB = np.uint8(outputLAB)

imagemHsv = cv2.cvtColor(outputHSV, cv2.COLOR_HSV2BGR)
imagemLab = cv2.cvtColor(outputLAB, cv2.COLOR_LAB2BGR)

cv2.imshow('Imagem Original', imagemArray)

cv2.imshow('Gamma Correction - RGB', outputRGB)
#cv2.imwrite('outputGammaCorrectionRGB.jpg', outputRGB)

cv2.imshow('Gamma Correction - HSV', imagemHsv)
#cv2.imwrite('outputGammaCorrectionHSV.jpg', imagemHsv)

cv2.imshow('Gamma Correction - LAB', imagemLab)
#cv2.imwrite('outputGammaCorrectionLAB.jpg', imagemLab)

cv2.waitKey(0)
cv2.destroyAllWindows()
