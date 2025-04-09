import re

def clean_text(text):
    """
    Elimina caracteres no deseados y espacios en blanco excesivos del texto.
    
    Parámetros:
        text (str): Texto de entrada sin procesar.

    Retorna:
        str: Texto limpio.
    """
    text = re.sub(r'\s+', ' ', text)  # Elimina espacios en blanco/nuevas líneas adicionales
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Elimina caracteres no ASCII
    return text.strip()

def truncate_text(text, max_length=200):
    """
    Trunca el texto a una longitud máxima de caracteres.

    Parámetros:
        text (str): Texto de entrada.
        max_length (int): Número máximo de caracteres permitidos.

    Retorna:
        str: Texto truncado con puntos suspensivos si es demasiado largo.
    """
    return text if len(text) <= max_length else text[:max_length] + "..."
