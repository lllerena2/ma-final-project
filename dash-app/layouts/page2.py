import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import utils.model as model
import plotly.express as px
import pandas as pd



#df_graph = pd.read_csv("utils/train_rod.csv")
#fig = 

layout_page2 = dbc.Container([
    html.H1("Estimación del ROD"),
    html.P("Ingresa los datos y haz clic en el botón 'Predecir' para obtener una estimación:"),
    dbc.Row([
        dbc.Col([
            html.H5("leak_dia"),
            html.P("Diámetro de la fuga o fisura (pulgadas)"),
            dbc.Input(id="input-x1", placeholder="in", type="number"),
            html.Br(),
            html.H5("pressure"),
            html.P("Presión de entrada al gasoducto (psig)"),
            dbc.Input(id="input-x2", placeholder="psig", type="number"),
            html.Br(),
            html.H5("flow_pipe"),
            html.P("Flujo de entrada al gasoducto (Mpcd)"),
            dbc.Input(id="input-x3", placeholder="mpcd", type="number"),
            dbc.Button("Predecir", id="btn-predict", color="primary", className="mt-3"),
            html.Br(),
            html.Div(id="output-prediction"),
        ], width=6),
        dbc.Col([html.Div(html.Img(src="/assets/imagen.png", className="img-fluid", style={'width': '100%'})),
        ], width=6)
    ])
])

@callback(
    Output('output-prediction', 'children'),
    Input('btn-predict', 'n_clicks'),
    State('input-x1', 'value'),
    State('input-x2', 'value'),
    State('input-x3', 'value'),
    prevent_initial_call=True
)
def update_prediction(n_clicks, x1, x2, x3):
    if n_clicks is None:
        return ""

    # Realizar la predicción utilizando el modelo
    rod = model.predict_rod(x1, x2, x3)
    #flow = model.predict_flow(rod)


    
    return html.Div([
    html.H5("Resultado de la predicción:"),
    html.P(f'El valor esperado de ROD es: {rod} psig/min (RSME=0.95)', style={'font-weight': 'bold'}),
    # dcc.Graph(id='graph-model', figure=fig)
], className="text-center")