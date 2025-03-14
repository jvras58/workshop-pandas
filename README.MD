<div align="center">
  <img src="https://pandas.pydata.org/static/img/pandas_mark.svg" alt="Pandas Logo" height="120px"/>
</div>
<h2 align="center">Workshop Interativo: Explorando o Titanic com Python, Pandas e NumPy</h2>

## 📖 Sobre o Projeto

Este projeto é uma aplicação interativa desenvolvida para o workshop e treinamentos de análise de dados com Python. Utilizando o famoso dataset do Titanic, os participantes podem aprender, praticar e visualizar conceitos essenciais de manipulação de dados com Pandas e NumPy através de uma interface amigável construída com Streamlit.

O workshop permite que os usuários:
- Aprendam conceitos fundamentais de manipulação de dados através de tutoriais guiados
- Pratiquem suas habilidades em desafios interativos com execução de código em tempo real
- Visualizem os resultados da análise através de gráficos informativos

## 🚀 Tecnologias e Ferramentas

A aplicação foi desenvolvida em Python e utiliza diversas bibliotecas modernas para análise de dados e interatividade:

## Stack do Projeto

Este é um projeto educacional interativo que combina análise de dados e interface web para criar uma experiência de aprendizado hands-on.

| Lib/Ferramenta | Versão |
|----------------|--------|
| **Runtime**    |        |
| Python         | v3.12+ |
| Pandas         | v2.2.3+|
| NumPy          | v2.2.3+|
| Matplotlib     | v3.10.1+|
| Streamlit      | v1.43.2+|
| Streamlit-Ace  | v0.1.1+|
| **Devtime**    |        |
| VSCode         | Latest |

### Organização do projeto
```
/
├─📁 .vscode            ->  Definições de ambiente para o VSCode
├─📁 config             ->  Configurações globais da aplicação
│   └─🐍 settings.py    ->  Constantes e configurações
├─📁 data               ->  Módulos para carregamento de dados
│   └─🐍 loader.py      ->  Funções para carregar e processar o dataset
├─📁 ui                 ->  Interface de usuário com Streamlit
│   ├─🐍 challenge_page.py    ->  Página de desafios interativos
│   ├─🐍 tutorial_page.py     ->  Página de tutoriais
│   └─🐍 visualization_page.py->  Página de visualizações
├─📁 utils              ->  Utilitários diversos
│   └─🐍 code_executor.py     ->  Executor de código Python
├─📄 .gitignore
├─📄 .python-version    ->  Versão Python utilizada
├─📄 app.py             ->  Ponto de entrada principal da aplicação
├─📄 pyproject.toml     ->  Configuração do projeto e dependências
└─📄 README.md          ->  Este arquivo
```

## 💻 Como Executar

### Pré-requisitos
- Python 3.12 ou superior
- pip ou uv para instalação de pacotes

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/workshop-pandas.git
cd workshop-pandas
```

2. Instale as dependências:
```bash
# Usando pip
pip install -e .

# OU usando uv
uv sync
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

## 🔍 Funcionalidades

### Tutorial Interativo
Aprenda os fundamentos do Pandas com exemplos práticos usando o dataset do Titanic, incluindo:
- Seleção de colunas
- Filtragem de dados
- Limpeza de dados
- Agrupamento e operações estatísticas
- Merge e concatenação de DataFrames

### Desafios Interativos
Aplique o conhecimento adquirido através de desafios práticos com um editor de código integrado e feedback em tempo real.

### Visualizações
Explore os dados através de gráficos interativos que revelam padrões e insights do dataset do Titanic.


<p align="center">
  Desenvolvido com ❤️ para entusiastas de análise de dados
</p>
