import pandas as pd
import streamlit as st
from config.settings import TITANIC_DATASET_URL, TITANIC_COLUMNS

@st.cache_data
def load_titanic_data():
    """
    Carrega o dataset Titanic da URL e retorna como DataFrame
    """
    df = pd.read_csv(TITANIC_DATASET_URL)
    return df

def get_processed_data():
    """
    Carrega e processa dados para visualização
    """
    df = load_titanic_data()
    df = df[TITANIC_COLUMNS]
    df_filtered = df[df['Age'] > 10]
    df_cleaned = df_filtered.dropna(subset=['Age', 'Embarked'])
    return df_cleaned