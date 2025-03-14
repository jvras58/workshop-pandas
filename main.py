import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import sys
from streamlit_ace import st_ace

st.set_page_config(page_title="Projeto Interativo: Titanic com Pandas", layout="wide")

# Título e introdução
st.title("Projeto Interativo: Explorando o Titanic com Python, Pandas e NumPy")
st.write("""
Bem-vindo ao workshop interativo! Neste projeto, você aprenderá a manipular e visualizar dados do dataset Titanic.
O conteúdo está dividido em três seções:
- **Tutorial**
- **Desafios**
- **Visualizações**
""")

# Carregar o dataset para uso geral
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    return df

df_titanic = load_data()

# Cria um ambiente global compartilhado para execução dos códigos
if "global_env" not in st.session_state:
    st.session_state.global_env = {}
global_env = st.session_state.global_env

# Função para executar código e capturar a saída
def run_code(code):
    buffer = io.StringIO()
    stdout_original = sys.stdout
    sys.stdout = buffer
    try:
        exec(code, global_env)
    except Exception as e:
        st.error(f"Erro ao executar o código: {e}")
    finally:
        sys.stdout = stdout_original
    return buffer.getvalue()

# Cria abas para organizar o conteúdo
tabs = st.tabs(["Tutorial", "Desafios", "Visualizações"])

# --- Aba 1: Tutorial ---
with tabs[0]:
    st.header("Tutorial Interativo")
    st.write("""
    Nesta seção, você aprenderá os principais conceitos e operações com Pandas usando o dataset Titanic:
    - **Seleção de Colunas**
    - **Filtragem de Dados**
    - **Limpeza, Agrupamento, Merge e Concatenação**
    - **Ordenação**
    """)

    st.subheader("Exemplo: Seleção, Filtragem e Limpeza")
    code_tutorial_1 = '''
# Carregar o dataset Titanic
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Seleção de colunas relevantes
df = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

# Filtragem: passageiros com mais de 10 anos
df_filtered = df[df['Age'] > 10]

# Limpeza: removendo linhas com valores nulos em 'Age' e 'Embarked'
df_cleaned = df_filtered.dropna(subset=['Age', 'Embarked'])

print("Dataset Titanic após seleção, filtragem e limpeza:")
print(df_cleaned.head())
    '''
    st.code(code_tutorial_1, language='python')

    st.subheader("Exemplo: Agrupamento e Operações")
    code_tutorial_2 = '''
# Agrupamento por classe e cálculo da média da tarifa
fare_mean = df_cleaned.groupby('Pclass')['Fare'].mean()
print("Média da tarifa por classe:")
print(fare_mean)

# Soma do número de passageiros por porto de embarque
embarked_sum = df_cleaned.groupby('Embarked')['PassengerId'].count()
print("Total de passageiros por porto de embarque:")
print(embarked_sum)
    '''
    st.code(code_tutorial_2, language='python')

    st.subheader("Exemplo: Merge e Concatenação")
    code_tutorial_3 = '''
# Criando um novo DataFrame fictício para merge
df_extra = pd.DataFrame({
    'PassengerId': [1, 2, 3],
    'ExtraInfo': ['VIP', 'Regular', 'VIP']
})
print("DataFrame df_extra criado:")
print(df_extra)

# Merge do dataset Titanic com informações adicionais
df_merged = pd.merge(df_cleaned, df_extra, on='PassengerId', how='left')
print("Dataset Titanic com informações adicionais:")
print(df_merged.head())

# Criando um DataFrame fictício para concatenar
df_new = pd.DataFrame({
    'PassengerId': [1000, 1001],
    'Survived': [1, 0],
    'Pclass': [1, 3],
    'Name': ['Fake Passenger 1', 'Fake Passenger 2'],
    'Sex': ['male', 'female'],
    'Age': [30, 25],
    'SibSp': [0, 1],
    'Parch': [0, 0],
    'Fare': [100, 50],
    'Embarked': ['S', 'C']
})
print("DataFrame df_new criado:")
print(df_new)

# Concatenando os DataFrames e adicionando uma nova linha
df_concatenated = pd.concat([df_cleaned, df_new], ignore_index=True)
df_concatenated = pd.concat([df_concatenated, pd.DataFrame([{
    'PassengerId': 1002,
    'Survived': 0,
    'Pclass': 2,
    'Name': 'Added Passenger',
    'Sex': 'male',
    'Age': 40,
    'SibSp': 1,
    'Parch': 2,
    'Fare': 80,
    'Embarked': 'Q'
}])], ignore_index=True)
print("Dataset após concatenação e adição de nova linha:")
print(df_concatenated.head())
    '''
    st.code(code_tutorial_3, language='python')

    st.subheader("Exemplo: Ordenação e Exibição Final")
    code_tutorial_4 = '''
# Ordenando o DataFrame pelo valor da tarifa de forma decrescente
df_sorted = df_concatenated.sort_values(by='Fare', ascending=False)
df_final = df_sorted.drop(columns=['ExtraInfo'], errors='ignore')
print("Dataset após ordenação e remoção de coluna 'ExtraInfo':")
print(df_final.head())

print("Dataset final após todas as operações:")
print(df_final.head())
    '''
    st.code(code_tutorial_4, language='python')

# --- Aba 2: Desafios ---
with tabs[1]:
    st.header("Desafios Interativos")
    st.write("Nesta seção, você poderá executar blocos de código pré-definidos e, em seguida, resolver um desafio prático.")

    st.subheader("Execução dos Blocos de Código")
    # Dicionário com cada bloco de código (cada questão)
    steps = {
        "1. Pacotes / Bibliotecas": '''import pandas as pd
import numpy as np
print("Bibliotecas importadas!")''',

        "2. Carregar o dataset Titanic": '''df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print("Dataset Titanic carregado! Shape:", df.shape)''',

        "3. Seleção de colunas relevantes": '''df = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
print("Colunas selecionadas:", df.columns.tolist())
print(df.head())''',

        "4. Filtragem: passageiros com mais de 10 anos": '''df_filtered = df[df['Age'] > 10]
print("Filtragem concluída! Exibindo primeiras linhas:")
print(df_filtered.head())''',

        "5. Limpeza: remover nulos em Age e Embarked": '''df_cleaned = df_filtered.dropna(subset=['Age', 'Embarked'])
print("Dataset após limpeza (nulos removidos):")
print(df_cleaned.head())''',

        "6. Agrupamento: média da tarifa por classe": '''fare_mean = df_cleaned.groupby('Pclass')['Fare'].mean()
print("Média da tarifa por classe:")
print(fare_mean)''',

        "7. Soma de passageiros por porto de embarque": '''embarked_sum = df_cleaned.groupby('Embarked')['PassengerId'].count()
print("Total de passageiros por porto de embarque:")
print(embarked_sum)''',

        "8. Criar DataFrame para merge": '''df_extra = pd.DataFrame({
    'PassengerId': [1, 2, 3],
    'ExtraInfo': ['VIP', 'Regular', 'VIP']
})
print("DataFrame df_extra criado:")
print(df_extra)''',

        "9. Merge com informações adicionais": '''df_merged = pd.merge(df_cleaned, df_extra, on='PassengerId', how='left')
print("Dataset Titanic com informações adicionais:")
print(df_merged.head())''',

        "10. Criar DataFrame para concatenar": '''df_new = pd.DataFrame({
    'PassengerId': [1000, 1001],
    'Survived': [1, 0],
    'Pclass': [1, 3],
    'Name': ['Fake Passenger 1', 'Fake Passenger 2'],
    'Sex': ['male', 'female'],
    'Age': [30, 25],
    'SibSp': [0, 1],
    'Parch': [0, 0],
    'Fare': [100, 50],
    'Embarked': ['S', 'C']
})
print("DataFrame df_new criado:")
print(df_new)''',

        "11. Concatenar DataFrames e adicionar nova linha": '''df_concatenated = pd.concat([df_cleaned, df_new], ignore_index=True)
df_concatenated = pd.concat([df_concatenated, pd.DataFrame([{
    'PassengerId': 1002,
    'Survived': 0,
    'Pclass': 2,
    'Name': 'Added Passenger',
    'Sex': 'male',
    'Age': 40,
    'SibSp': 1,
    'Parch': 2,
    'Fare': 80,
    'Embarked': 'Q'
}])], ignore_index=True)
print("Dataset após concatenação e adição de nova linha:")
print(df_concatenated.head())''',

        "12. Ordenar e remover coluna ExtraInfo": '''df_sorted = df_concatenated.sort_values(by='Fare', ascending=False)
df_final = df_sorted.drop(columns=['ExtraInfo'], errors='ignore')
print("Dataset após ordenação e remoção de coluna 'ExtraInfo':")
print(df_final.head())''',

        "13. Exibir dataset final": '''print("Dataset final após todas as operações:")
print(df_final.head())'''
    }

    selected_step = st.selectbox("Selecione o bloco de código para executar", list(steps.keys()), key="desafio_select")
    st.markdown(f"#### Bloco: {selected_step}")
    code_block = st_ace(
        value=steps[selected_step],
        language='python',
        theme='monokai',
        key=f"ace_editor_{selected_step}",
        height=300
    )

    if st.button("Executar Bloco", key="executar_bloco"):
        with st.spinner("Executando o código..."):
            result = run_code(code_block)
        st.markdown("### Saída do Código")
        with st.expander("Clique para visualizar a saída"):
            st.code(result, language='python')

    st.markdown("---")
    st.subheader("Desafio Final")
    st.write("""
    **Desafio:**  
    Utilizando o dataset limpo (variável `df_cleaned`) criado pelos blocos anteriores, escreva um código que calcule e exiba a média da tarifa (coluna **Fare**) dos passageiros da **classe 2**.
    """)

    challenge_code = st_ace(
        value='''# Utilize o dataset df_cleaned previamente criado
media_classe2 = df_cleaned[df_cleaned['Pclass'] == 2]['Fare'].mean()
print("Média da tarifa para passageiros da classe 2:", media_classe2)
''',
        language='python',
        theme='monokai',
        key="ace_editor_challenge",
        height=200
    )

    if st.button("Executar Desafio", key="executar_desafio"):
        with st.spinner("Executando o desafio..."):
            result_desafio = run_code(challenge_code)
        st.markdown("### Saída do Desafio")
        with st.expander("Clique para visualizar a saída"):
            st.code(result_desafio, language='python')

# --- Aba 3: Visualizações ---
with tabs[2]:
    st.header("Visualizações dos Dados")
    st.write("Explore os dados do Titanic através de gráficos interativos.")

    st.subheader("Gráfico 1: Média da Tarifa por Classe")
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    df = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    df_filtered = df[df['Age'] > 10]
    df_cleaned = df_filtered.dropna(subset=['Age', 'Embarked'])
    fare_mean = df_cleaned.groupby('Pclass')['Fare'].mean()
    st.write("Média da tarifa por classe:")
    st.write(fare_mean)
    fig, ax = plt.subplots()
    ax.bar(fare_mean.index.astype(str), fare_mean.values)
    ax.set_xlabel("Classe")
    ax.set_ylabel("Média da Tarifa")
    ax.set_title("Média da Tarifa por Classe")
    st.pyplot(fig)

    st.subheader("Gráfico 2: Distribuição de Idades")
    fig2, ax2 = plt.subplots()
    ax2.hist(df_cleaned["Age"], bins=20)
    ax2.set_xlabel("Idade")
    ax2.set_ylabel("Frequência")
    ax2.set_title("Distribuição de Idades")
    st.pyplot(fig2)
