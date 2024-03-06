import dash_bootstrap_components as dbc
from dash import dcc, html

layout_page3 = dbc.Container([
    html.H1("Predicción por Lotes"),
    html.P("Sube un archivo CSV o Excel con los datos de entrada para obtener las predicciones:"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Arrastra y suelta o ',
            html.A('selecciona un archivo')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-data-upload'),
    dbc.Button("Procesar Datos", id="btn-process-data", color="primary", className="mt-3"),
    html.Div(id='output-prediction-batch'),
    dbc.Button("Descargar Predicciones", id="btn-download-predictions", color="success", className="mt-3")
])