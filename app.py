import streamlit as st
from dotenv import load_dotenv
import os
from modules.search import perform_search
from modules.summarizer import generate_summary
from modules.wordcloud_generator import create_wordcloud

# Cargar variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Configuración de la página
st.set_page_config(page_title="Asistente de Investigación", layout="wide")
st.title("🔍 Asistente de Investigación")

# Entrada del usuario
query = st.text_input("Introduce un tema de investigación:", placeholder="ej. IA en salud")

# Si el usuario introduce un tema
if query:
    with st.spinner("Buscando en la web..."):
        results = perform_search(query, TAVILY_API_KEY)

    st.subheader("🔗 Resultados Web")
    for res in results:
        st.markdown(f"**[{res['title']}]({res['url']})**")
        st.markdown(f"{res['content'][:200]}...")  # Vista previa corta

    full_text = " ".join([r['content'] for r in results])

    with st.spinner("Generando resumen..."):
        summary = generate_summary(full_text, OPENAI_API_KEY)

    st.subheader("Resumen")
    st.markdown(summary)

    with st.spinner("Creando nube de palabras..."):
        fig = create_wordcloud(full_text)

    st.subheader("Nube de Palabras")
    st.pyplot(fig)
