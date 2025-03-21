import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/foto_perfil.jpeg", width=230)

with col2:
    st.title("Felipe Jerônimo", anchor=False)
    st.write(
        "Engenheiro de dados."
    )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 2 anos de experiência na área de suporte e análise de dados
    - Sólida experiência prática e conhecimento em Python e SQL
    - Bom entendimento de engenharia e análise de dados
    - Boa capacidade de trabalho em equipe, proatividade e comunicação
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python, SQL, VBA
    - Data Visualization: Looker, PowerBi, Plotly
    - Databases: MySQL, Postgres, MongoDB
    - Cloud: AWS
    """
)