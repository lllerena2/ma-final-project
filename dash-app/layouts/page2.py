import dash_bootstrap_components as dbc
from dash import dcc, html

layout_page2 = dbc.Container([
    html.H1("Predicción Manual"),
    html.P("Ingresa los valores de entrada para obtener una predicción:"),
    dbc.Row([
        dbc.Col([
            html.H5("Variable X1"),
            html.P("Descripción de la variable X1"),
            dbc.Input(id="input-x1", placeholder="Valor de X1", type="number"),
            html.H5("Variable X2"),
            html.P("Descripción de la variable X2"),
            dbc.Input(id="input-x2", placeholder="Valor de X2", type="number"),
            html.H5("Variable X3"),
            html.P("Descripción de la variable X3"),
            dbc.Input(id="input-x3", placeholder="Valor de X3", type="number"),
            dbc.Button("Predecir", id="btn-predict", color="primary", className="mt-3")
        ], width=6),
        dbc.Col([
            html.Div(id="output-prediction"),
            dcc.Graph(id="graph-model")
        ], width=6)
    ])
])