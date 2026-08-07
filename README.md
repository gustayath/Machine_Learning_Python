🏅 Análise Exploratória de Dados: Jogos Olímpicos (Olympic Games Analysis)Este repositório contém estudos práticos e análises exploratórias de dados (EDA) utilizando o dataset histórico de eventos e atletas dos Jogos Olímpicos (athlete_events.csv). O objetivo principal é extrair insights sobre o perfil físico dos atletas, distribuição demográfica e desempenho por comitês olímpicos.  📌 Conteúdo do RepositórioManipulação de DataFrames: Carregamento e inspeção inicial dos dados (head(), loc, ordenação).  Filtros Avançados: Consultas específicas por medalhas, modalidades, comitês nacionais (ex: Brasil/BRA) e edições dos jogos.  Visualização de Dados: Gráficos estatísticos como Boxplots e Histogramas para análise de distribuições e identificação de outliers.  🛠️ Tecnologias UtilizadasPython 3.xPandas: Para manipulação e tratamento dos dados.  Matplotlib / Seaborn: Para geração das visualizações estatísticas.  📊 Visualizações e Análises ESTATÍSTICAS1. Análise de Distribuição por Idade (Age)O boxplot e o histograma a seguir ilustram a amplitude e o comportamento da idade dos atletas ao longo da história dos Jogos Olímpicos:  Insight: A idade média dos atletas concentra-se na faixa dos 20 aos 30 anos (com mediana em torno de 25 anos), apresentando outliers em esportes específicos (como equitação ou tiro) com atletas acima de 50 anos.  2. Análise de Distribuição por Altura (Height)Distribuição de altura dos atletas participantes:Insight: A altura segue uma distribuição simétrica (normal), com média ao redor de 175 cm.🔍 Exemplos de CódigoCarregamento e Inspeção dos DadosPythonimport pandas as pd

# Carregando o conjunto de dados
df = pd.read_csv('Dados/athlete_events.csv')

# Exibindo as 5 primeiras linhas
df.head()
```[cite: 1, 2]

### Filtro de Atletas Brasileiros Campeões Olímpicos
Exemplo de filtro para identificar medalhistas de ouro do Brasil no Judô a partir de 2016 (ex: Rafaela Silva)[cite: 1]:

```python
# Consulta específica por Ouro, Brasil (BRA), a partir de 2016 e modalidade Judô
ouro_judo_bra = df.loc[
    (df['Medal'] == 'Gold') & 
    (df['NOC'] == 'BRA') & 
    (df['Year'] >= 2016) & 
    (df['Sport'] == 'Judo')
].sort_values('Age')

print(ouro_judo_bra)
```[cite: 1]

### Geração de Boxplot
```python
import matplotlib.pyplot as plt

# Criando boxplot da coluna 'Age'
df.boxplot(column='Age')
plt.title('Distribuição da Idade dos Atletas')
plt.show()
```[cite: 2]

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
Instale as dependências:Bashpip install pandas matplotlib seaborn
Inicie o Jupyter Notebook:Bashjupyter notebook
📝 LicençaEste projeto é destinado para fins de estudo e aprendizado prático em Ciência de Dados e Machine Learning.
