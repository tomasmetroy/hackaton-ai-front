import streamlit as st
import pandas as pd

from src.auth import check_password
from src.components import (
    get_description,
)

from dotenv import load_dotenv
load_dotenv()


if check_password():
    st.set_page_config(page_title="Tucar", page_icon="📈", layout="wide")
    st.title("Hackaton EY - Bianquilu & Cia")
    st.markdown("""
    Esta aplicación permite generar descripciones mediante AI
    * **Python libraries used:** pandas, streamlit, bigquery
    * **Data source:** Tucar app
    """)

    option = st.selectbox(
        '¿Qué información quieres visualizar?', ['-', 'Generar descripción']
    )

    if option == 'Generar descripción':
        product_id = st.text_input('Nombre producto')
        if product_id != '':
            description_component = get_description(product_id)
            if isinstance(description_component, pd.DataFrame):
                st.dataframe(description_component)
