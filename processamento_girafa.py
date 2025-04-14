# Processamento de Imagem - GIRAFA.jpeg
# pip install opencv-python matplotlib numpy

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

# Carregando a imagem
img = cv2.imread('GIRAFA.jpeg')

# Convertendo para RGB (OpenCV carrega em BGR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Aplicando blur para redução de ruído
img_blur = cv2.blur(img_rgb, (5, 5))

# Convertendo para escala de cinza
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)

# Binarização da imagem
a = img_gray.max()
_, img_thresh = cv2.threshold(img_gray, a/2+30, a, cv2.THRESH_BINARY_INV)

# Definindo kernel para operações morfológicas
kernel = np.ones((7, 7), np.uint8)

# Aplicando operações morfológicas
img_dilate = cv2.dilate(img_thresh, kernel, iterations=1)
img_erode = cv2.erode(img_thresh, kernel, iterations=1)
img_open = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
img_close = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)

# Detecção de bordas com Canny
edges = cv2.Canny(image=img_gray, threshold1=a/2, threshold2=a/2)

# Encontrando contornos
contours, _ = cv2.findContours(
    image=img_close,
    mode=cv2.RETR_TREE,
    method=cv2.CHAIN_APPROX_SIMPLE
)

# Ordenando contornos por área (do maior para o menor)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Desenhando contornos na imagem original
img_contours = img_rgb.copy()
final = cv2.drawContours(img_contours, contours, contourIdx=-1, color=(255, 0, 0), thickness=2)

# Preparando imagens para visualização
imagens_intermediarias = [
    img_rgb, img_blur, img_gray, img_thresh,
    img_dilate, img_erode, img_open, img_close, edges, final
]

titulos = [
    'Original RGB', 'Blur', 'Escala de Cinza', 'Limiarização',
    'Dilatação', 'Erosão', 'Abertura', 'Fechamento', 'Bordas Canny', 'Contornos'
]

# Plotando imagens intermediárias
formatoX = math.ceil(len(imagens_intermediarias) ** 0.5)
if (formatoX**2 - len(imagens_intermediarias)) > formatoX:
    formatoY = formatoX - 1
else:
    formatoY = formatoX

plt.figure(figsize=(15, 10))
for i in range(len(imagens_intermediarias)):
    plt.subplot(formatoY, formatoX, i + 1)
    if i == 0 or i == 1 or i == 9:  # Imagens coloridas
        plt.imshow(imagens_intermediarias[i])
    else:  # Imagens em escala de cinza
        plt.imshow(imagens_intermediarias[i], 'gray')
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.savefig('GIRAFA_intermediarias.png')
plt.show()

# Destacando a imagem final em tamanho grande
plt.figure(figsize=(12, 10))
plt.imshow(final)
plt.title('Resultado Final - Girafa com Contornos', fontsize=16)
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.savefig('GIRAFA_final.png')
plt.show()

print("Processamento da imagem GIRAFA.jpeg concluído!")
print("Imagens salvas: GIRAFA_intermediarias.png e GIRAFA_final.png")