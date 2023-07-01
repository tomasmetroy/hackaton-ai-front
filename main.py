import streamlit as st
import pandas as pd

from src.auth import check_password
from src.components import (
    get_description,
)

from dotenv import load_dotenv
load_dotenv()


if check_password():
    st.set_page_config(page_title="Hackaton EYU", page_icon="📈", layout="wide")
    st.title("OpinAI: lo mejor de tu catálogo")
    st.markdown("""
    Te mostramos un análisis de reseñas sobre ventajas y desventajas del
    producto seleccionado, junto con recomendaciones sobre productos similares.
    """)

    # option = st.selectbox(
    #     '¿Qué información quieres visualizar?', ['-', 'Generar descripción']
    # )

    if True:
        product_id = st.selectbox(label="Nombre producto", options=["", "Lavadora", "Licuadora"])
        if product_id != '':
            description_component = get_description(product_id)
            if isinstance(description_component, pd.DataFrame):
                col1, col2, col3, col4 = st.columns(4)
                col1.subheader("Descripción")
                col1.write(description_component.iloc[0]["description"])
                col2.subheader("Comentarios positivos")
                col2.write(description_component.iloc[0]["positive"])
                col3.subheader("Comentarios negativos")
                col3.write(description_component.iloc[0]["negative"])
                col4.subheader("Productos relacionados")
                col4.write(f"- {description_component.iloc[0]['recommended'][0]}")
                col4.write(f"- {description_component.iloc[0]['recommended'][1]}")
