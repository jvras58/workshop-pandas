import streamlit as st
from config.settings import PAGE_TITLE, PAGE_LAYOUT
from ui.tutorial_page import render_tutorial_page
from ui.challenge_page import render_challenge_page
from ui.visualization_page import render_visualization_page

def main():
    """
    Função principal que configura e executa o aplicativo Streamlit
    """
    st.set_page_config(page_title=PAGE_TITLE, layout=PAGE_LAYOUT)

    st.title("Projeto Interativo: Explorando o Titanic com Python, Pandas e NumPy")
    st.write("""
    Bem-vindo ao workshop interativo! Neste projeto, você aprenderá a manipular e visualizar dados do dataset Titanic.
    O conteúdo está dividido em três seções:
    - **Tutorial**
    - **Desafios**
    - **Visualizações**
    """)

    tabs = st.tabs(["Tutorial", "Desafios", "Visualizações"])

    with tabs[0]:
        render_tutorial_page()
    with tabs[1]:
        render_challenge_page()
    with tabs[2]:
        render_visualization_page()

if __name__ == "__main__":
    main()