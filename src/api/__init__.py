from os import environ
from requests import get
from time import sleep


def get_description(product_id):
    if True:
        sleep(2)
        if product_id == "Lavadora":
            return {
                "description": "Según el análisis de reseñas de productos similares a la aspiradora, se encontraron preocupaciones sobre el ruido y la apariencia, pero su eficiencia de limpieza fue altamente elogiada. Si buscas una aspiradora eficiente y capaz de una limpieza a fondo, podría ser adecuada para ti.",
                "positive": "Recomendamos nuestra potente y ergonómica aspiradora. Con su gran potencia de succión, podrás eliminar fácilmente la suciedad de cualquier superficie. Además, es multifuncional, ecológica y estéticamente atractiva, adaptándose a cualquier estilo de decoración en tu hogar.",
                "negative": "Al elegir una aspiradora, ten en cuenta preocupaciones comunes como el alto costo, el tamaño voluminoso, la dificultad para limpiar, la baja capacidad de almacenamiento y el cable corto. Considera opciones más compactas, con mayor capacidad de almacenamiento, cable más largo, fácil limpieza y asequibles.",
                "recommended": ['Lavadora Iguazu 2', 'Lavadora AH2']
            }
        else:
            return {
                'description': 'Los usuarios están encantados con esta increíble licuadora. Su potencia y versatilidad permiten preparar una amplia variedad de batidos y bebidas saludables. Las cuchillas afiladas garantizan una textura suave y sin grumos. El diseño moderno y fácil de limpiar ha sido elogiado por todos. Sin duda, esta licuadora se ha convertido en un imprescindible en la cocina de muchos, recomendada para los amantes de los batidos frescos y nutritivos. ¡Una elección perfecta para mejorar tu estilo de vida!',
                'positive': 'Los usuarios suelen destacar la versatilidad, durabilidad y calidad del producto.',
                'negative': 'Aspectos negativos suelen incluir exceso de ruido.',
                'recommended': ['Licuadora DarkB', 'Blender AA']
            }
    else:
        url = f'{environ.get("API_URL")}/{product_id}'
        response = get(url)
        if response.status_code != 200:
            return {}
        return response.json()
