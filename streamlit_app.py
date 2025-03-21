import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="Sobre mim",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/projetos.py",
    title="Projetos",
    icon=":material/bar_chart:",
)
certificado_1_page = st.Page(
    "views/certificados.py",
    title="Certificados",
    icon=":material/license:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Informações": [about_page],
        "Projetos": [project_1_page],#, project_2_page],
        "Certificados": [certificado_1_page]
    }
)


# --- RUN NAVIGATION ---
pg.run()