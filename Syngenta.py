"""
    Esse código é responsável por encontrar a quantidade de pixels verdes
    existentes em uma imagem. A abordagem adotada foi definir uma margem de
    erro para o valor dos pixels verdes e se contar os pixels que pertenciam
    a essa margem
"""
import cv2
import numpy as np

# Caminho da imagem no disco
path = "/home/luan/Downloads/desafio_pixel_syngenta_digital/Syngenta.bmp"

# Leitura da imagem usando a OpenCv
img = cv2.imread(path)

# Para encontrar o valor RGB dos pixels verdes
cv2.imshow('image', img)
cv2.waitKey(0)

# Definição do valor nominal dos pixels verdes
verde_bgr = (0, 192, 96) # Formato padrão do OpenCv é BGR

# Uma vez que não foram verificados os valores de todos os pixels verdes
# pode ser que algum deles tenha valor diferente do nominal definido
# anteriormente. Para isso defini-se uma margem de "verde" com 15% do valor
# nominal
verde_min = (np.array(verde_bgr)*0.85).astype(int)
verde_max = (np.array(verde_bgr)*1.15).astype(int)
(height, width) = img.shape[:2] # dimensão da imagem

# Contagem de pixels verdes
total_verde = 0
for i in range(height):
    for j in range(width):
        if ((img[i, j] >= verde_min).all() and (img[i, j] <= verde_max).all()):
            total_verde += 1

# Resultado
print("O número total de pixels verdes é {}".format(total_verde))
