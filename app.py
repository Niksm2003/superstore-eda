import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Superstore Sales Intelligence",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    letter-spacing: -0.01em;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

/* ── Backgrounds ── */
[data-testid="stAppViewContainer"] { background: #0a0a14; }
.main { background: #0a0a14; }

/* ── Hide sidebar completely ── */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }

/* ── Top filter bar ── */
.filter-bar {
    background: #0f0f1e;
    border: 1px solid #1e1e32;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    flex-wrap: wrap;
}
.filter-brand {
    font-size: 0.95rem;
    font-weight: 700;
    color: #c8c8e8;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    white-space: nowrap;
    padding-right: 1.5rem;
    border-right: 1px solid #1e1e32;
}
.filter-label {
    font-size: 0.62rem;
    font-weight: 600;
    color: #6868a0;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin-bottom: 0.3rem;
}

/* ── Multiselect tags — dark subtle style ── */
span[data-baseweb="tag"] {
    background-color: #1a1a30 !important;
    border: 1px solid #2a2a48 !important;
    border-radius: 5px !important;
}
span[data-baseweb="tag"] span {
    color: #9090c0 !important;
    font-size: 11px !important;
    font-weight: 500 !important;
}
span[data-baseweb="tag"] button { color: #444466 !important; }
[data-baseweb="select"] > div {
    background-color: #0f0f1e !important;
    border-color: #1e1e32 !important;
    min-width: 160px !important;
}
[data-baseweb="popover"] { background-color: #0f0f1e !important; }
[data-baseweb="menu"]    { background-color: #0f0f1e !important; }
[data-baseweb="option"]  { background-color: #0f0f1e !important; color: #9090c0 !important; }
[data-baseweb="option"]:hover { background-color: #1a1a30 !important; }

/* ── Page header ── */
.ph { border-bottom: 1px solid #1e1e32; padding-bottom: 1.1rem; margin-bottom: 1.8rem; }
.ph-title {
    font-size: 1.55rem; font-weight: 700;
    color: #d8d8f0; letter-spacing: -0.03em; margin-bottom: 0.3rem;
}
.ph-meta {
    font-size: 0.68rem; color: #6868a0;
    font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase;
}

/* ── Section label ── */
.sl {
    font-size: 0.62rem; font-weight: 600; color: #6868a0;
    text-transform: uppercase; letter-spacing: 0.18em;
    margin-bottom: 1rem; margin-top: 2.2rem;
    padding-bottom: 0.6rem; border-bottom: 1px solid #1e1e32;
}

/* ── KPI cards ── */
.kc {
    background: #0f0f1e; border: 1px solid #1e1e32;
    border-radius: 12px; padding: 1.4rem 1.5rem;
}
.kc-tag {
    font-size: 0.62rem; font-weight: 600; color: #6868a0;
    text-transform: uppercase; letter-spacing: 0.16em; margin-bottom: 0.7rem;
}
.kc-val { font-size: 1.75rem; font-weight: 700; letter-spacing: -0.04em; line-height: 1; }
.kc-sub { font-size: 0.66rem; color: #6060a0; margin-top: 0.45rem; }
.c-blue  { color: #7c83fd; }
.c-green { color: #2dd4aa; }
.c-slate { color: #8899bb; }
.c-amber { color: #e8b84b; }

/* ── Insight box ── */
.ib {
    background: #0f0f1e; border: 1px solid #1e1e32;
    border-left: 3px solid #3d3d7a; border-radius: 8px;
    padding: 0.9rem 1.1rem; margin: 0.8rem 0;
    font-size: 0.82rem; color: #7070a8; line-height: 1.75;
}
.ib strong { color: #9090c0; font-weight: 600; }

.rule { height: 1px; background: #1e1e32; margin: 2.5rem 0 1.5rem; }
.foot {
    text-align: center; font-size: 0.62rem; color: #404060;
    text-transform: uppercase; letter-spacing: 0.12em; padding-top: 1rem;
}
.foot a { color: #505080; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── Chart layout ─────────────────────────────────────────────────────────────
LABEL = "#a0a0cc"

def cl(**kw):
    base = dict(
        paper_bgcolor="#0f0f1e", plot_bgcolor="#0f0f1e",
        font=dict(family="Inter", color="#8080b0", size=11),
        title_font=dict(family="Inter", color="#a0a0c8", size=12),
        xaxis=dict(gridcolor="#1e1e32", linecolor="#1e1e32",
                   zerolinecolor="#1e1e32", tickfont=dict(color="#7878b0", size=11)),
        yaxis=dict(gridcolor="#1e1e32", linecolor="#1e1e32",
                   zerolinecolor="#1e1e32", tickfont=dict(color="#7878b0", size=11)),
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="#1e1e32",
                    font=dict(color="#8080b0", size=11)),
        margin=dict(t=45, b=35, l=40, r=20),
        colorway=["#7c83fd","#2dd4aa","#e8b84b","#f87171","#a78bfa","#38bdf8"]
    )
    base.update(kw)
    return base

C = dict(
    blue="#7c83fd", green="#2dd4aa",
    amber="#e8b84b", rose="#f87171",
    violet="#a78bfa", cyan="#38bdf8"
)

# ── Load data ────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")
    df["Order Date"]    = pd.to_datetime(df["Order Date"])
    df["Ship Date"]     = pd.to_datetime(df["Ship Date"])
    df["Year"]          = df["Order Date"].dt.year
    df["Month"]         = df["Order Date"].dt.to_period("M").astype(str)
    df["Profit Margin"] = (df["Profit"] / df["Sales"] * 100).round(2)
    df["Days to Ship"]  = (df["Ship Date"] - df["Order Date"]).dt.days
    return df

df = load_data()

# ── Top filter bar ────────────────────────────────────────────────────────────
st.markdown('<div class="filter-brand">Sales Intelligence</div>', unsafe_allow_html=True)

col_r, col_c, col_y, col_space = st.columns([1, 1, 1, 2])

with col_r:
    st.markdown('<div class="filter-label">Region</div>', unsafe_allow_html=True)
    regions = st.multiselect("Region", df["Region"].unique(),
                             default=df["Region"].unique(),
                             label_visibility="collapsed")
with col_c:
    st.markdown('<div class="filter-label">Product Category</div>', unsafe_allow_html=True)
    categories = st.multiselect("Category", df["Category"].unique(),
                                default=df["Category"].unique(),
                                label_visibility="collapsed")
with col_y:
    st.markdown('<div class="filter-label">Year</div>', unsafe_allow_html=True)
    years = st.multiselect("Year", sorted(df["Year"].unique()),
                           default=sorted(df["Year"].unique()),
                           label_visibility="collapsed")

st.markdown('<div class="rule"></div>', unsafe_allow_html=True)

filtered = df[
    df["Region"].isin(regions) &
    df["Category"].isin(categories) &
    df["Year"].isin(years)
]

tot_orders    = filtered["Order ID"].nunique()
tot_customers = filtered["Customer ID"].nunique()
tot_states    = filtered["State"].nunique()
yr_min = int(filtered["Year"].min()) if len(filtered) else "-"
yr_max = int(filtered["Year"].max()) if len(filtered) else "-"

# ── Page header ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ph">
  <div class="ph-title">Sales Performance Dashboard</div>
  <div class="ph-meta">
    {tot_orders:,} orders &nbsp;&middot;&nbsp;
    {tot_customers:,} customers &nbsp;&middot;&nbsp;
    {tot_states} states &nbsp;&middot;&nbsp;
    {yr_min} &ndash; {yr_max}
  </div>
</div>""", unsafe_allow_html=True)

# ════════ KPIs ════════
st.markdown('<div class="sl">Key Metrics</div>', unsafe_allow_html=True)

tot_sales  = filtered["Sales"].sum()
tot_profit = filtered["Profit"].sum()
avg_margin = filtered["Profit Margin"].mean()
p_ratio    = (tot_profit / tot_sales * 100) if tot_sales else 0

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="kc"><div class="kc-tag">Total Revenue</div>'
                f'<div class="kc-val c-blue">${tot_sales:,.0f}</div>'
                f'<div class="kc-sub">All selected filters</div></div>',
                unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="kc"><div class="kc-tag">Net Profit</div>'
                f'<div class="kc-val c-green">${tot_profit:,.0f}</div>'
                f'<div class="kc-sub">Profit ratio &nbsp;{p_ratio:.1f}%</div></div>',
                unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="kc"><div class="kc-tag">Total Orders</div>'
                f'<div class="kc-val c-slate">{tot_orders:,}</div>'
                f'<div class="kc-sub">Unique order records</div></div>',
                unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="kc"><div class="kc-tag">Avg Profit Margin</div>'
                f'<div class="kc-val c-amber">{avg_margin:.1f}%</div>'
                f'<div class="kc-sub">Across all product lines</div></div>',
                unsafe_allow_html=True)

# ════════ Category Performance ════════
st.markdown('<div class="sl">Category Performance</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.6])

with col1:
    cat = filtered.groupby("Category").agg(
        Sales=("Sales","sum"), Profit=("Profit","sum")
    ).reset_index().sort_values("Sales", ascending=False)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Revenue", x=cat["Category"], y=cat["Sales"],
        marker_color=C["blue"], marker_line_width=0,
        text=cat["Sales"].apply(lambda x: f"${x/1000:.0f}K"),
        textposition="outside", textfont=dict(color=LABEL, size=11)
    ))
    fig.add_trace(go.Bar(
        name="Profit", x=cat["Category"], y=cat["Profit"],
        marker_color=C["green"], marker_line_width=0,
        text=cat["Profit"].apply(lambda x: f"${x/1000:.0f}K"),
        textposition="outside", textfont=dict(color=LABEL, size=11)
    ))
    fig.update_layout(**cl(
        title="Revenue vs Profit by Category",
        barmode="group", bargap=0.25,
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1, bgcolor="rgba(0,0,0,0)",
                    bordercolor="#1e1e32", font=dict(color="#8080b0", size=11))
    ))
    st.plotly_chart(fig, width="stretch")

with col2:
    sub = filtered.groupby("Sub-Category")["Sales"].sum().reset_index().sort_values("Sales")
    fig = px.bar(
        sub, x="Sales", y="Sub-Category", orientation="h",
        color="Sales",
        color_continuous_scale=["#12122a","#3d3d9a","#7c83fd"],
        text=sub["Sales"].apply(lambda x: f"${x/1000:.0f}K")
    )
    fig.update_traces(textposition="outside", textfont=dict(color=LABEL, size=10))
    fig.update_layout(**cl(
        title="Revenue by Sub-Category",
        coloraxis_showscale=False,
        yaxis=dict(gridcolor="#1e1e32", linecolor="#1e1e32",
                   zerolinecolor="#1e1e32", tickfont=dict(color="#9090c0", size=11),
                   title=None),
        margin=dict(t=45, b=20, l=130, r=80)
    ))
    st.plotly_chart(fig, width="stretch")

# ════════ Regional Analysis ════════
st.markdown('<div class="sl">Regional Analysis</div>', unsafe_allow_html=True)

reg = filtered.groupby("Region").agg(
    Sales=("Sales","sum"), Profit=("Profit","sum")
).reset_index()

col1, col2, col3 = st.columns([1.2, 1, 1])

with col1:
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Revenue", x=reg["Region"], y=reg["Sales"],
        marker_color=C["blue"], marker_line_width=0
    ))
    fig.add_trace(go.Bar(
        name="Profit", x=reg["Region"], y=reg["Profit"],
        marker_color=C["green"], marker_line_width=0
    ))
    fig.update_layout(**cl(
        title="Revenue and Profit by Region", barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1, bgcolor="rgba(0,0,0,0)",
                    bordercolor="#1e1e32", font=dict(color="#8080b0", size=11))
    ))
    st.plotly_chart(fig, width="stretch")

with col2:
    fig = px.pie(reg, names="Region", values="Sales",
                 color_discrete_sequence=[C["blue"],C["violet"],C["rose"],C["cyan"]],
                 hole=0.6)
    fig.update_traces(
        textposition="outside", textinfo="percent+label",
        textfont=dict(color="#a0a0cc", size=10),
        marker=dict(line=dict(color="#0a0a14", width=2))
    )
    fig.update_layout(**cl(title="Revenue Share by Region", showlegend=False))
    st.plotly_chart(fig, width="stretch")

with col3:
    seg = filtered.groupby("Segment")["Sales"].sum().reset_index()
    fig = px.pie(seg, names="Segment", values="Sales",
                 color_discrete_sequence=[C["green"],C["amber"],C["rose"]],
                 hole=0.6)
    fig.update_traces(
        textposition="outside", textinfo="percent+label",
        textfont=dict(color="#a0a0cc", size=10),
        marker=dict(line=dict(color="#0a0a14", width=2))
    )
    fig.update_layout(**cl(title="Revenue by Customer Segment", showlegend=False))
    st.plotly_chart(fig, width="stretch")

best_rev    = reg.loc[reg["Sales"].idxmax(), "Region"]
best_profit = reg.loc[reg["Profit"].idxmax(), "Region"]
st.markdown(f"""<div class="ib">
The <strong>{best_rev}</strong> region leads in total revenue generation.
The <strong>{best_profit}</strong> region delivers the highest absolute profit,
indicating stronger margin discipline or a more favourable product mix in that market.
</div>""", unsafe_allow_html=True)

# ════════ Monthly Trend ════════
st.markdown('<div class="sl">Sales Trend</div>', unsafe_allow_html=True)

monthly = filtered.groupby("Month").agg(
    Sales=("Sales","sum"), Profit=("Profit","sum")
).reset_index()

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=monthly["Month"], y=monthly["Sales"],
    name="Revenue", mode="lines+markers",
    line=dict(color=C["blue"], width=2),
    marker=dict(size=4, color=C["blue"]),
    fill="tozeroy", fillcolor="rgba(124,131,253,0.06)"
))
fig.add_trace(go.Scatter(
    x=monthly["Month"], y=monthly["Profit"],
    name="Profit", mode="lines+markers",
    line=dict(color=C["green"], width=1.5, dash="dot"),
    marker=dict(size=4, color=C["green"])
))
fig.update_layout(**cl(
    title="Monthly Revenue and Profit",
    xaxis_tickangle=45, height=360,
    legend=dict(orientation="h", yanchor="bottom", y=1.02,
                xanchor="right", x=1, bgcolor="rgba(0,0,0,0)",
                bordercolor="#1e1e32", font=dict(color="#8080b0", size=11))
))
st.plotly_chart(fig, width="stretch")

# ════════ Product & Discount ════════
st.markdown('<div class="sl">Product Performance and Discount Impact</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    top10 = (filtered.groupby("Product Name")["Profit"].sum()
             .reset_index().sort_values("Profit", ascending=False).head(10))
    fig = px.bar(
        top10, x="Profit", y="Product Name", orientation="h",
        color="Profit",
        color_continuous_scale=["#0d1c14","#065f46","#2dd4aa"],
        text=top10["Profit"].apply(lambda x: f"${x:,.0f}")
    )
    fig.update_traces(textposition="outside", textfont=dict(color=LABEL, size=10))
    fig.update_layout(**cl(
        title="Top 10 Products by Profit",
        coloraxis_showscale=False,
        yaxis=dict(gridcolor="#1e1e32", linecolor="#1e1e32",
                   zerolinecolor="#1e1e32",
                   tickfont=dict(color="#9090c0", size=10),
                   categoryorder="total ascending", title=None),
        margin=dict(t=45, b=20, l=220, r=80), height=400
    ))
    st.plotly_chart(fig, width="stretch")

with col2:
    fig = px.scatter(
        filtered, x="Discount", y="Profit",
        color="Category", size="Sales",
        color_discrete_map={
            "Furniture":       C["blue"],
            "Office Supplies": C["green"],
            "Technology":      C["violet"]
        },
        opacity=0.5,
        hover_data=["Product Name","Region","Sales"]
    )
    fig.update_layout(**cl(
        title="Discount Rate vs Profit Impact",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1, bgcolor="rgba(0,0,0,0)",
                    bordercolor="#1e1e32", font=dict(color="#8080b0", size=11)),
        height=400
    ))
    st.plotly_chart(fig, width="stretch")

high_disc = filtered[filtered["Discount"] > 0.3]
loss_pct  = (high_disc["Profit"] < 0).mean() * 100
st.markdown(f"""<div class="ib">
Orders carrying a discount above 30% result in a net loss <strong>{loss_pct:.0f}%</strong> of the time.
Aggressive discounting is most prevalent in the <strong>Furniture</strong> category
and represents the primary driver of margin erosion across the portfolio.
</div>""", unsafe_allow_html=True)

# ════════ Shipping ════════
st.markdown('<div class="sl">Shipping Analysis</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    ship = (filtered.groupby("Ship Mode")["Sales"].sum()
            .reset_index().sort_values("Sales", ascending=False))
    fig = px.bar(
        ship, x="Ship Mode", y="Sales",
        color="Ship Mode",
        color_discrete_sequence=[C["blue"],C["violet"],C["rose"],C["amber"]],
        text=ship["Sales"].apply(lambda x: f"${x/1000:.0f}K")
    )
    fig.update_traces(textposition="outside", textfont=dict(color=LABEL, size=11))
    fig.update_layout(**cl(title="Revenue by Shipping Mode", showlegend=False))
    st.plotly_chart(fig, width="stretch")

with col2:
    ship_days = filtered.groupby("Ship Mode")["Days to Ship"].mean().reset_index()
    ship_days.columns = ["Ship Mode","Avg Days to Ship"]
    fig = px.bar(
        ship_days, x="Ship Mode", y="Avg Days to Ship",
        color="Avg Days to Ship",
        color_continuous_scale=["#2dd4aa","#e8b84b","#f87171"],
        text=ship_days["Avg Days to Ship"].apply(lambda x: f"{x:.1f} days")
    )
    fig.update_traces(textposition="outside", textfont=dict(color=LABEL, size=11))
    fig.update_layout(**cl(
        title="Average Fulfilment Time by Shipping Mode",
        coloraxis_showscale=False
    ))
    st.plotly_chart(fig, width="stretch")

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown('<div class="rule"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="foot">
  Prepared by &nbsp;<strong style="color:#505080;">Nikhil Mishra</strong>
  &nbsp;&middot;&nbsp;
  <a href="https://github.com/Niksm2003" target="_blank">github.com/Niksm2003</a>
</div>""", unsafe_allow_html=True)
