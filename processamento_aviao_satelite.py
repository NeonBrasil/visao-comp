# Processamento de Imagem - AVIAO.jpeg e SATELITE.jpeg
# pip install opencv-python matplotlib numpy

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def processar_imagem(nome_arquivo, titulo_principal):
    # Carregando a imagem
    img = cv2.imread(nome_arquivo)
    
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
    plt.savefig(f'{nome_arquivo.split(".")[0]}_intermediarias.png')
    plt.show()
    
    # Destacando a imagem final em tamanho grande
    plt.figure(figsize=(12, 10))
    plt.imshow(final)
    plt.title(f'Resultado Final - {titulo_principal} com Contornos', fontsize=16)
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.savefig(f'{nome_arquivo.split(".")[0]}_final.png')
    plt.show()
    
    print(f"Processamento da imagem {nome_arquivo} concluído!")
    print(f"Imagens salvas: {nome_arquivo.split('.')[0]}_intermediarias.png e {nome_arquivo.split('.')[0]}_final.png")
    
    return final

# Processando as imagens
print("Iniciando processamento das imagens...")

# Processando a imagem do avião
final_aviao = processar_imagem('AVIAO.jpeg', 'Avião')

# Processando a imagem do satélite
final_satelite = processar_imagem('SATELITE.jpeg', 'Satélite')

# Criando um relatório final com as três imagens processadas
plt.figure(figsize=(15, 5))

# Carregando a imagem final da girafa (assumindo que já foi processada)
final_girafa = cv2.imread('GIRAFA_final.png')
if final_girafa is not None:
    final_girafa = cv2.cvtColor(final_girafa, cv2.COLOR_BGR2RGB)
    plt.subplot(1, 3, 1)
    plt.imshow(final_girafa)
    plt.title('Girafa Processada')
    plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2)
plt.imshow(final_aviao)
plt.title('Avião Processado')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3)
plt.imshow(final_satelite)
plt.title('Satélite Processado')
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.savefig('resultados_finais.png')
plt.show()

print("\nTodos os processamentos concluídos!")
print("Resumo das técnicas aplicadas:")
print("1. Conversão para RGB")
print("2. Aplicação de blur para redução de ruído")
print("3. Conversão para escala de cinza")
print("4. Binarização da imagem")
print("5. Operações morfológicas (dilatação, erosão, abertura, fechamento)")
print("6. Detecção de bordas com Canny")
print("7. Identificação e desenho de contornos")
print("\nLink para o código fonte: https://github.com/seu-usuario/visao-computacional-processamento")