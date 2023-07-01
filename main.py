import streamlit as st
import pandas as pd

from src.auth import check_password
from src.components import (
    upload_dbs,
)
from src.api import map_ids


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
        id_mapping_component = upload_dbs()
        if isinstance(id_mapping_component, pd.DataFrame):
            id_mapping_component
            if st.button('Confirmar archivos', type='primary'):
                st.success('¡Archivos cargados correctamente!', icon="✅")
                st.info('Mapeando ids..')
                mapped_ids = map_ids(id_mapping_component)
                st.success('¡Aquí tienes tus ids relacionados!', icon="✅")
                st.json(mapped_ids)
