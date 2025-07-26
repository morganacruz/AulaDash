import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os 

df = pd.DataFrame({
    "Cidade": ["São Paulo", "Rio", "Fortaleza", "São Paulo", "Rio", "Fortaleza"],
    "Mês": ["Jan", "Jan", "Jan", "Fev", "Fev", "Fev"],
    "Vendas": [100, 80, 70, 120, 90, 1000]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Interativo de Vendas"),

    html.Label("Escolha a cidade:"),
    dcc.Dropdown(
        id="dropdown-cidade",
        options=[{"label": c, "value": c} for c in df["Cidade"].unique()],
        value="São Paulo"
    ),

    dcc.Graph(id="grafico-vendas")
])

@app.callback(
    Output("grafico-vendas", "figure"),
    Input("dropdown-cidade", "value")
)
def atualizar_grafico(cidade_selecionada):
    df_filtrado = df[df["Cidade"] == cidade_selecionada]
    fig = px.bar(df_filtrado, x="Mês", y="Vendas", title=f"Vendas em {cidade_selecionada}")
    return fig

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",8050)))

