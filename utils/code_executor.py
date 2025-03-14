import io
import sys
import streamlit as st

def initialize_global_env():
    """
    Inicializa o ambiente global para execução de código
    """
    if "global_env" not in st.session_state:
        st.session_state.global_env = {}
    return st.session_state.global_env

def run_code(code, global_env=None):
    """
    Executa um bloco de código e captura a saída
    
    Args:
        code (str): Código Python para executar
        global_env (dict, opcional): Ambiente global para execução
        
    Returns:
        str: Saída da execução do código
    """
    if global_env is None:
        global_env = initialize_global_env()
        
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