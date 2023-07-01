from os import environ
from requests import get
from time import sleep


def get_description(product_id):
    if True:
        sleep(2)
        return {
            "description": "Basado en el análisis de las reseñas de productos similares, puedo recomendar el producto . Los consumidores han destacado su eficiencia y buen rendimiento, lo que indica que es una opción confiable. Sin embargo, algunas reseñas mencionan que el producto puede ser ruidoso, lo cual puede ser una preocupación para aquellos que buscan un funcionamiento silencioso. Además, algunos usuarios han comentado que el diseño del producto no es estéticamente agradable. A pesar de estas preocupaciones, la mayoría de las reseñas resaltan su eficiencia y buen desempeño, lo que lo convierte en una opción a considerar para aquellos que valoran la funcionalidad sobre la estética.",
            "positive": "Recomendación: Basado en el análisis de las reseñas de productos similares, podemos concluir que el producto es altamente eficiente y de calidad. Los consumidores han elogiado su rendimiento y lo han calificado como bueno en términos de satisfacción. Si estás buscando un producto confiable y efectivo, este es definitivamente una excelente opción. Su eficiencia garantiza que obtendrás resultados óptimos, y su calidad asegura una larga durabilidad. No dudes en adquirir este producto, ya que su reputación positiva respalda su desempeño y te brindará una experiencia satisfactoria.",
            "negative": "Basado en el análisis de las reseñas de productos similares, es importante tener en cuenta que algunos consumidores han expresado preocupaciones sobre el nivel de ruido y el aspecto visual de este producto. Algunos usuarios han mencionado que el producto puede ser ruidoso en su funcionamiento, lo cual puede resultar molesto en determinadas situaciones. Además, se ha señalado que el diseño estético del producto puede no ser del agrado de todos los usuarios, describiéndolo como poco atractivo o incluso feo.\n\nTeniendo en cuenta estas preocupaciones, es recomendable que los consumidores finales consideren cuidadosamente si el nivel de ruido y el aspecto visual son aspectos importantes para ellos antes de realizar su compra. Es posible que aquellos que busquen un producto silencioso y estéticamente agradable deseen explorar otras opciones disponibles en el mercado. Sin embargo, es importante recordar que las preferencias pueden variar de un individuo a otro, por lo que es recomendable leer otras reseñas y considerar otros factores relevantes antes de tomar una decisión final.",
            "recommended": [
                "Espantador de moscas 3000",
                "Lavanda en spray"
            ]
        }
    else:
        url = f'{environ.get("API_URL")}/{product_id}'
        response = get(url)
        if response.status_code != 200:
            return {}
        return response.json()
