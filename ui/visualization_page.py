import streamlit as st
import matplotlib.pyplot as plt
from data.loader import get_processed_data

def render_visualization_page():
    """
    Renderiza a página de visualizações
    """
    st.header("Visualizações dos Dados")
    st.write("Explore os dados do Titanic através de gráficos interativos.")

    # Carrega dados processados
    df_cleaned = get_processed_data()

    st.subheader("Gráfico 1: Média da Tarifa por Classe")
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