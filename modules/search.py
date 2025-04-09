import requests

def perform_search(query, api_key, max_results=5):
    """
    Realiza una búsqueda web utilizando la API de Tavily.

    Parámetros:
        query (str): La consulta de búsqueda.
        api_key (str): Clave de la API de Tavily.
        max_results (int): Número de resultados de búsqueda a devolver.

    Retorna:
        List[dict]: Lista de resultados de búsqueda con título, URL y contenido.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "query": query,
        "search_depth": "advanced",
        "max_results": max_results
    }

    response = requests.post("https://api.tavily.com/search", headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        raise Exception(f"Solicitud a la API de Tavily fallida: {response.status_code} - {response.text}")
