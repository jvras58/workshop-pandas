import streamlit as st

def render_tutorial_page():
    """
    Renderiza a página de tutoriais interativos
    """
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