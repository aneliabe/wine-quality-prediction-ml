# Classificação da Qualidade de Vinhos com Machine Learning

## Visão Geral do Projeto

Este projeto explora as propriedades físico-químicas do vinho e utiliza algoritmos de classificação de Machine Learning para prever sua qualidade.

A análise tem como foco identificar padrões no conjunto de dados, compreender como diferentes características químicas se relacionam com a qualidade do vinho e avaliar o desempenho de modelos de classificação.

## Objetivos

- Explorar e compreender o conjunto de dados por meio da Análise Exploratória de Dados (EDA).
- Identificar padrões e possíveis outliers nos dados.
- Preparar o conjunto de dados para o treinamento dos modelos de Machine Learning.
- Treinar e comparar diferentes modelos de classificação.
- Avaliar o desempenho dos modelos utilizando métricas de classificação adequadas.
- Interpretar a importância das variáveis para compreender sua contribuição nas previsões dos modelos.

## Conjunto de Dados

O conjunto de dados utilizado neste projeto é o Wine Quality (`WineQT.csv`).

Ele contém medidas físico-químicas de amostras de vinho, incluindo:

- Acidez fixa (Fixed acidity)
- Acidez volátil (Volatile acidity)
- Ácido cítrico (Citric acid)
- Açúcar residual (Residual sugar)
- Cloretos (Chlorides)
- Dióxido de enxofre livre (Free sulfur dioxide)
- Dióxido de enxofre total (Total sulfur dioxide)
- Densidade (Density)
- pH
- Sulfatos (Sulphates)
- Álcool (Alcohol)

A pontuação original de qualidade é utilizada para criar uma variável-alvo de classificação binária.

## Análise Exploratória de Dados (EDA)

A análise exploratória inclui:

- Análise da estrutura do conjunto de dados e estatísticas descritivas.
- Distribuição das pontuações de qualidade dos vinhos.
- Análise das propriedades físico-químicas.
- Identificação de possíveis outliers pelo método do Intervalo Interquartil (IQR).
- Análise das relações entre as variáveis e a qualidade do vinho.

## Machine Learning

São treinados e comparados modelos de classificação para identificar a abordagem mais adequada para prever a qualidade do vinho.

A avaliação dos modelos considera métricas de classificação como:

- Acurácia (Accuracy)
- Precisão (Precision)
- Revocação (Recall)
- F1-score
- Matriz de confusão (Confusion Matrix)

## Interpretação dos Modelos

A técnica Permutation Importance é utilizada para avaliar a importância das variáveis, medindo o impacto de cada uma no desempenho do modelo.

## Tecnologias e Bibliotecas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

## Estrutura do Projeto

```text
wine-quality-prediction-ml/
│
├── data/
├── notebooks/
├── presentation/
├── results/
├── src/
│
├── requirements.txt
└── README.md
```

## Como Executar o Projeto

Clone este repositório:

```bash
git clone https://github.com/aneliabe/wine-quality-prediction-ml
```

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

Abra o Jupyter Notebook e execute as células para reproduzir a análise.

## Informações do Projeto

Este projeto foi desenvolvido como parte da especialização em Data Analytics da FIAP.
