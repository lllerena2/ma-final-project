import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import utils.model as model

layout_page2 = dbc.Container([
    html.H1("Predicción Manual"),
    html.P("Ingresa los valores de entrada para obtener una predicción:"),
    dbc.Row([
        dbc.Col([
            html.H5("Variable X1"),
            html.P("Descripción de la variable X1"),
            dbc.Input(id="input-x1", placeholder="Valor de X1", type="number"),
            html.Br(),
            html.H5("Variable X2"),
            html.P("Descripción de la variable X2"),
            dbc.Input(id="input-x2", placeholder="Valor de X2", type="number"),
            html.Br(),
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

@callback(
    Output('output-prediction', 'children'),
    Input('btn-predict', 'n_clicks'),
    State('input-x1', 'value'),
    State('input-x2', 'value'),
    State('input-x3', 'value'),
    State('graph-model', 'figure')
)
def update_prediction(n_clicks, x1, x2, x3, figure):
    if n_clicks is None:
        return "Haz clic en el botón 'Predecir' para obtener una predicción"

    # Realizar la predicción utilizando el modelo
    prediction = model.predict(x1, x2, x3)

    # Actualizar la gráfica del modelo (por ahora, solo un ejemplo)
    # figure['data'][0]['y'] = [x1, x2, x3]
    
    return html.Div([
    html.H5("Resultado de la predicción"),
    html.P(f'El grupo predicho es: {prediction}', style={'font-weight': 'bold'})
], className="text-center")