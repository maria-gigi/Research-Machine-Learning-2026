# Identificação de Sujeitos e Atividades por meio de EEG utilizando Inteligência Artificial

## 📖 Sobre o Projeto

Este projeto tem como objetivo desenvolver um modelo de Inteligência Artificial capaz de identificar indivíduos a partir de sinais de eletroencefalografia (EEG) obtidos durante a realização de diferentes atividades.
Os sinais de EEG utilizados neste projeto passaram inicialmente por um processo de remoção de artefatos utilizando a técnica **MoSYN**, executada no **MATLAB**. Posteriormente, os dados foram submetidos a etapas adicionais de pré-processamento, organização das características e treinamento de modelos de Inteligência Artificial em Python.

O objetivo final é construir um sistema composto por duas etapas:

1. **Identificar qual atividade está sendo realizada** a partir dos sinais de EEG;
2. **Identificar o sujeito** utilizando as características do EEG juntamente com a atividade reconhecida.

O projeto ainda está em desenvolvimento, sendo continuamente aprimorado com novas técnicas de processamento de sinais, extração de características e modelos de aprendizado de máquina.

---

## 🎯 Objetivos

- Realizar o pré-processamento de sinais de EEG.
- Remover artefatos e canais desnecessários.
- Extrair características baseadas em conectividade cerebral (REA) e métricas de Hubs.
- Construir uma base de dados estruturada para treinamento.
- Desenvolver modelos de Inteligência Artificial para classificação de atividades.
- Expandir o modelo para identificação simultânea do sujeito e da atividade realizada.

---

# Fluxo do Projeto

## 1️⃣ Remoção de Artefatos

A primeira etapa consiste no pré-processamento dos sinais de EEG.

Nessa etapa são realizados:

- Leitura dos arquivos no formato `.edf`;
- Remoção de canais não utilizados e canais de ruído;
- Filtragem passa-faixa entre **0,5 Hz e 48 Hz**;
- Divisão do sinal em épocas de **1,28 segundos**;
- Remoção automática de épocas contaminadas por artefatos utilizando limiar de amplitude;
- Seleção das épocas válidas para análise.

### Bibliotecas utilizadas

- MNE-Python
- NumPy
- Pandas

---

## 2️⃣ Tratamento dos Dados

Após o pré-processamento, os arquivos contendo as métricas de conectividade (iREA) e Hubs são organizados em uma única tabela utilizada pelo modelo de IA.

Nesta etapa:

- Os arquivos são carregados automaticamente;
- Eletrodos indesejados são removidos;
- As informações são reorganizadas em formato tabular;
- Cada linha representa um sujeito realizando determinada atividade;
- As métricas REA e Hubs são unificadas em um único conjunto de atributos.

Ao final é gerada uma tabela contendo:

- Identificação do sujeito;
- Atividade realizada;
- Métricas REA;
- Métricas de Hubs.

---

## 3️⃣ Treinamento da Rede Neural

Atualmente o projeto utiliza uma **Rede Neural Perceptron Multicamadas (MLP)** implementada em **PyTorch**.

### Arquitetura

- Camada de entrada: **116 atributos**
- Primeira camada oculta: **32 neurônios**
- Segunda camada oculta: **16 neurônios**
- Camada de saída: **6 classes (atividades)**
- Função de ativação: **Tanh**
- Função de perda: **CrossEntropyLoss**
- Otimizador: **SGD com Momentum e Weight Decay**

### Configuração do treinamento

- 50 épocas
- Batch Size = 4
- Padronização dos dados (StandardScaler)
- Codificação das classes com LabelEncoder

Durante o treinamento são gerados:

- Histórico da Loss
- Histórico da Acurácia

---

# 📊 Resultados Atuais

Atualmente o modelo alcança aproximadamente **100% de acurácia sobre os dados de treinamento**.

Entretanto, esse resultado evidencia um **caso de overfitting**, já que a quantidade de dados disponíveis ainda é relativamente pequena.

Como o projeto ainda está em fase de desenvolvimento, esse comportamento era esperado nesta etapa inicial.

---

# 🚧 Limitações Atuais

O projeto ainda possui algumas limitações importantes:

- Quantidade reduzida de sujeitos;
- Base de dados ainda pequena;
- Avaliação realizada apenas sobre os dados de treinamento;
- Ainda não foram realizados testes com validação cruzada;
- A capacidade de generalização do modelo ainda está sendo investigada.

---

# 🔬 Trabalhos Futuros

As próximas etapas do projeto incluem:

- Ampliação da base de dados com novos sujeitos;
- Inclusão de novas atividades;
- Avaliação em conjuntos independentes de teste;
- Implementação de validação cruzada;
- Aplicação de técnicas de regularização;
- Comparação com outros modelos de Inteligência Artificial.

Espera-se que o aumento da quantidade de dados reduza significativamente o problema de overfitting.

Caso isso não ocorra, serão avaliadas outras arquiteturas de aprendizado profundo, como:

- Redes Neurais Convolucionais (CNN);
- Redes Neurais Recorrentes (RNN/LSTM);
- Graph Neural Networks (GNN);
- Modelos baseados em Transformers.

---

# 🛠 Tecnologias Utilizadas

- Python
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- MNE-Python
- Matplotlib
- Google Colab

---

# 📁 Estrutura Atual do Projeto

```
Projeto
│
├── Remocao_Artefatos.ipynb
├── Tratamento_Dados.ipynb
├── Treinamento.ipynb
├── Dados/
└── README.md
```

---

# 📌 Status do Projeto

🚧 **Em desenvolvimento**

O projeto encontra-se em constante evolução. Novas técnicas de pré-processamento, extração de características, ampliação da base de dados e novos modelos de Inteligência Artificial serão incorporados ao longo da pesquisa.

---

# 👨‍💻 Autoria

Projeto desenvolvido como parte de uma pesquisa científica na área de **Inteligência Artificial aplicada ao processamento de sinais de EEG**, com foco na identificação de atividades e sujeitos por meio de técnicas de aprendizado de máquina.
