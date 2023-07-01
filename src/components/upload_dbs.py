import streamlit as st
import pandas as pd


def upload_dbs():
    first_db = st.file_uploader(
        'Selecciona tu primer set de ids.'
    )
    second_db = st.file_uploader(
        'Selecciona tu segundo set de ids.'
    )
    if first_db is not None and second_db is not None:
        first_db_df = pd.read_csv(first_db)
        second_db_df = pd.read_csv(second_db)
        component = pd.DataFrame()
        component['id_1'] = first_db_df['id']
        component['id_2'] = second_db_df['id']
        return component
