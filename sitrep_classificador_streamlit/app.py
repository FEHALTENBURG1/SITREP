import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ------------------------------------------------------------
# Classificador de Risco — SITREP · SDS UnB
# Aplicação Streamlit para publicação de HTML interativo.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Classificador de Risco — SITREP · SDS UnB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove margens e elementos visuais padrão do Streamlit para
# deixar o HTML ocupar a área principal da página.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-right: 0rem;
            padding-left: 0rem;
            padding-bottom: 0rem;
            max-width: 100%;
        }
        iframe {
            border: 0;
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "SITREP_CLASS.html"

try:
    html_content = html_path.read_text(encoding="utf-8")
except FileNotFoundError:
    st.error("Arquivo SITREP_CLASS.html não encontrado. Verifique se ele está na mesma pasta do app.py.")
    st.stop()

components.html(
    html_content,
    height=3200,
    scrolling=True,
)
