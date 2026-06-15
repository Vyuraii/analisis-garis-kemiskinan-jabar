import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Dashboard Garis Kemiskinan Jabar",
    page_icon="📊",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

/* Global Reset & Font */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0a1628 0%, #0d2144 50%, #0a1628 100%);
    min-height: 100vh;
}

/* Hide default Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container padding */
.block-container {
    padding: 1.5rem 2rem !important;
    max-width: 100% !important;
}

/* ===================== HEADER ===================== */
.header-container {
    background: linear-gradient(135deg, #0d2144 0%, #1a3a6e 50%, #0d2144 100%);
    border: 1px solid rgba(100, 160, 255, 0.25);
    border-radius: 16px;
    padding: 1.2rem 2rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}

.header-icon {
    font-size: 2.5rem;
}

.header-title {
    font-size: 1.9rem;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin: 0;
    line-height: 1.1;
}

.header-title span {
    color: #4da6ff;
}

/* ===================== KPI CARDS ===================== */
.kpi-primary {
    background: linear-gradient(135deg, #1a3a6e 0%, #1e4a8a 100%);
    border: 1px solid rgba(100, 160, 255, 0.3);
    border-radius: 14px;
    padding: 1.4rem 1.8rem;
    box-shadow: 0 6px 24px rgba(0,0,0,0.35);
    height: 100%;
}

.kpi-primary .kpi-value {
    font-size: 2.4rem;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}

.kpi-primary .kpi-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #7ab8ff;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.kpi-primary .kpi-sub {
    font-size: 0.95rem;
    color: #4da6ff;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.3rem;
}

.kpi-secondary {
    background: linear-gradient(135deg, #112236 0%, #162d4a 100%);
    border: 1px solid rgba(100, 160, 255, 0.2);
    border-radius: 14px;
    padding: 1.4rem 1.8rem;
    box-shadow: 0 6px 24px rgba(0,0,0,0.3);
    height: 100%;
}

.kpi-secondary .kpi-value {
    font-size: 2.1rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}

.kpi-secondary .kpi-label {
    font-size: 0.8rem;
    font-weight: 600;
    color: #7ab8ff;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.kpi-secondary .kpi-trend {
    color: #4ade80;
    font-size: 1.1rem;
    margin-left: 0.3rem;
}

/* ===================== SECTION CARDS ===================== */
.section-card {
    background: linear-gradient(135deg, #0f1f3d 0%, #132640 100%);
    border: 1px solid rgba(100, 160, 255, 0.18);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 1rem;
}

.section-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: #7ab8ff;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

/* ===================== SIDEBAR ===================== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a1628 0%, #0d2144 100%) !important;
    border-right: 1px solid rgba(100, 160, 255, 0.15) !important;
}

[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stSlider label {
    color: #c5dcff !important;
}

[data-testid="stSidebar"] .sidebar-header {
    background: linear-gradient(135deg, #1a3a6e, #1e4a8a);
    border: 1px solid rgba(100,160,255,0.3);
    border-radius: 10px;
    padding: 0.8rem 1rem;
    margin-bottom: 1rem;
    color: white;
    font-weight: 700;
    font-size: 0.95rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    text-align: center;
}

/* Slider track color */
[data-testid="stSlider"] .st-b4 {
    background-color: #4da6ff !important;
}

/* Multiselect tags */
[data-testid="stMultiSelect"] span[data-baseweb="tag"] {
    background-color: #1a3a6e !important;
    color: #c5dcff !important;
    border: 1px solid rgba(100,160,255,0.3) !important;
}

/* Expander */
[data-testid="stExpander"] {
    background: linear-gradient(135deg, #0f1f3d 0%, #132640 100%) !important;
    border: 1px solid rgba(100, 160, 255, 0.18) !important;
    border-radius: 12px !important;
}

[data-testid="stExpander"] summary {
    color: #c5dcff !important;
    font-weight: 600 !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: #0a1628 !important;
    border: 1px solid rgba(100,160,255,0.2) !important;
    border-radius: 8px !important;
}

/* Warning */
.stAlert {
    background: rgba(255,165,0,0.1) !important;
    border: 1px solid rgba(255,165,0,0.3) !important;
    color: #ffd080 !important;
    border-radius: 8px !important;
}

/* Footer badge */
.footer-badge {
    background: linear-gradient(135deg, #1a3a6e, #1e4a8a);
    border: 1px solid rgba(100,160,255,0.3);
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    text-align: center;
    color: #7ab8ff;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    margin-top: 0.5rem;
}

/* Divider line */
.custom-divider {
    border: none;
    border-top: 1px solid rgba(100, 160, 255, 0.15);
    margin: 1rem 0;
}

/* Table header */
.table-header {
    background: linear-gradient(135deg, #1a3a6e, #1e4a8a);
    border: 1px solid rgba(100,160,255,0.3);
    border-radius: 10px;
    padding: 0.7rem 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.8rem;
}

.table-header-text {
    color: #ffffff;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)


# --- FUNGSI LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("kemiskinan_jabar.csv")
    return df

df = load_data()

# ===================== HEADER =====================
st.markdown("""
<div class="header-container">
    <div class="header-icon">📊</div>
    <div>
        <div class="header-title">Dashboard Analisis <span>Garis Kemiskinan</span> Jawa Barat</div>
    </div>
    <div style="margin-left:auto; font-size:0.78rem; color:#7ab8ff; text-align:right; line-height:1.6;">
        Data BPS • 2004 – 2025<br>
        <span style="color:#4da6ff;">● Live</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
with st.sidebar:
    st.markdown('<div class="sidebar-header">🔍 Filter Data</div>', unsafe_allow_html=True)

    tahun_min = int(df['tahun'].min())
    tahun_max = int(df['tahun'].max())
    pilih_tahun = st.slider("Pilih Rentang Tahun", tahun_min, tahun_max, (2015, tahun_max))

    st.markdown("")
    list_kabkota = sorted(df['nama_kabupaten_kota'].unique().tolist())
    default_kota = [k for k in ["KOTA BANDUNG", "KOTA BOGOR", "KABUPATEN CIREBON", "KOTA BEKASI", "KOTA DEPOK"] if k in list_kabkota]
    pilih_kabkota = st.multiselect(
        "Pilih Kabupaten/Kota",
        list_kabkota,
        default=default_kota if default_kota else list_kabkota[:5]
    )

    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)
    st.markdown('<div class="footer-badge">🏛️ Jawa Barat Data Project</div>', unsafe_allow_html=True)

# ===================== FILTER DATA =====================
df_filtered = df[
    (df['tahun'] >= pilih_tahun[0]) &
    (df['tahun'] <= pilih_tahun[1]) &
    (df['nama_kabupaten_kota'].isin(pilih_kabkota))
]

# ===================== KPI CARDS =====================
if not df_filtered.empty:
    rata_rata = df_filtered['garis_kemiskinan'].mean()
    total_obs = len(df_filtered)

    df_latest = df_filtered[df_filtered['tahun'] == pilih_tahun[1]]
    if not df_latest.empty:
        nilai_max = df_latest['garis_kemiskinan'].max()
        kota_max = df_latest.loc[df_latest['garis_kemiskinan'].idxmax()]['nama_kabupaten_kota']
    else:
        nilai_max = df_filtered['garis_kemiskinan'].max()
        kota_max = df_filtered.loc[df_filtered['garis_kemiskinan'].idxmax()]['nama_kabupaten_kota']

    kpi1, kpi2, kpi3 = st.columns([2, 1, 1])

    with kpi1:
        st.markdown(f"""
        <div class="kpi-primary">
            <div class="kpi-label">Tertinggi Tahun {pilih_tahun[1]}</div>
            <div class="kpi-value">Rp {nilai_max:,.0f}</div>
            <div class="kpi-sub">↑ {kota_max}</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi2:
        st.markdown(f"""
        <div class="kpi-secondary">
            <div class="kpi-label">Rata-Rata</div>
            <div class="kpi-value">Rp {rata_rata:,.0f} <span class="kpi-trend">↗</span></div>
        </div>
        """, unsafe_allow_html=True)

    with kpi3:
        st.markdown(f"""
        <div class="kpi-secondary">
            <div class="kpi-label">Total Data</div>
            <div class="kpi-value">{total_obs} <span class="kpi-trend">↗</span></div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.warning("⚠️ Silakan pilih minimal satu Kabupaten/Kota untuk melihat data.")

st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

# ===================== CHARTS =====================
col_left, col_right = st.columns(2, gap="medium")

# Plotly layout base
plotly_layout = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#c5dcff", family="Inter"),
    margin=dict(l=10, r=10, t=10, b=40),
    legend=dict(
        bgcolor="rgba(10,22,40,0.7)",
        bordercolor="rgba(100,160,255,0.2)",
        borderwidth=1,
        font=dict(color="#c5dcff", size=11)
    ),
    xaxis=dict(
        gridcolor="rgba(100,160,255,0.08)",
        zerolinecolor="rgba(100,160,255,0.1)",
        tickfont=dict(color="#7ab8ff"),
        title_font=dict(color="#7ab8ff")
    ),
    yaxis=dict(
        gridcolor="rgba(100,160,255,0.08)",
        zerolinecolor="rgba(100,160,255,0.1)",
        tickfont=dict(color="#7ab8ff"),
        title_font=dict(color="#7ab8ff")
    )
)

with col_left:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">📈 Trend Garis Kemiskinan Per Tahun</div>
    """, unsafe_allow_html=True)

    if not df_filtered.empty:
        fig_line = px.line(
            df_filtered,
            x='tahun',
            y='garis_kemiskinan',
            color='nama_kabupaten_kota',
            markers=True,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_line.update_traces(line=dict(width=2), marker=dict(size=5))
        fig_line.update_layout(
            **plotly_layout,
            xaxis_title="Tahun",
            yaxis_title="Garis Kemiskinan (Rp/Kapita/Bulan)",
            legend_title="Wilayah",
            hovermode="x unified",
            height=320
        )
        st.plotly_chart(fig_line, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">📊 Perbandingan Antar Wilayah (Tahun {pilih_tahun[1]})</div>
    """, unsafe_allow_html=True)

    if not df_filtered.empty:
        df_bar = df_filtered[df_filtered['tahun'] == pilih_tahun[1]].sort_values(by='garis_kemiskinan', ascending=True)

        fig_bar = go.Figure(go.Bar(
            x=df_bar['nama_kabupaten_kota'],
            y=df_bar['garis_kemiskinan'],
            marker=dict(
                color=df_bar['garis_kemiskinan'],
                colorscale=[[0, '#1a3a6e'], [0.5, '#2563b0'], [1, '#4da6ff']],
                line=dict(color='rgba(100,160,255,0.2)', width=1)
            ),
            text=df_bar['garis_kemiskinan'].apply(lambda x: f"Rp {x/1000:.0f}K"),
            textposition='outside',
            textfont=dict(color='#c5dcff', size=10)
        ))
        fig_bar.update_layout(
            **plotly_layout,
            xaxis_title="Kabupaten/Kota",
            yaxis_title="Garis Kemiskinan (Rp)",
            height=320,
        )
        fig_bar.update_xaxes(
            tickangle=-40,
            tickfont=dict(color="#7ab8ff", size=9),
            gridcolor="rgba(100,160,255,0.08)",
            zerolinecolor="rgba(100,160,255,0.1)",
            title_font=dict(color="#7ab8ff")
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===================== TABEL DATA =====================
st.markdown("""
<div class="table-header">
    <span>📋</span>
    <span class="table-header-text">Detail Data Mentah (Representasi Data Raw)</span>
</div>
""", unsafe_allow_html=True)

with st.expander("Klik di sini untuk melihat atau menyalin tabel data lengkap"):
    if not df_filtered.empty:
        df_display = df_filtered.copy()
        df_display['garis_kemiskinan'] = df_display['garis_kemiskinan'].apply(lambda x: f"Rp {x:,.0f}")
        st.dataframe(
            df_display.reset_index(drop=True),
            use_container_width=True,
            height=280
        )
    else:
        st.info("Tidak ada data untuk ditampilkan.")