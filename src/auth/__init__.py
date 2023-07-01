# import streamlit as st
# from os import environ


def check_password():
    return True
    # def password_entered():
    #     return True
    #     if st.session_state["password"] == environ.get("PASSWORD"):
    #         st.session_state["password_correct"] = True
    #         del st.session_state["password"]
    #     else:
    #         st.session_state["password_correct"] = False

    # if "password_correct" not in st.session_state:
    #     st.text_input(
    #         "Password", type="password", on_change=password_entered,
    #         key="password"
    #     )
    #     return False
    # elif not st.session_state["password_correct"]:
    #     st.text_input(
    #         "Password", type="password", on_change=password_entered,
    #         key="password"
    #     )
    #     st.error("😕 Password incorrect")
    #     return False
    # else:
    #     return True
