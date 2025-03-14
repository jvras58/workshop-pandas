import streamlit as st
from streamlit_ace import st_ace
from utils.code_executor import run_code, initialize_global_env

def get_code_steps():
    """
    Retorna os blocos de código para os desafios
    """
    return {
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

def render_challenge_page():
    """
    Renderiza a página de desafios interativos
    """
    global_env = initialize_global_env()
    
    st.header("Desafios Interativos")
    st.write("Nesta seção, você poderá executar blocos de código pré-definidos e, em seguida, resolver um desafio prático.")

    st.subheader("Execução dos Blocos de Código")
    # Blocos de código para cada etapa do desafio
    steps = get_code_steps()
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
            result = run_code(code_block, global_env)
        st.markdown("### Saída do Código")
        with st.expander("Clique para visualizar a saída"):
            st.code(result, language='python')


    # Seção aberta
    st.markdown("---")
    st.subheader("Código Livre")
    st.write("""
    **Experimente seus próprios comandos:**  
    Escreva qualquer código Python usando as variáveis criadas anteriormente.
    Todas as variáveis definidas nos blocos executados estão disponíveis neste ambiente.
    """)
    free_code = st_ace(
        value='''# Exemplo: visualizar informações do dataset
if 'df_cleaned' in globals():
    print("Informações do dataset:")
    print(df_cleaned.describe())
else:
    print("Execute os blocos anteriores para criar o dataset primeiro")

# Exemplo: Com o uso do NumPy e Pandas
import numpy as np
import pandas as pd


# Exemplo: Crie um exemplo simples usando o numpy mas usando o dataframe anterior
fare_array = df_cleaned['Fare'].values
fare_mean = np.mean(fare_array)
print("Média da tarifa:", fare_mean)

# Exemplo: crie uma nova coluna com a soma de SibSp e Parch
df_cleaned['FamilySize'] = df_cleaned['SibSp'] + df_cleaned['Parch']
print("Dataset com nova coluna 'FamilySize':")
print(df_cleaned.head())

''',
        language='python',
        theme='monokai',
        key="ace_editor_free",
        height=250
    )

    if st.button("Executar Código", key="executar_livre"):
        with st.spinner("Executando seu código..."):
            result_livre = run_code(free_code, global_env)
        st.markdown("### Saída do Código")
        with st.expander("Clique para visualizar a saída"):
            st.code(result_livre, language='python')


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
            result_desafio = run_code(challenge_code, global_env)
        st.markdown("### Saída do Desafio")
        with st.expander("Clique para visualizar a saída"):
            st.code(result_desafio, language='python')
