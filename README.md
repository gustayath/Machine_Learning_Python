🏅 Análise Exploratória de Dados: Jogos Olímpicos (Olympic Games Analysis)
Este repositório contém estudos práticos e análises exploratórias de dados (EDA) utilizando o dataset histórico de eventos e atletas dos Jogos Olímpicos (athlete_events.csv). O objetivo principal é extrair insights sobre o perfil físico dos atletas, distribuição demográfica e desempenho por comitês olímpicos.

📌 Conteúdo do Repositório: 
- Manipulação de DataFrames: Carregamento e inspeção inicial dos dados.
- Filtros Avançados: Consultas específicas por medalhas, modalidades, comitês nacionais (ex: Brasil/BRA) e edições dos jogos.
- Visualização de Dados: Gráficos estatísticos como Boxplots e Histogramas para análise de distribuições e identificação de outliers.

🛠️ Tecnologias Utilizadas:
- Python 3.14
- Pandas: Para manipulação e tratamento dos dados.
- Matplotlib / Seaborn: Para geração das visualizações estatísticas.

📊 Visualizações e Análises ESTATÍSTICAS
1. Análise de Distribuição por Idade (Age): O boxplot e o histograma a seguir ilustram a amplitude e o comportamento da idade dos atletas ao longo da história dos Jogos Olímpicos:
- Insight: A idade média dos atletas concentra-se na faixa dos 20 aos 30 anos (com mediana em torno de 25 anos), apresentando outliers em esportes específicos (como equitação ou tiro) com atletas acima de 50 anos.
![image_alt](https://github.com/gustayath/Machine_Learning_Python/blob/f7380daa791f0116d0d7c54da9ce2c430ec752f5/boxPlot_idade.png)
![image_alt](https://github.com/gustayath/Machine_Learning_Python/blob/ae0337e51b8de5ec46675d1c44e0ccb734edf8a6/hist_idade.png)

2. Análise de Distribuição por Altura (Height)
Distribuição de altura dos atletas participantes:
- Insight: A altura segue uma distribuição simétrica (normal), com média ao redor de 175 cm.
![image_alt](https://github.com/gustayath/Machine_Learning_Python/blob/f6eff4516f9d2868f81937ec07d1b307408ab05c/boxPlot_altura.png)
![image_alt](https://github.com/gustayath/Machine_Learning_Python/blob/3e151e6874a9fb0c4ea538f1849ad1f0db4936be/hist_altura.png)

## 🔍 Exemplos de Código

### Carregando o conjunto de dados

```python
import pandas as pd

# Carregando o conjunto de dados
df = pd.read_csv("Dados/athlete_events.csv")

# Exibindo as 5 primeiras linhas
df.head()
```

### 🥇 Filtro de Atletas Brasileiros Campeões Olímpicos

Exemplo de filtro para identificar medalhistas de ouro do Brasil na modalidade **Judô**, a partir de **2016**.

```python
# Consulta específica por Ouro, Brasil (BRA), a partir de 2016 e modalidade Judô
ouro_judo_bra = df.loc[
    (df["Medal"] == "Gold") &
    (df["NOC"] == "BRA") &
    (df["Year"] >= 2016) &
    (df["Sport"] == "Judo")
].sort_values("Age")

print(ouro_judo_bra)
```

### 📈 Geração de Boxplot

```python
import matplotlib.pyplot as plt

# Criando boxplot da coluna 'Age'
df.boxplot(column="Age", figsize=(8, 5))
plt.title("Distribuição da Idade dos Atletas")
plt.ylabel("Idade")
plt.show()
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/gustayath/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install pandas matplotlib seaborn
```

### 3. Inicie o Jupyter Notebook

```bash
jupyter notebook
```

---

## 📦 Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 👨‍💻 Autor

**Gustavo Yath**

- GitHub: https://github.com/gustayath
- LinkedIn: https://www.linkedin.com/in/gustavoyath/

---

## 📝 Licença

Este projeto foi desenvolvido para fins de **estudo, aprendizado prático em Ciência de Dados e Machine Learning**, podendo ser utilizado como referência para fins educacionais.
