from wordcloud import WordCloud
import matplotlib.pyplot as plt

def crear_nube_de_palabras(texto):
    """
    Genera una figura de nube de palabras a partir del texto dado.

    Parámetros:
        texto (str): El texto del cual generar la nube de palabras.

    Devuelve:
        matplotlib.figure.Figure: Una figura de Matplotlib que contiene la nube de palabras.
    """
    nube_de_palabras = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=100
    ).generate(texto)

    # Crear una figura de Matplotlib
    figura, eje = plt.subplots(figsize=(10, 5))
    eje.imshow(nube_de_palabras, interpolation='bilinear')
    eje.axis("off")
    plt.tight_layout(pad=0)

    return figura
