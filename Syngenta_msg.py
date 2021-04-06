"""
    Esse código é responsável por tentar encontrar uma mensagem escondida
    dentro da imagem fornecida pela Syngenta.
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

# Encontrando valores úteis
texto_final = np.zeros((height, width)).astype(int) # Vetor texto
indice_w = [] # Vetor com os índices na horizontal
indice_h = [] # Vetor com os índices na vertical

# É necessário utilizar dois "for" uma vez que quando se altera a ordem
# de percurso da imagem, também se altera os indices, e portanto, fica
# inviável salvar os índices dentro de um só for.
for i in range(height):
    for j in range(width):
        if ((img[i, j] >= verde_min).all() and (img[i, j] <= verde_max).all()):
            texto_final[i, j] = 1
            indice_w.append(j)

for i in range(width):
    for j in range(height):
        if ((img[j, i] >= verde_min).all() and (img[j, i] <= verde_max).all()):
            indice_h.append(j)


# ---------------------------- TENTATIVA UM -------------------------------
# salva-se o vetor binarizado da imagem em um arquivo de texto

#with open("text.txt", "w") as output_file:
#    output_file.write("".join(texto_final.reshape(-1).astype(int).astype(str)))

# Como não gerou bons resultados, printa-se o valor retirando-se os blocos com
# 8 zeros seguidos:

# aux = texto_final.T.reshape(-1).astype(int)
# texto_final_sem_zeros = []
# for i in range(0, height*width, 8):
    # if (aux[i:i + 8] != [0, 0, 0, 0, 0, 0, 0, 0]).any():
        # texto_final_sem_zeros += aux[i:i + 8].tolist()
# 
# print("".join(np.array(texto_final_sem_zeros).astype(str)))


# --------------------------- TENTATIVA DOIS ------------------------------
# Conta-se a quantidade de pontos verdes em cada linha ou coluna
contagem_vertical = []
contagem_horizontal = []
for i in range(width):
   contagem_vertical.append((texto_final[:, i].tolist().count(1)))
for i in range(height):
   contagem_horizontal.append((texto_final[i, :].tolist().count(1)))
print(contagem_vertical)
print(contagem_horizontal)


# --------------------------- TENTATIVA TRÊS ------------------------------
# Exibe a posição relativa ao pixel verde na imagem (alguns pixels verdes são 
# próximos)
print(indice_w)
print(indice_h)


