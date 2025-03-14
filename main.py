import streamlit as st
import io
import sys
from streamlit_ace import st_ace

if "global_env" not in st.session_state:
    st.session_state.global_env = {}
global_env = st.session_state.global_env

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

# Menu lateral para selecionar o bloco de código
selected_step = st.sidebar.selectbox("Selecione o bloco de código para executar", list(steps.keys()))

st.header(f"Bloco: {selected_step}")

# Utiliza o streamlit-ace com key dinâmica para atualizar o editor conforme a seleção
code = st_ace(
    value=steps[selected_step],
    language='python',
    theme='monokai',
    key=f"ace_editor_{selected_step}",
    height=300
)

if st.button("Executar Bloco"):
    with st.spinner("Executando o código..."):
        result = run_code(code)
    st.markdown("### Saída do Código")
    with st.expander("Clique para visualizar a saída"):
        st.code(result, language='python')
