# Processamento de Imagens - Visão Computacional

## Membros
* Cayque Cicarelli - 22.221.005-6

* Bruna Paz - 22.121.020-6

* Matheus Miranda - 22.22.0017-2

Este projeto contém scripts para processamento de imagens utilizando técnicas de visão computacional. O objetivo é aplicar diferentes técnicas de processamento em três imagens: GIRAFA.jpeg, AVIAO.jpeg e SATELITE.jpeg.

## Requisitos

Para executar os scripts, você precisará das seguintes bibliotecas:

```
pip install opencv-python matplotlib numpy
```

## Arquivos do Projeto

- `processamento_completo.py`: Script principal que processa as três imagens e gera um relatório completo
- `processamento_girafa.py`: Script específico para processamento da imagem GIRAFA.jpeg
- `processamento_aviao_satelite.py`: Script para processamento das imagens AVIAO.jpeg e SATELITE.jpeg
- `GIRAFA.jpeg`, `AVIAO.jpeg`, `SATELITE.jpeg`: Imagens originais para processamento

## Como Executar

Para executar o processamento completo das três imagens e gerar o relatório:

```
python processamento_completo.py
```

Para processar apenas a imagem da girafa:

```
python processamento_girafa.py
```

Para processar as imagens do avião e do satélite:

```
python processamento_aviao_satelite.py
```

## Etapas do Processamento

O processamento de cada imagem segue as seguintes etapas:

1. **Carregamento da imagem original**
2. **Conversão de BGR para RGB** - OpenCV carrega imagens no formato BGR
3. **Aplicação de blur** - Redução de ruído na imagem
4. **Conversão para escala de cinza** - Simplificação da imagem para processamento
5. **Binarização** - Aplicação de threshold para criar uma imagem binária
6. **Operações morfológicas**:
   - Dilatação - Expande as regiões brancas
   - Erosão - Contrai as regiões brancas
   - Abertura - Erosão seguida de dilatação
   - Fechamento - Dilatação seguida de erosão
7. **Detecção de bordas** - Aplicação do algoritmo Canny
8. **Identificação de contornos** - Encontrar contornos na imagem
9. **Desenho dos contornos** - Destacar os contornos na imagem original

## Resultados


![image](https://github.com/user-attachments/assets/f4752ef8-a699-47ce-b139-c9192c148af3)

![image](https://github.com/user-attachments/assets/a017a871-c315-4ff9-a4a2-ecd8352e4152)

![image](https://github.com/user-attachments/assets/7e7eb76c-03f2-45cb-bee4-ef250b012422)

![image](https://github.com/user-attachments/assets/da2d2c2a-f04d-4012-b3ef-92ecefbcb64f)

![image](https://github.com/user-attachments/assets/3c4afb98-5e1d-4b39-9acd-d53bddf5654a)

![image](https://github.com/user-attachments/assets/39a2caa8-3eba-4b41-a8a5-3eff2cf3d559)


![image](https://github.com/user-attachments/assets/bc79d5f5-d8a2-4eed-90f3-8d892ebaf099)


![image](https://github.com/user-attachments/assets/0cc3145a-9110-4b8c-b00e-eed817f0db97)


![image](https://github.com/user-attachments/assets/6b1c7175-6035-43fc-baac-73ea79228d45)
