import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import os
import re

# -----------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Caio Barbosa | Engenharia, Projetos & Gestão de Ativos",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. FUNÇÃO INTELIGENTE DE CARREGAMENTO EM BASE64
# -----------------------------------------------------------------------------
def carregar_arquivo_base64(candidatos_nomes, mime_type="image/png"):
    if isinstance(candidatos_nomes, str):
        candidatos_nomes = [candidatos_nomes]
    for nome in candidatos_nomes:
        if os.path.exists(nome):
            with open(nome, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                ext = nome.split(".")[-1].lower()
                real_mime = "image/jpeg" if ext in ["jpg", "jpeg"] else ("application/pdf" if ext == "pdf" else "image/png")
                return f"data:{real_mime};base64,{encoded}"
    return ""

# Foto de Perfil Executiva
foto_perfil_b64 = carregar_arquivo_base64(["foto_perfil.png", "foto_perfil.jpg", "perfil.png", "perfil.jpg", "foto.png", "foto.jpg"])

# Fundo Obra / Guindaste ao Pôr do Sol
fundo_obra_b64 = carregar_arquivo_base64(["fundo_obra.jpg", "fundo_obra.png", "background_obra.jpg", "fundo.jpg", "fundo.png"], "image/jpeg")
url_fundo_default = "https://images.unsplash.com/photo-1541888946425-d0fbb186156f?w=1920&q=80"
bg_image_css = fundo_obra_b64 if fundo_obra_b64 else url_fundo_default

# Conselhos
cft_b64 = carregar_arquivo_base64(["CFT.png", "cft.png"])
crea_b64 = carregar_arquivo_base64(["CREA-SP.png", "crea-sp.png", "CREA.png"])

# Softwares e Ferramentas
autocad_b64 = carregar_arquivo_base64(["AUTOCAD.png", "autocad.png"])
revit_b64 = carregar_arquivo_base64(["REVIT.png", "revit.png"])
solidworks_b64 = carregar_arquivo_base64(["SOLIDWORKS.png", "solidworks.png"])
tekla_b64 = carregar_arquivo_base64(["Tekla_Structures_Logo.png", "TEKLA.png", "tekla.png", "Tekla.png"])
sketchup_b64 = carregar_arquivo_base64(["SKETCHUP.png", "sketchup.png", "SketchUp.png"])
inventor_b64 = carregar_arquivo_base64(["INVENTOR.png", "inventor.png"])
msproject_b64 = carregar_arquivo_base64(["MS PROJECT.png", "ms project.png", "msproject.png"])
excel_b64 = carregar_arquivo_base64(["MS EXCEL.png", "ms excel.png", "excel.png", "EXCEL.png"])
visio_b64 = carregar_arquivo_base64(["MS VISION.png", "MS VISIO.png", "ms vision.png", "visio.png"])
powerbi_b64 = carregar_arquivo_base64(["POWER BI.png", "power bi.png", "powerbi.png"])
looker_b64 = carregar_arquivo_base64(["Looker-Studio-Logo.png", "looker.png"])
bizagi_b64 = carregar_arquivo_base64(["bizagi-modeler.png", "bizagi.png"])
factoryio_b64 = carregar_arquivo_base64(["FACTORY IO.png", "factory io.png", "factoryio.png"])
coreldraw_b64 = carregar_arquivo_base64(["CORELDRAW.png", "coreldraw.png"])
photoshop_b64 = carregar_arquivo_base64(["Adobe_Photoshop.png", "photoshop.png"])
illustrator_b64 = carregar_arquivo_base64(["illustrator-cs6_2.jpg", "illustrator-cs6.jpg", "illustrator.png", "illustrator.jpg"])
vba_b64 = carregar_arquivo_base64(["VBA.png", "vba.png", "Vba.png"])
vray_b64 = carregar_arquivo_base64(["VRAY.png", "vray.png", "V-RAY.png", "v-ray.png", "V_Ray.png"])

# PDF do Acervo Oficial
pdf_acervo_b64 = carregar_arquivo_base64(["registradas_2.pdf", "registradas.pdf", "acervo_tecnico.pdf"], "application/pdf")

# -----------------------------------------------------------------------------
# 3. CSS EXECUTIVO
# -----------------------------------------------------------------------------

st.markdown("""
<style>
    /* Card responsivo com ajuste automático de padding e borda */
    .hero-card {
        background: linear-gradient(135deg, rgba(16, 26, 43, 0.95), rgba(10, 17, 30, 0.98));
        border-left: 5px solid #FF6B00;
        border-radius: 12px;
        padding: clamp(16px, 4vw, 36px);
        margin: 10px auto;
        max-width: 900px;
        box-sizing: border-box;
        overflow: hidden;
        word-wrap: break-word;
    }

    /* Subtítulo / Tagline superior */
    .hero-tag {
        color: #FF8C33;
        font-weight: 700;
        font-size: clamp(0.75rem, 2vw, 0.95rem);
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    /* Título com escala fluida para não quebrar lateralmente */
    .hero-title {
        color: #FFFFFF;
        font-weight: 900;
        font-size: clamp(1.4rem, 5vw, 2.5rem);
        line-height: 1.15;
        text-transform: uppercase;
        margin: 0 0 16px 0;
        hyphens: auto;
    }

    /* Corpo do texto explicativo */
    .hero-body {
        color: #E0E6ED;
        font-size: clamp(0.85rem, 2.2vw, 1rem);
        line-height: 1.5;
        margin-bottom: 24px;
    }

    /* Botão responsivo */
    .btn-acervo {
        display: inline-block;
        width: 100%;
        max-width: 380px;
        background-color: #FF6B00;
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: clamp(0.8rem, 2.5vw, 0.95rem);
        text-align: center;
        text-decoration: none;
        padding: 12px 18px;
        border-radius: 8px;
        box-sizing: border-box;
        transition: background 0.3s ease;
    }

    .btn-acervo:hover {
        background-color: #E05D00;
    }
</style>

<div class="hero-card">
    <div class="hero-tag">⚡ ENGENHARIA MULTIDISCIPLINAR & GESTÃO TÉCNICA</div>
    <div class="hero-title">POTENCIALIZE A PRODUTIVIDADE E A CONFIABILIDADE DA SUA OPERAÇÃO</div>
    <div class="hero-body">
        Soluções completas em <b>Engenharia de Produção, Mecânica e Infraestrutura Elétrica</b>. Mais de 10 anos de atuação como Responsável Técnico <b>(CREA/CFT)</b>, integrando compatibilização em <b>BIM 5D</b>, <b>Engenharia de Dados</b> e metodologias preditivas para assegurar máxima confiabilidade operacional, segurança jurídica e eficiência em ativos de missão crítica.
    </div>
    <a href="#" class="btn-acervo">📄 CONSULTAR ACERVO TÉCNICO OFICIAL (PDF)</a>
</div>
""", unsafe_allow_html=True)
# -----------------------------------------------------------------------------
# 4. CONFIGURAÇÃO DE CONTROLE PLOTLY
# -----------------------------------------------------------------------------
PLOTLY_CONFIG = {
    'displayModeBar': False,
    'scrollZoom': False,
    'doubleClick': False,
    'staticPlot': False
}

# -----------------------------------------------------------------------------
# 5. TRATAMENTO E CARREGAMENTO DE DADOS
# -----------------------------------------------------------------------------
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv("trts_projetos.csv")
        df = df.sort_values(by=["ano", "id_doc"], ascending=[False, False]).reset_index(drop=True)
        return df
    except Exception:
        return pd.DataFrame()

df_projetos = carregar_dados()

# -----------------------------------------------------------------------------
# 6. TOP UTILITY BAR
# -----------------------------------------------------------------------------
st.markdown("""
<div class="top-ribbon-container">
    <div class="top-ribbon-text">
        <span>📍 São Paulo, SP - Brasil</span> &nbsp;|&nbsp; 
        <span>📱 (11) 92096-0786</span> &nbsp;|&nbsp; 
        <span>📧 caioflavio.cf@gmail.com</span>
    </div>
    <div class="top-ribbon-links">
        <a href="https://www.linkedin.com/in/caiobarbosas" target="_blank">LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. NAVBAR COM LOGOMARCAS OFICIAIS (CFT & CREA-SP)
# -----------------------------------------------------------------------------
nav_c1, nav_c2 = st.columns([6.2, 3.8])

with nav_c1:
    st.markdown("""
    <div>
        <h2 style="margin:0; font-size:1.65rem; color:#F8FAFC; font-weight:900; letter-spacing:0.5px;">CAIO BARBOSA DOS SANTOS</h2>
        <p style="margin:0; font-size:0.88rem; color:#FB923C; font-weight:700; text-transform:uppercase;">Engenharia de Produção & Mecânica | Projetos & Operações</p>
    </div>
    """, unsafe_allow_html=True)

with nav_c2:
    cft_img_html = f'<img src="{cft_b64}" height="42" style="object-fit:contain;" alt="CFT">' if cft_b64 else '<span style="font-weight:800; color:#0F172A;">CFT</span>'
    crea_img_html = f'<img src="{crea_b64}" height="42" style="object-fit:contain;" alt="CREA-SP">' if crea_b64 else '<span style="font-weight:800; color:#0F172A;">CREA-SP</span>'
    
    st.markdown(f"""
    <div class="council-box-header">
        {cft_img_html}
        <div style="height:32px; width:1px; background-color:#CBD5E1;"></div>
        {crea_img_html}
        <div class="council-text-title">
            HABILITAÇÃO TÉCNICA
            <span class="council-text-badge">CREA-SP / CFT</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 8. HERO BANNER PRINCIPAL COM FOTO DE PERFIL
# -----------------------------------------------------------------------------
link_botao_pdf = pdf_acervo_b64 if pdf_acervo_b64 else "#acervo"
target_attr = 'target="_blank" download="Acervo_Tecnico_CFT_Caio_Barbosa.pdf"' if pdf_acervo_b64 else ''

foto_html = f'<img src="{foto_perfil_b64}" class="hero-profile-photo" alt="Caio Barbosa">' if foto_perfil_b64 else ''

st.markdown(f"""
<div class="hero-banner-pro">
    <div class="hero-flex-wrapper">
        <div>
            <div class="hero-pretitle-pro">⚡ ENGENHARIA MULTIDISCIPLINAR & GESTÃO TÉCNICA</div>
            <div class="hero-headline-pro">Potencialize a Produtividade e a Confiabilidade da Sua Operação</div>
            <div class="hero-description-pro">
                Soluções completas em <b>Engenharia de Produção, Mecânica e Infraestrutura Elétrica</b>. 
                Mais de 10 anos de atuação como Responsável Técnico (<b>CREA/CFT</b>), integrando compatibilização em <b>BIM 5D</b>, 
                <b>Engenharia de Dados</b> e metodologias preditivas para assegurar máxima confiabilidade operacional, 
                segurança jurídica e eficiência em ativos de missão crítica.
            </div>
            <div>
                <a href="{link_botao_pdf}" {target_attr} class="hero-btn-action">📄 CONSULTAR ACERVO TÉCNICO OFICIAL (PDF)</a>
            </div>
        </div>
        <div>
            {foto_html}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. KPIS COM HOVER TOOLTIP FLUTUANTE
# -----------------------------------------------------------------------------
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown("""
    <div class="kpi-hover-card">
        <div class="kpi-num-pro">320+</div>
        <div class="kpi-label-pro">Projetos Executados</div>
        <div class="kpi-hint-tag">ℹ️ Passe o mouse</div>
        <div class="kpi-tooltip-box">
            <b style="color:#FB923C;">Multidisciplinar:</b><br>
            Acervo técnico completo abrangendo mais de 320 entregas de engenharia multidisciplinar, contemplando modelagens paramétricas em BIM/CAD (Revit, Plant 3D e SolidWorks), pranchas executivas em DWG, memoriais de cálculo estrutural/elétrico e composições orçamentárias detalhadas.
        </div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="kpi-hover-card">
        <div class="kpi-num-pro">65</div>
        <div class="kpi-label-pro">TRTs Oficiais CFT</div>
        <div class="kpi-hint-tag">ℹ️ Passe o mouse</div>
        <div class="kpi-tooltip-box">
            <b style="color:#FB923C;">Responsabilidade Técnica:</b><br>
            Acervo de Responsabilidade Técnica formalmente homologado junto ao Conselho Federal dos Técnicos Industriais (CFT). Registros de projetos elétricos, sistemas de combate a incêndio (PPCI), laudos periciais e reformas civis/mecânicas, garantindo plena conformidade e segurança jurídica.
        </div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="kpi-hover-card">
        <div class="kpi-num-pro">20+</div>
        <div class="kpi-label-pro">Projetos CPFL Aprovados</div>
        <div class="kpi-hint-tag">ℹ️ Passe o mouse</div>
        <div class="kpi-tooltip-box">
            <b style="color:#FB923C;">Homologação e Concessionárias:</b><br>
            Histórico com mais de 20 projetos elétricos aprovados com 100% de conformidade junto à concessionária CPFL sob a norma GED-13. Engloba dimensionamento de subestações, entradas de média e baixa tensão coletivas/individuais, malhas de aterramento e estudos de seletividade e proteção.
        </div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="kpi-hover-card">
        <div class="kpi-num-pro">-25%</div>
        <div class="kpi-label-pro">Lead Time de Projeto</div>
        <div class="kpi-hint-tag">ℹ️ Passe o mouse</div>
        <div class="kpi-tooltip-box">
            <b style="color:#FB923C;">Eficiência de Processos:</b><br>
            Ganhos expressivos de produtividade e redução no ciclo de desenvolvimento técnico através de metodologias Lean Six Sigma e automação com blocos dinâmicos CAD e famílias BIM. Otimização de fluxos de engenharia que elevou a padronização e reduziu drasticamente o retrabalho em obras.
        </div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown("""
    <div class="kpi-hover-card">
        <div class="kpi-num-pro">10 Anos</div>
        <div class="kpi-label-pro">Responsabilidade Legal</div>
        <div class="kpi-hint-tag">ℹ️ Passe o mouse</div>
        <div class="kpi-tooltip-box">
            <b style="color:#FB923C;">Experiência e Liderança:</b><br>
            Uma década de atuação consolidada como Responsável Técnico e Engenheiro Projetista, liderando contratos multidisciplinares com emissão de ARTs e TRTs. Vivência integral no ciclo de vida de ativos industriais e civis, integrando engenharia legal, auditorias e gestão física de obras.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 10. ABAS DE NAVEGAÇÃO
# -----------------------------------------------------------------------------
tab_resumo, tab_experiencia, tab_tools, tab_analytics, tab_acervo, tab_formacao = st.tabs([
    "💡 Resumo & Competências",
    "💼 Trajetória & Experiências",
    "🛠️ Programas & Ferramentas",
    "📊 Indicadores & Produtividade",
    "📂 Acervo Técnico (TRTs & Projetos)",
    "🎓 Formação Acadêmica & Técnica"
])

# --- ABA 1: RESUMO PROFISSIONAL & COMPETÊNCIAS ---
with tab_resumo:
    st.markdown("### 📌 Resumo Profissional")
    st.markdown("""
    <div class="card-pro-content" style="border-left: 6px solid #F37021;">
        <p style="font-size: 1.05rem; line-height: 1.7; color: #0F172A; font-weight: 500;">
            Sou <b>Engenheiro de Produção e Mecânico (CREA/CFT)</b> com <b>10 anos de experiência</b> como Responsável Técnico e Projetista. 
            Lidero projetos multidisciplinares integrando PMO/PCP ao campo para otimizar Capex/Opex. 
            Diferencio-me pelo uso de <b>Engenharia de Dados e BIM 5D</b> na gestão de ativos, reduzindo lead time e garantindo alta disponibilidade. 
            Expert em infraestrutura de missão crítica e engenharia legal, asseguro conformidade normativa e rentabilidade em projetos de alta complexidade.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Competências Técnicas & Gestão")
    
    comp1, comp2 = st.columns(2)
    with comp1:
        st.markdown("""
        <div class="card-pro-content">
            <h4>📅 Planejamento e Gestão</h4>
            <p>Estruturação de governança em PMO e controle físico-financeiro de Capex/Opex através de EAP e Caminho Crítico (CPM). Elaboração de histogramas de recursos, curvas S de avanço e matrizes probabilísticas de risco com Primavera P6 e MS Project. Foco em previsibilidade contratual, otimização de lead time e alinhamento estratégico entre planejamento executivo e rotinas de campo.</p>
            <span class="badge-tool-tag">Primavera P6</span><span class="badge-tool-tag">MS Project</span><span class="badge-tool-tag">PMO / PCP</span><span class="badge-tool-tag">Gestão de Riscos</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-pro-content">
            <h4>📊 Processos e Dados</h4>
            <p>Engenharia de dados aplicada à otimização operacional e automação de rotinas industriais. Desenvolvimento de pipelines de dados em Python e bancos SQLite para rastreabilidade de ativos e auditorias técnicas. Aplicação de Lean Six Sigma (DMAIC, VSM e Kaizen) com modelagem de dashboards em Power BI para monitoramento de KPIs estratégicos, eliminação de gargalos e tomada de decisão ágil.</p>
            <span class="badge-tool-tag">Python</span><span class="badge-tool-tag">SQL / SQLite</span><span class="badge-tool-tag">Power BI</span><span class="badge-tool-tag">Lean Six Sigma</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-pro-content">
            <h4>🏛️ Infraestrutura e Normas</h4>
            <p>Concepção e homologação de infraestruturas elétricas e de telecomunicações de alta disponibilidade. Certificação internacional Furukawa FCP Master para redes ópticas e Data Centers. Aprovação de mais de 20 projetos de subestações e baixa tensão junto à CPFL (GED-13), coordenação integral de processos de PPCI/AVCB e emissão de laudos de engenharia legal com respaldo via CREA e CFT.</p>
            <span class="badge-tool-tag">Telecom (FCP Master)</span><span class="badge-tool-tag">AVCB</span><span class="badge-tool-tag">CPFL / GED-13</span><span class="badge-tool-tag">NRs / ABNT</span>
        </div>
        """, unsafe_allow_html=True)

    with comp2:
        st.markdown("""
        <div class="card-pro-content">
            <h4>📐 Projetos e Modelagem</h4>
            <p>Engenharia de detalhamento e modelagem paramétrica em ambiente BIM 5D, integrando geometria 3D, cronograma e orçamentação (B.O.Q.). Compatibilização multidisciplinar com detecção de interferências (Clash Detection) em Navisworks e Revit. Cálculo e detalhamento de estruturas metálicas (Pipe Racks), tubulações em Plant 3D e ativos mecânicos em SolidWorks com total conformidade ABNT.</p>
            <span class="badge-tool-tag">Revit (BIM 5D)</span><span class="badge-tool-tag">SolidWorks</span><span class="badge-tool-tag">Plant 3D</span><span class="badge-tool-tag">AutoCAD Avançado</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-pro-content">
            <h4>🔧 Manutenção e Ativos</h4>
            <p>Gestão da confiabilidade e integridade operacional de ativos de missão crítica sob metodologia RCM e TPM. Elaboração e auditoria de PMOC hospitalar/industrial (Anvisa e NBR 7256) em sistemas de climatização e utilidades. Monitoramento de KPIs de performance (OEE, MTBF e MTTR), implementação de rotinas preditivas (termografia e vibração) e parametrização de ordens via IBM Maximo.</p>
            <span class="badge-tool-tag">IBM Maximo</span><span class="badge-tool-tag">TPM</span><span class="badge-tool-tag">OEE / Confiabilidade</span><span class="badge-tool-tag">PMOC / RCM</span>
        </div>
        """, unsafe_allow_html=True)

# --- ABA 2: EXPERIÊNCIAS PROFISSIONAIS ---
with tab_experiencia:
    st.markdown("### 💼 Histórico & Experiência Profissional")
    
    st.markdown("""
    <div class="card-pro-content">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <h4 style="margin:0; color:#F37021;">L. Parice</h4>
            <span class="badge-cft-tag">05/2026 - Atual</span>
        </div>
        <p style="font-weight:700; color:#0F172A; margin-bottom:8px;">Engenheiro de Planejamento e Processos</p>
        <p>Atuação focada na gestão de ativos de missão crítica e utilidades hospitalares. Classificação de criticidade e aplicação de RCM (Manutenção Centrada na Confiabilidade) para sistemas de climatização (chillers e fancoils) prioritários em UTIs e centros cirúrgicos.</p>
        <ul>
            <li>Gestão integral do <b>PMOC</b> (Plano de Manutenção, Operação e Controle), garantindo qualidade do ar e integridade de filtros HEPA sob diretrizes Anvisa e NBR 7256.</li>
            <li>Monitoramento contínuo dos indicadores de confiabilidade (<b>MTBF e MTTR</b>) e rotinas preditivas (termografia e análise de vibração em compressores e bombas).</li>
            <li>Coordenação da calibração rastreável de sensores das redes de frio sob padrão <b>RBC (Rede Brasileira de Calibração)</b>.</li>
            <li>Estruturação de planos de contingência com redundâncias elétricas para chillers e controle de estoque crítico (<b>MRO</b>).</li>
        </ul>
        <div style="margin-top:10px;"><b>Ferramentas:</b> <span class="badge-tool-tag">MS Project</span><span class="badge-tool-tag">Python / SQL</span><span class="badge-tool-tag">Excel Avançado</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-pro-content">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <h4 style="margin:0; color:#F37021;">Autônomo</h4>
            <span class="badge-cft-tag">01/2025 - Atual</span>
        </div>
        <p style="font-weight:700; color:#0F172A; margin-bottom:8px;">Engenheiro Consultor de Projetos e Instalações</p>
        <p>Consultoria multidisciplinar e viabilização de Capex/Opex com emissão de ARTs e TRTs.</p>
        <ul>
            <li>Cálculo estrutural, hidráulico, elétrico e mecânico, com detalhamento em <b>BIM 5D (Revit/SolidWorks)</b>.</li>
            <li>Projetos de baixa, média e alta tensão (<b>até 800kVA</b>) e redes de missão crítica.</li>
            <li><b>Engenharia Legal:</b> coordenação técnica de processos de AVCB, laudos periciais e inspeções prediais com 100% de conformidade técnica.</li>
        </ul>
        <div style="margin-top:10px;"><b>Ferramentas:</b> <span class="badge-tool-tag">Revit (BIM 5D)</span><span class="badge-tool-tag">SolidWorks</span><span class="badge-tool-tag">AutoCAD</span><span class="badge-tool-tag">Navisworks</span><span class="badge-tool-tag">MS Project</span><span class="badge-tool-tag">Power BI</span><span class="badge-tool-tag">Python / SQL</span><span class="badge-tool-tag">IBM Maximo</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-pro-content">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <h4 style="margin:0; color:#F37021;">Tracevia S/A</h4>
            <span class="badge-cft-tag">08/2025 - 11/2025</span>
        </div>
        <p style="font-weight:700; color:#0F172A; margin-bottom:8px;">Engenheiro de Planejamento</p>
        <p>Gestão estratégica de projetos de infraestrutura tecnológica (ITS) e controle físico-financeiro sob práticas PMBOK.</p>
        <ul>
            <li>Desenvolvimento em <b>Python e SQLite</b> para rastreabilidade de ativos e logística em tempo real.</li>
            <li>Dashboards estratégicos em <b>Power BI</b> que eliminaram falhas de auditoria.</li>
            <li>Levantamento de materiais (<b>B.O.Q.</b>) e padronização de fluxos operacionais.</li>
        </ul>
        <div style="margin-top:10px;"><b>Ferramentas:</b> <span class="badge-tool-tag">MS Project</span><span class="badge-tool-tag">Python</span><span class="badge-tool-tag">SQLite</span><span class="badge-tool-tag">Power BI</span><span class="badge-tool-tag">PMBOK</span><span class="badge-tool-tag">Jira / Trello</span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-pro-content">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <h4 style="margin:0; color:#F37021;">Grupo Garcia</h4>
            <span class="badge-cft-tag">03/2018 - 01/2025</span>
        </div>
        <p style="font-weight:700; color:#0F172A; margin-bottom:8px;">Supervisor de Projetos</p>
        <p>Estruturação do departamento técnico e liderança de equipes multidisciplinares.</p>
        <ul>
            <li>Padronização em blocos dinâmicos CAD com <b>redução de 25% no tempo de elaboração</b> de projetos.</li>
            <li>Compatibilização em <b>AutoCAD e Revit</b> com eliminação sistemática de interferências em obra.</li>
            <li><b>Incremento de 10% no faturamento operacional</b> pela redução drástica de retrabalhos.</li>
        </ul>
        <div style="margin-top:10px;"><b>Ferramentas:</b> <span class="badge-tool-tag">Revit (BIM)</span><span class="badge-tool-tag">AutoCAD</span><span class="badge-tool-tag">Navisworks</span><span class="badge-tool-tag">BIM 360</span><span class="badge-tool-tag">Trello / Asana</span></div>
    </div>
    """, unsafe_allow_html=True)

# --- ABA 3: PROGRAMAS & FERRAMENTAS ---
with tab_tools:
    st.markdown("### 🛠️ Domínio de Softwares, Ferramentas & Ecossistema Digital")
    st.markdown("Aplicações práticas de modelagem 3D, engenharia de processos, automação industrial, gestão de projetos e ciência de dados.")
    st.write("")

    # LINHA 1: AUTOCAD, REVIT, SOLIDWORKS
    t1, t2, t3 = st.columns(3)

    with t1:
        img_src = autocad_b64 if autocad_b64 else "https://cdn-icons-png.flaticon.com/512/5968/5968434.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="AutoCAD">
                    <div>
                        <p class="card-tool-name">AutoCAD</p>
                        <p class="card-tool-category">CAD 2D/3D & Automação</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Elaboração de projetos executivos civis, mecânicos e elétricos. Criação e padronização de <b>blocos dinâmicos avançados</b> com atributos inteligentes, reduzindo em até 25% o tempo de detalhamento técnico.
                </p>
            </div>
            <div><span class="badge-tool-tag">Blocos Dinâmicos</span><span class="badge-tool-tag">Projetos Executivos</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t2:
        img_src = revit_b64 if revit_b64 else "https://cdn-icons-png.flaticon.com/512/5968/5968434.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Revit">
                    <div>
                        <p class="card-tool-name">Autodesk Revit</p>
                        <p class="card-tool-category">Modelagem Paramétrica BIM 5D</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Desenvolvimento de modelos paramétricos multidisciplinares (Arquitetura, Estruturas e MEP). Extração automática de quantitativos (B.O.Q.), detecção de interferências (Clash Detection) e integração direta com o planejamento físico.
                </p>
            </div>
            <div><span class="badge-tool-tag">BIM 5D</span><span class="badge-tool-tag">Clash Detection</span><span class="badge-tool-tag">B.O.Q.</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t3:
        img_src = solidworks_b64 if solidworks_b64 else "https://cdn-icons-png.flaticon.com/512/1086/1086741.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="SolidWorks">
                    <div>
                        <p class="card-tool-name">SolidWorks</p>
                        <p class="card-tool-category">Cálculo & Estruturas Metálicas</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Dimensionamento e detalhamento de estruturas metálicas pesadas (Pipe Racks, comportas estanques e suportes industriais). Análise de esforços estáticos/dinâmicos, torção e flambagem sob normas ABNT (NBR 8800).
                </p>
            </div>
            <div><span class="badge-tool-tag">Pipe Racks</span><span class="badge-tool-tag">Estruturas Metálicas</span><span class="badge-tool-tag">Análise Estática</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # LINHA 2: TEKLA, SKETCHUP, V-RAY
    t4, t5, t6 = st.columns(3)

    with t4:
        img_src = tekla_b64 if tekla_b64 else "https://cdn-icons-png.flaticon.com/512/1086/1086741.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Tekla Structures">
                    <div>
                        <p class="card-tool-name">Tekla Structures</p>
                        <p class="card-tool-category">BIM Estrutural & Detalhamento Metálico</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Modelagem e detalhamento de estruturas metálicas de alta complexidade, galpões industriais, ligações parafusadas/soldadas e geração de listas de materiais para fabricação e montagem em campo.
                </p>
            </div>
            <div><span class="badge-tool-tag">BIM Estrutural</span><span class="badge-tool-tag">Conexões Metálicas</span><span class="badge-tool-tag">Montagem</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t5:
        img_src = sketchup_b64 if sketchup_b64 else "https://cdn-icons-png.flaticon.com/512/5968/5968705.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="SketchUp">
                    <div>
                        <p class="card-tool-name">SketchUp</p>
                        <p class="card-tool-category">Modelagem 3D & Concepção Espacial</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Concepção volumétrica rápida, modelagem de leiautes industriais e prediais, estudos de viabilidade geométrica, insolação e apresentações preliminares de projetos arquitetônicos e civis.
                </p>
            </div>
            <div><span class="badge-tool-tag">Volumetria 3D</span><span class="badge-tool-tag">Layout Industrial</span><span class="badge-tool-tag">Concepção</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t6:
        img_src = vray_b64 if vray_b64 else "https://cdn-icons-png.flaticon.com/512/1086/1086741.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Chaos V-Ray">
                    <div>
                        <p class="card-tool-name">Chaos V-Ray</p>
                        <p class="card-tool-category">Renderização Fotorrealista 3D</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Renderização fotorrealista de projetos arquitetônicos e industriais, configuração avançada de materiais fisicamente corretos (PBR), iluminação global e visualização de impacto para clientes e investidores.
                </p>
            </div>
            <div><span class="badge-tool-tag">Render Fotorrealista</span><span class="badge-tool-tag">Iluminação Global</span><span class="badge-tool-tag">Materiais PBR</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # LINHA 3: MS PROJECT, PMBOK/SCRUM, EXCEL
    t7, t8, t9 = st.columns(3)

    with t7:
        img_src = msproject_b64 if msproject_b64 else "https://cdn-icons-png.flaticon.com/512/906/906324.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="MS Project">
                    <div>
                        <p class="card-tool-name">MS Project & Primavera P6</p>
                        <p class="card-tool-category">Planejamento & Controle Físico-Financeiro</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Estruturação de cronogramas integrados, determinação de Caminho Crítico (CPM), nivelamento de histogramas de recursos, curvas S de avanço físico-financeiro e gestão de riscos contratuais.
                </p>
            </div>
            <div><span class="badge-tool-tag">Caminho Crítico (CPM)</span><span class="badge-tool-tag">Curva S</span><span class="badge-tool-tag">Nivelamento</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t8:
        st.markdown("""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="https://cdn-icons-png.flaticon.com/512/1534/1534938.png" class="card-tool-img" alt="PMBOK Scrum">
                    <div>
                        <p class="card-tool-name">PMBOK & Metodologias Ágeis</p>
                        <p class="card-tool-category">Governança, Scrum & Kanban</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Liderança híbrida de projetos unindo a governança do <b>PMBOK</b> (EAP, escopo, controle de Capex/Opex e matriz de riscos) à agilidade do <b>Scrum e Kanban</b> para entregas ágeis e produtividade contínua.
                </p>
            </div>
            <div><span class="badge-tool-tag">PMBOK</span><span class="badge-tool-tag">Scrum</span><span class="badge-tool-tag">Kanban</span><span class="badge-tool-tag">Capex / Opex</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t9:
        img_src = excel_b64 if excel_b64 else "https://cdn-icons-png.flaticon.com/512/732/732220.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="MS Excel">
                    <div>
                        <p class="card-tool-name">Microsoft Excel</p>
                        <p class="card-tool-category">Engenharia Financeira & Planilhas Avançadas</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Desenvolvimento de planilhas avançadas de dimensionamento técnico, modelagem orçamentária de Capex/Opex, curvas de fluxo de caixa, fórmulas dinâmicas e tratamento analítico de dados operacionais.
                </p>
            </div>
            <div><span class="badge-tool-tag">Orçamentação</span><span class="badge-tool-tag">Modelagem Financeira</span><span class="badge-tool-tag">Dimensionamento</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # LINHA 4: POWER BI, VBA, LOOKER STUDIO
    t10, t11, t12 = st.columns(3)

    with t10:
        img_src = powerbi_b64 if powerbi_b64 else "https://cdn-icons-png.flaticon.com/512/5968/5968532.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Power BI">
                    <div>
                        <p class="card-tool-name">Microsoft Power BI</p>
                        <p class="card-tool-category">Business Intelligence & Dashboards Executivos</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Construção de relatórios analíticos interativos e painéis dinâmicos para acompanhamento de indicadores de confiabilidade (MTBF/MTTR/OEE), avanço físico-financeiro de obras e tomada de decisão gerencial.
                </p>
            </div>
            <div><span class="badge-tool-tag">Modelagem DAX</span><span class="badge-tool-tag">Dashboards Executivos</span><span class="badge-tool-tag">KPIs</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t11:
        img_src = vba_b64 if vba_b64 else "https://cdn-icons-png.flaticon.com/512/906/906324.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="VBA">
                    <div>
                        <p class="card-tool-name">VBA (Visual Basic)</p>
                        <p class="card-tool-category">Automação de Rotinas & Macros</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Desenvolvimento de macros avançadas e rotinas personalizadas em VBA para automação de tarefas repetitivas, integração entre planilhas Excel e geração automática de relatórios executivos e memoriais.
                </p>
            </div>
            <div><span class="badge-tool-tag">Macros Avançadas</span><span class="badge-tool-tag">Automação Office</span><span class="badge-tool-tag">Produtividade</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t12:
        img_src = looker_b64 if looker_b64 else "https://cdn-icons-png.flaticon.com/512/2920/2920349.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Looker Studio">
                    <div>
                        <p class="card-tool-name">Looker Studio</p>
                        <p class="card-tool-category">Cloud Analytics & Relatórios Gerenciais</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Construção de relatórios analíticos em nuvem com compartilhamento dinâmico, integrados a fontes SQL e planilhas para acompanhamento transparente de produtividade e métricas de contrato.
                </p>
            </div>
            <div><span class="badge-tool-tag">Cloud Reports</span><span class="badge-tool-tag">Métricas de Contrato</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # LINHA 5: PYTHON, SQL, BIZAGI
    t13, t14, t15 = st.columns(3)

    with t13:
        st.markdown("""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" class="card-tool-img" alt="Python">
                    <div>
                        <p class="card-tool-name">Python</p>
                        <p class="card-tool-category">Automação de Engenharia & Scripts</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Desenvolvimento de algoritmos e rotinas customizadas para automação de cálculos de dimensionamento, pipelines de tratamento de dados técnicos e integração de scripts para aumento da produtividade analítica.
                </p>
            </div>
            <div><span class="badge-tool-tag">Automação de Cálculos</span><span class="badge-tool-tag">Pipelines de Dados</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t14:
        st.markdown("""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" class="card-tool-img" alt="SQL SQLite">
                    <div>
                        <p class="card-tool-name">SQL & SQLite</p>
                        <p class="card-tool-category">Modelagem de Dados & Consultas Relacionais</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Modelagem e manipulação de bancos de dados relacionais para gestão de inventário de ativos, rastreabilidade de componentes em campo, histórico de manutenção e suporte a auditorias técnicas.
                </p>
            </div>
            <div><span class="badge-tool-tag">Modelagem Relacional</span><span class="badge-tool-tag">Rastreabilidade de Ativos</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t15:
        img_src = bizagi_b64 if bizagi_b64 else "https://cdn-icons-png.flaticon.com/512/2920/2920277.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Bizagi">
                    <div>
                        <p class="card-tool-name">Bizagi Modeler</p>
                        <p class="card-tool-category">BPMN & Engenharia de Processos</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Mapeamento, modelagem e documentação de processos operacionais e fluxos de engenharia sob a notação <b>BPMN 2.0</b>, padronizando procedimentos e eliminando gargalos de comunicação entre escritório e campo.
                </p>
            </div>
            <div><span class="badge-tool-tag">BPMN 2.0</span><span class="badge-tool-tag">Mapeamento de Processos</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # LINHA 6: VISIO, INVENTOR, FACTORY I/O
    t16, t17, t18 = st.columns(3)

    with t16:
        img_src = visio_b64 if visio_b64 else "https://cdn-icons-png.flaticon.com/512/906/906324.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Microsoft Visio">
                    <div>
                        <p class="card-tool-name">Microsoft Visio</p>
                        <p class="card-tool-category">Diagramas de Processo & P&ID</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Desenvolvimento de diagramas conceituais de engenharia, fluxogramas de processos industriais (PFD), diagramas P&ID de utilidades e leiautes de distribuição eletromecânica.
                </p>
            </div>
            <div><span class="badge-tool-tag">Diagramas P&ID</span><span class="badge-tool-tag">Fluxogramas PFD</span><span class="badge-tool-tag">Layout</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t17:
        img_src = inventor_b64 if inventor_b64 else "https://cdn-icons-png.flaticon.com/512/5968/5968434.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Inventor">
                    <div>
                        <p class="card-tool-name">Autodesk Inventor</p>
                        <p class="card-tool-category">Projetos Mecânicos Paramétricos</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Modelagem 3D avançada de máquinas e mecanismos, montagens industriais com validação de interferências e geração de detalhamento com tolerâncias geométricas e de montagem.
                </p>
            </div>
            <div><span class="badge-tool-tag">Mecanismos 3D</span><span class="badge-tool-tag">Manufatura</span><span class="badge-tool-tag">Tolerâncias</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t18:
        img_src = factoryio_b64 if factoryio_b64 else "https://cdn-icons-png.flaticon.com/512/1086/1086741.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Factory IO">
                    <div>
                        <p class="card-tool-name">Factory I/O</p>
                        <p class="card-tool-category">Gêmeos Digitais & Simulação Industrial</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Simulação dinâmica de plantas industriais em 3D (Digital Twins) para validação e comissionamento virtual de sistemas automatizados, esteiras, sensores e lógicas de acionamento.
                </p>
            </div>
            <div><span class="badge-tool-tag">Digital Twin</span><span class="badge-tool-tag">Automação 3D</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # LINHA 7: CORELDRAW, PHOTOSHOP, ILLUSTRATOR
    t19, t20, t21 = st.columns(3)

    with t19:
        img_src = coreldraw_b64 if coreldraw_b64 else "https://cdn-icons-png.flaticon.com/512/5968/5968532.png"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="CorelDRAW">
                    <div>
                        <p class="card-tool-name">CorelDRAW</p>
                        <p class="card-tool-category">Comunicação Visual & Vetorização</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Vetorização de pranchas técnicas, elaboração de layouts de comunicação visual industrial, sinalização de segurança, plantas humanizadas e diagramação executiva de memoriais comerciais.
                </p>
            </div>
            <div><span class="badge-tool-tag">Vetorização Técnica</span><span class="badge-tool-tag">Plantas Humanizadas</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t20:
        img_src = photoshop_b64 if photoshop_b64 else "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Photoshop">
                    <div>
                        <p class="card-tool-name">Adobe Photoshop</p>
                        <p class="card-tool-category">Pós-Produção & Edição de Imagens</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Tratamento de imagens de vistorias técnicas e laudos patológicos, pós-produção e texturização de maquetes 3D e refinamento estético de apresentações executivas.
                </p>
            </div>
            <div><span class="badge-tool-tag">Pós-Produção</span><span class="badge-tool-tag">Imagens Técnicas</span></div>
        </div>
        """, unsafe_allow_html=True)

    with t21:
        img_src = illustrator_b64 if illustrator_b64 else "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/illustrator/illustrator-plain.svg"
        st.markdown(f"""
        <div class="card-tool-box">
            <div>
                <div class="card-tool-header">
                    <img src="{img_src}" class="card-tool-img" alt="Illustrator">
                    <div>
                        <p class="card-tool-name">Adobe Illustrator</p>
                        <p class="card-tool-category">Design Vetorial & Diagramação Técnica</p>
                    </div>
                </div>
                <p class="card-tool-desc">
                    Criação de diagramas unifilares conceituais, infográficos de fluxos industriais, ilustrações normativas vetoriais e identidade visual para entregáveis de engenharia.
                </p>
            </div>
            <div><span class="badge-tool-tag">Ilustração Técnica</span><span class="badge-tool-tag">Diagramas Vetoriais</span></div>
        </div>
        """, unsafe_allow_html=True)

# --- ABA 4: INDICADORES & PRODUTIVIDADE ---
with tab_analytics:
    st.markdown("### 📊 Indicadores Técnicos & Produtividade Operacional")
    st.markdown("Métricas consolidadas de desempenho, distribuição por disciplina e eficiência técnica.")
    st.write("")
    
    g1_col, g2_col = st.columns(2)
    
    with g1_col:
        st.markdown("""<div class="card-chart-wrapper"><h4>📌 Distribuição por Disciplina Técnica</h4>""", unsafe_allow_html=True)
        
        df_disc_raw = df_projetos['disciplina'].value_counts().reset_index()
        df_disc_raw.columns = ['Disciplina', 'Quantidade']
        
        top_n = 5
        if len(df_disc_raw) > top_n:
            df_top = df_disc_raw.iloc[:top_n].copy()
            outras_qtd = df_disc_raw.iloc[top_n:]['Quantidade'].sum()
            df_outras = pd.DataFrame([{'Disciplina': 'Outras Especialidades', 'Quantidade': outras_qtd}])
            df_chart_disc = pd.concat([df_top, df_outras], ignore_index=True)
        else:
            df_chart_disc = df_disc_raw

        fig_pie = px.pie(
            df_chart_disc,
            values='Quantidade',
            names='Disciplina',
            hole=0.52,
            color_discrete_sequence=['#F37021', '#0F172A', '#EA580C', '#334155', '#FB923C', '#64748B']
        )
        fig_pie.update_traces(
            textposition='inside',
            textinfo='percent',
            insidetextfont=dict(color='#FFFFFF', size=12, family='Montserrat'),
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )
        fig_pie.update_layout(
            template="plotly_white",
            font=dict(family="Montserrat, Inter, sans-serif", color="#0F172A", size=12),
            paper_bgcolor='#FFFFFF',
            plot_bgcolor='#FFFFFF',
            margin=dict(l=10, r=10, t=10, b=60),
            height=320,
            autosize=True,
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.08,
                xanchor="center",
                x=0.5,
                font=dict(color="#0F172A", size=11, family="Montserrat")
            )
        )
        st.plotly_chart(fig_pie, use_container_width=True, theme=None, config=PLOTLY_CONFIG)
        st.markdown('</div>', unsafe_allow_html=True)

    with g2_col:
        st.markdown("""<div class="card-chart-wrapper"><h4>📈 Evolução Histórica de Registros (2018 - 2026)</h4>""", unsafe_allow_html=True)
        
        df_ano_count = df_projetos.groupby('ano').size().reset_index(name='Projetos')
        df_ano_count = df_ano_count.sort_values('ano')
        
        fig_bar_ano = px.bar(
            df_ano_count,
            x='ano',
            y='Projetos',
            text='Projetos',
            color_discrete_sequence=['#F37021']
        )
        fig_bar_ano.update_traces(
            textposition='outside',
            textfont=dict(color="#0F172A", size=13, family="Montserrat"),
            marker=dict(line=dict(color='#C2410C', width=1)),
            cliponaxis=False
        )
        fig_bar_ano.update_layout(
            template="plotly_white",
            font=dict(family="Montserrat, Inter, sans-serif", color="#0F172A", size=12),
            paper_bgcolor='#FFFFFF',
            plot_bgcolor='#FFFFFF',
            margin=dict(l=10, r=10, t=45, b=10),
            height=320,
            autosize=True,
            xaxis=dict(
                tickmode='linear',
                dtick=1,
                title=dict(text="Ano de Emissão", font=dict(color="#0F172A", size=13, family="Montserrat")),
                tickfont=dict(color="#0F172A", size=12, family="Montserrat"),
                showgrid=False,
                linecolor='#94A3B8',
                fixedrange=True
            ),
            yaxis=dict(
                title=dict(text="Quantidade", font=dict(color="#0F172A", size=13, family="Montserrat")),
                tickfont=dict(color="#0F172A", size=12, family="Montserrat"),
                gridcolor='#E2E8F0',
                linecolor='#94A3B8',
                range=[0, 18],
                fixedrange=True
            )
        )
        st.plotly_chart(fig_bar_ano, use_container_width=True, theme=None, config=PLOTLY_CONFIG)
        st.markdown('</div>', unsafe_allow_html=True)

    g3_col, g4_col = st.columns(2)
    
    with g3_col:
        st.markdown("""<div class="card-chart-wrapper"><h4>🏢 Volume por Polo Regional de Atuação</h4>""", unsafe_allow_html=True)
        
        df_cidade_count = df_projetos['cidade'].value_counts().reset_index()
        df_cidade_count.columns = ['Cidade', 'Volume']
        
        fig_cidade = px.bar(
            df_cidade_count.head(6),
            x='Volume',
            y='Cidade',
            orientation='h',
            text='Volume',
            color='Volume',
            color_continuous_scale=['#FFEDD5', '#F37021', '#0F172A']
        )
        fig_cidade.update_traces(
            textposition='outside',
            textfont=dict(color='#0F172A', size=12, family="Montserrat")
        )
        fig_cidade.update_layout(
            template="plotly_white",
            font=dict(family="Montserrat, Inter, sans-serif", color="#0F172A", size=12),
            paper_bgcolor='#FFFFFF',
            plot_bgcolor='#FFFFFF',
            margin=dict(l=140, r=25, t=10, b=10),
            height=280,
            autosize=True,
            yaxis=dict(
                autorange="reversed",
                title=None,
                automargin=True,
                tickfont=dict(color="#0F172A", size=12, family="Montserrat"),
                fixedrange=True
            ),
            xaxis=dict(
                title=dict(text="Documentos Emitidos", font=dict(color="#0F172A", size=13, family="Montserrat")),
                tickfont=dict(color="#0F172A", size=12, family="Montserrat"),
                gridcolor='#E2E8F0',
                linecolor='#94A3B8',
                fixedrange=True
            ),
            coloraxis_showscale=False
        )
        st.plotly_chart(fig_cidade, use_container_width=True, theme=None, config=PLOTLY_CONFIG)
        st.markdown('</div>', unsafe_allow_html=True)

    with g4_col:
        st.markdown("""<div class="card-pro-content"><h4>🎯 Indicadores de Eficiência de Processos</h4>""", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="eff-card-box">
            <div class="eff-card-title">⚡ Otimização de Ciclo Técnico (-25%)</div>
            <p class="eff-card-desc">Redução de <b>25% no lead time</b> de elaboração através de blocos dinâmicos CAD e padronização de famílias BIM.</p>
        </div>
        <div class="eff-card-box" style="border-left-color:#0F172A !important;">
            <div class="eff-card-title">📈 Retorno Operacional (+10%)</div>
            <p class="eff-card-desc">Incremento anual no faturamento pela mitigação rigorosa de retrabalhos e compatibilização em obra.</p>
        </div>
        <div class="eff-card-box" style="border-left-color:#F37021 !important;">
            <div class="eff-card-title">🛡️ Conformidade Legal (100% de Aprovação)</div>
            <p class="eff-card-desc">Aprovação integral em mais de 20 projetos submetidos à concessionária CPFL e Corpo de Bombeiros.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- ABA 5: ACERVO TÉCNICO DE TRTs E PROJETOS (DECRESCENTE) ---
with tab_acervo:
    st.markdown('<div id="acervo"></div>', unsafe_allow_html=True)
    st.markdown("### 📂 Catálogo Oficial de Registros Técnicos (TRTs / ARTs) & Projetos")
    st.caption("Exibição ordenada do mais recente (2026) para o mais antigo (2018).")
    
    f1, f2, f3 = st.columns([1.2, 1.2, 2.5])
    with f1:
        disciplinas = ["Todas"] + sorted(list(df_projetos["disciplina"].dropna().unique()))
        filtro_disc = st.selectbox("Disciplina:", disciplinas)
    with f2:
        anos = ["Todos"] + [str(a) for a in sorted(list(df_projetos["ano"].dropna().unique()), reverse=True)]
        filtro_ano = st.selectbox("Ano:", anos)
    with f3:
        termo = st.text_input("Filtrar por Cliente, Tecnologia, Cidade ou Código:", placeholder="Ex: CPFL, Hospitalar, SPDA, Gás, Mooca, CFT...")
        
    df_show = df_projetos.copy()
    if filtro_disc != "Todas":
        df_show = df_show[df_show["disciplina"] == filtro_disc]
    if filtro_ano != "Todos":
        df_show = df_show[df_show["ano"] == int(filtro_ano)]
    if termo:
        t = termo.lower()
        df_show = df_show[
            df_show["titulo"].str.lower().str.contains(t, na=False) |
            df_show["descricao"].str.lower().str.contains(t, na=False) |
            df_show["cliente_empresa"].str.lower().str.contains(t, na=False) |
            df_show["id_doc"].str.lower().str.contains(t, na=False) |
            df_show["normas_atendidas"].str.lower().str.contains(t, na=False)
        ]
        
    df_show = df_show.sort_values(by=["ano", "id_doc"], ascending=[False, False])
    
    st.write(f"Exibindo **{len(df_show)}** documentos técnicos:")
    
    for _, row in df_show.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="card-pro-content" style="margin-bottom: 12px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <h4 style="margin:0; color:#0F172A;">{row['titulo']}</h4>
                    <span class="badge-cft-tag">{row['conselho']} • {row['id_doc']}</span>
                </div>
                <p style="margin:2px 0 6px 0; color:#475569; font-size:0.88rem;">
                    🏢 <b>Cliente:</b> {row['cliente_empresa']} &nbsp;|&nbsp;
                    📍 <b>Local:</b> {row['cidade']} &nbsp;|&nbsp;
                    ⚙️ <b>Disciplina:</b> {row['disciplina']} &nbsp;|&nbsp;
                    📅 <b>Ano:</b> <b style="color:#F37021;">{row['ano']}</b>
                </p>
                <p style="margin:6px 0 8px 0; font-size:0.93rem; color:#1E293B;">{row['descricao']}</p>
                <span class="badge-norma-tag">📌 Normas: {row['normas_atendidas']}</span>
            </div>
            """, unsafe_allow_html=True)

# --- ABA 6: FORMAÇÃO ACADÊMICA E TÉCNICA ---
with tab_formacao:
    st.markdown("### 🎓 Qualificações Acadêmicas e Formações Técnicas")
    
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        st.markdown("""
        <div class="card-pro-content">
            <h4>🎓 Ensino Superior & Pós-Graduações</h4>
            <ul>
                <li><b>Pós-graduação em Engenharia de Controle e Automação</b> – Faculdade Anhanguera (Concluído 01/2026)</li>
                <li><b>Pós-graduação em Engenharia de Estruturas Metálicas</b> – Faculdade Anhanguera (Concluído 01/2026)</li>
                <li><b>Pós-graduação em Análise de Dados</b> – Faculdade Anhanguera (Concluído 01/2026)</li>
                <li><b>Graduação em Engenharia Mecânica</b> – Universidade Cesumar (Conclusão 12/2026)</li>
                <li><b>MBA em Gestão de Projetos</b> – Faculdade Anhanguera (Concluído 06/2023)</li>
                <li><b>Pós-graduação em Engenharia de Qualidade</b> – Faculdade Anhanguera (Concluído 06/2023)</li>
                <li><b>Tecnólogo em Manutenção Industrial</b> – Universidade Cesumar (Concluído 2023)</li>
                <li><b>Graduação em Engenharia de Produção</b> – UNIVESP (Concluído 2022)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with f_col2:
        st.markdown("""
        <div class="card-pro-content">
            <h4>⚙️ Formações Técnicas (ETEC)</h4>
            <ul>
                <li><b>Técnico em Mecânica (2021)</b> – ETEC Aristóteles Ferreira</li>
                <li><b>Especialização Técnica em Gestão de Projetos (2020)</b> – ETEC Praia Grande</li>
                <li><b>Técnico em Eletrotécnica (2017)</b> – ETEC Aristóteles Ferreira</li>
                <li><b>Técnico em Desenho da Construção Civil (2014)</b> – ETEC Aristóteles Ferreira</li>
                <li><b>Técnico em Edificações (2011)</b> – ETEC Ruth Cardoso</li>
                <li><b>Técnico em Segurança do Trabalho (2009)</b> – ETEC Escolástica Rosa</li>
                <li><b>Técnico em Informática (2008)</b> – ETEC Praia Grande</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="card-pro-content">
        <h4>🌐 Certificações Internacionais & Habilitações</h4>
        <ul>
            <li><b>Certificações:</b> Autodesk Certified User (ACU), Furukawa FCP Professional e Furukawa FCP Master.</li>
            <li><b>Idiomas:</b> Inglês (técnico para leitura), Espanhol (básico).</li>
            <li><b>Habilitação Nacional:</b> CNH Categorias A e B.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 11. FOOTER CORPORATIVO
# -----------------------------------------------------------------------------
st.markdown("""
<div class="footer-pro">
    <div class="footer-title">
        CAIO BARBOSA DOS SANTOS • ENGENHARIA & PROJETOS
    </div>
    <div class="footer-subtitle">
        Responsável Técnico Habilitado • CREA-SP & CFT | São Paulo, SP - Brasil
    </div>
    <div class="footer-copy">
        © 2026 Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)
