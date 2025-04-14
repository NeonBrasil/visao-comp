# Processamento de Imagens - Relatório Completo
# pip install opencv-python matplotlib numpy

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def processar_imagem(nome_arquivo, titulo_principal, ajuste_threshold=30, tamanho_kernel=7):
    print(f"\nProcessando a imagem {nome_arquivo}...")
    
    # Passo 1: Carregando a imagem
    print("Passo 1: Carregando a imagem original")
    img = cv2.imread(nome_arquivo)
    if img is None:
        raise FileNotFoundError(f"Não foi possível encontrar a imagem: {nome_arquivo}")
    
    # Passo 2: Convertendo para RGB (OpenCV carrega em BGR)
    print("Passo 2: Convertendo de BGR para RGB")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Passo 3: Aplicando blur para redução de ruído
    print("Passo 3: Aplicando filtro de blur para redução de ruído")
    img_blur = cv2.blur(img_rgb, (5, 5))
    
    # Passo 4: Convertendo para escala de cinza
    print("Passo 4: Convertendo para escala de cinza")
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
    
    # Passo 5: Binarização da imagem
    print("Passo 5: Aplicando limiarização (threshold) para binarização")
    a = img_gray.max()
    _, img_thresh = cv2.threshold(img_gray, a/2+ajuste_threshold, a, cv2.THRESH_BINARY_INV)
    
    # Passo 6: Definindo kernel para operações morfológicas
    print("Passo 6: Definindo kernel para operações morfológicas")
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)
    
    # Passo 7: Aplicando operações morfológicas
    print("Passo 7: Aplicando operações morfológicas")
    img_dilate = cv2.dilate(img_thresh, kernel, iterations=1)
    img_erode = cv2.erode(img_thresh, kernel, iterations=1)
    img_open = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)
    img_close = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)
    
    # Passo 8: Detecção de bordas com Canny
    print("Passo 8: Aplicando detector de bordas Canny")
    edges = cv2.Canny(image=img_gray, threshold1=a/2, threshold2=a/2)
    
    # Passo 9: Encontrando contornos
    print("Passo 9: Encontrando contornos na imagem")
    contours, _ = cv2.findContours(
        image=img_close,
        mode=cv2.RETR_TREE,
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    
    # Passo 10: Ordenando contornos por área (do maior para o menor)
    print("Passo 10: Ordenando contornos por área")
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # Passo 11: Desenhando contornos na imagem original
    print("Passo 11: Desenhando contornos na imagem original")
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
    print("Gerando visualização das imagens intermediárias...")
    formatoX = math.ceil(len(imagens_intermediarias) ** 0.5)
    if (formatoX**2 - len(imagens_intermediarias)) > formatoX:
        formatoY = formatoX - 1
    else:
        formatoY = formatoX
    
    plt.figure(figsize=(15, 12))
    for i in range(len(imagens_intermediarias)):
        plt.subplot(formatoY, formatoX, i + 1)
        if i == 0 or i == 1 or i == 9:  # Imagens coloridas
            plt.imshow(imagens_intermediarias[i])
        else:  # Imagens em escala de cinza
            plt.imshow(imagens_intermediarias[i], 'gray')
        plt.title(titulos[i])
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    nome_base = nome_arquivo.split(".")[0]
    plt.savefig(f'{nome_base}_intermediarias.png')
    plt.show()
    
    # Destacando a imagem final em tamanho grande
    print("Gerando imagem final em tamanho grande...")
    plt.figure(figsize=(12, 10))
    plt.imshow(final)
    plt.title(f'Resultado Final - {titulo_principal} com Contornos', fontsize=16)
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.savefig(f'{nome_base}_final.png')
    plt.show()
    
    print(f"Processamento da imagem {nome_arquivo} concluído!")
    print(f"Imagens salvas: {nome_base}_intermediarias.png e {nome_base}_final.png")
    
    return final, imagens_intermediarias, titulos

# Função para criar o relatório final
def criar_relatorio_final(resultados):
    print("\nCriando relatório final com todas as imagens processadas...")
    
    # Criando figura para mostrar os resultados finais lado a lado
    plt.figure(figsize=(15, 5))
    
    for i, (nome, resultado, _) in enumerate(resultados):
        plt.subplot(1, 3, i+1)
        plt.imshow(resultado)
        plt.title(f'{nome} Processado')
        plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.savefig('resultados_finais.png')
    plt.show()
    
    # Criando relatório detalhado com todas as etapas
    print("Gerando relatório detalhado com todas as etapas do processamento...")
    
    plt.figure(figsize=(18, 15))
    
    # Para cada imagem, mostrar todas as etapas do processamento
    for img_idx, (nome, _, imagens_intermediarias) in enumerate(resultados):
        for step_idx, img in enumerate(imagens_intermediarias[:5]):  # Primeiras 5 etapas
            plt.subplot(3, 5, img_idx*5 + step_idx + 1)
            if step_idx < 2:  # Imagens coloridas
                plt.imshow(img)
            else:  # Imagens em escala de cinza
                plt.imshow(img, 'gray')
            plt.title(f"{nome} - {titulos[step_idx]}")
            plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.savefig('relatorio_etapas_parte1.png')
    plt.show()
    
    plt.figure(figsize=(18, 15))
    for img_idx, (nome, _, imagens_intermediarias) in enumerate(resultados):
        for step_idx, img in enumerate(imagens_intermediarias[5:]):  # Últimas 5 etapas
            plt.subplot(3, 5, img_idx*5 + step_idx + 1)
            if step_idx == 4:  # Imagem final com contornos (colorida)
                plt.imshow(img)
            else:  # Imagens em escala de cinza
                plt.imshow(img, 'gray')
            plt.title(f"{nome} - {titulos[step_idx+5]}")
            plt.xticks([]), plt.yticks([])
    
    plt.tight_layout()
    plt.savefig('relatorio_etapas_parte2.png')
    plt.show()

# Processando as imagens com parâmetros específicos para cada uma
print("Iniciando processamento das imagens...")

# Lista para armazenar os resultados
resultados = []
titulos = [
    'Original RGB', 'Blur', 'Escala de Cinza', 'Limiarização',
    'Dilatação', 'Erosão', 'Abertura', 'Fechamento', 'Bordas Canny', 'Contornos'
]

try:
    # Processando a imagem da girafa
    final_girafa, intermediarias_girafa, _ = processar_imagem('GIRAFA.jpeg', 'Girafa', ajuste_threshold=30, tamanho_kernel=7)
    resultados.append(('Girafa', final_girafa, intermediarias_girafa))
    
    # Processando a imagem do avião
    final_aviao, intermediarias_aviao, _ = processar_imagem('AVIAO.jpeg', 'Avião', ajuste_threshold=40, tamanho_kernel=5)
    resultados.append(('Avião', final_aviao, intermediarias_aviao))
    
    # Processando a imagem do satélite
    final_satelite, intermediarias_satelite, _ = processar_imagem('SATELITE.jpeg', 'Satélite', ajuste_threshold=20, tamanho_kernel=9)
    resultados.append(('Satélite', final_satelite, intermediarias_satelite))
    
    # Criando o relatório final
    criar_relatorio_final(resultados)
    
    print("\nTodos os processamentos concluídos!")
    print("\nResumo das técnicas aplicadas:")
    print("1. Carregamento da imagem original")
    print("2. Conversão de BGR para RGB")
    print("3. Aplicação de blur para redução de ruído")
    print("4. Conversão para escala de cinza")
    print("5. Binarização da imagem através de limiarização (threshold)")
    print("6. Definição de kernel para operações morfológicas")
    print("7. Aplicação de operações morfológicas (dilatação, erosão, abertura, fechamento)")
    print("8. Detecção de bordas com algoritmo Canny")
    print("9. Identificação de contornos na imagem")
    print("10. Ordenação dos contornos por área")
    print("11. Desenho dos contornos na imagem original")
    print("\nArquivos gerados:")
    print("- GIRAFA_intermediarias.png: Etapas do processamento da imagem da girafa")
    print("- GIRAFA_final.png: Resultado final da imagem da girafa")
    print("- AVIAO_intermediarias.png: Etapas do processamento da imagem do avião")
    print("- AVIAO_final.png: Resultado final da imagem do avião")
    print("- SATELITE_intermediarias.png: Etapas do processamento da imagem do satélite")
    print("- SATELITE_final.png: Resultado final da imagem do satélite")
    print("- resultados_finais.png: Comparação dos resultados finais das três imagens")
    print("- relatorio_etapas_parte1.png e relatorio_etapas_parte2.png: Relatório detalhado de todas as etapas")
    print("\nLink para o código fonte: https://github.com/seu-usuario/visao-computacional-processamento")

except Exception as e:
    print(f"Erro durante o processamento: {e}")