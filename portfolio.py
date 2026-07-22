import streamlit as st
st.set_page_config(page_title="Thiago Ramires | Portfólio", page_icon="💻", layout="centered")

st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 800;
        color: #CCFF00; /* Amarelo Neon */
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #A0AEC0;
        text-align: center;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #CCFF00;
        border-bottom: 2px solid #CCFF00;
        padding-bottom: 5px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .card {
        background-color: #1E293B;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 5px solid #CCFF00;
    }
    .project-title {
        font-size: 18px;
        font-weight: bold;
        color: #F8FAFC;
    }
    .btn-link {
        display: inline-block;
        background-color: #CCFF00;
        color: #0F172A !important;
        font-weight: bold;
        padding: 8px 16px;
        border-radius: 5px;
        text-decoration: none;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">THIAGO RAMIRES</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Desenvolvedor Python & Analista de Dados Júnior</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">👤 Sobre Mim</div>', unsafe_allow_html=True)
st.write("""
Olá! Sou o Thiago. Desenvolvo soluções utilizando **Python** e bancos de dados **PostgreSQL**. 
Sou focado em transformar problemas de negócios em aplicações web modernas e intuitivas. 
Tenho facilidade para resolver desafios de infraestrutura, lógica de dados e publicação de sistemas na nuvem.
""")

st.markdown('<div class="section-title">🌐 Conecte-se Comigo</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.link_button("🚀 Meu GitHub", "https://github.com", use_container_width=True)
with col2:
    st.link_button("💼 Meu LinkedIn", "https://linkedin.com", use_container_width=True) # Cole seu link real aqui

st.markdown('<div class="section-title">🛠️ Projetos em Destaque</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <div class="project-title">🏋️‍♂️ SmartGym AI Cloud</div>
        <p style="color: #94A3B8; font-size: 14px; margin-top: 5px;">
            Sistema de gerenciamento de membros de academia com <b>lógica preditiva de risco de evasão (Churn)</b> 
            e recomendação dinâmica de treinos segmentada por objetivo, gênero e nível (Iniciante ao Avançado). 
            Desenvolvido em Programação Orientada a Objetos (POO) e integrado ao banco de dados PostgreSQL na nuvem.
        </p>
        <a class="btn-link" href="https://streamlit.app" target="_blank">Acessar Sistema ao Vivo</a>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">📊 Principais Competências</div>', unsafe_allow_html=True)
competencias = ["Python", "Streamlit", "SQL / PostgreSQL", "Git & GitHub", "Modelagem Orientada a Objetos", "Cloud Deploy (Streamlit Cloud / Supabase)"]
st.write("  |  ".join([f"**{comp}**" for comp in competencias]))

st.markdown("---")
st.markdown('<div style="text-align: center; color: #64748B; font-size: 12px;">© 2026 - Thiago Ramires. Criado inteiramente em Python e Streamlit.</div>', unsafe_allow_html=True)
