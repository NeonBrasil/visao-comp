# Processamento de Imagens - Visão Computacional

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

Para cada imagem processada, são gerados os seguintes arquivos:

- `[NOME]_intermediarias.png`: Mostra todas as etapas intermediárias do processamento
- `[NOME]_final.png`: Mostra o resultado final em tamanho grande

Além disso, são gerados arquivos de relatório que comparam os resultados:

- `resultados_finais.png`: Comparação dos resultados finais das três imagens
- `relatorio_etapas_parte1.png` e `relatorio_etapas_parte2.png`: Relatório detalhado de todas as etapas
