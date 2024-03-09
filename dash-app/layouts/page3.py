import base64
import io
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import urllib
import utils.model as model

# Definir la función para cargar los datos del archivo
def parse_data(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Leer archivo CSV
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    elif 'xlsx' in filename:
        # Leer archivo Excel
        df = pd.read_excel(io.BytesIO(decoded))
    return df

# Definir el layout de la página 3
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
    dcc.Store(id='data-store'),
])

# Callback para actualizar la salida después de cargar el archivo
@callback(
    [Output('output-data-upload', 'children'),
     Output('data-store', 'data')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_output(contents, filename):
    if contents is not None:
        # Cargar los datos del archivo
        df = parse_data(contents, filename)
        return [html.Div([
            html.H5(filename),
            html.Hr(),
        ]), df.to_dict('records')]

# Callback para procesar los datos y realizar las predicciones
@callback(
    Output('output-prediction-batch', 'children'),
    [Input('btn-process-data', 'n_clicks')],
    [State('data-store', 'data')]
)
def process_data(n_clicks, data):
    if n_clicks is not None and data is not None:

        df = pd.DataFrame.from_dict(data)
        
        df['ROD'] = model.predict_rod_batch(df)

        csv_data = df.to_csv(index=False)

        # Crear un objeto de descarga para el archivo CSV
        csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_data)
        return html.Div([
            html.A(dbc.Button("Descargar Predicciones", id="btn-download-predictions", color="success", className="mt-3"),
                   id='download-predictions',
                   download="predicciones_rod.csv",
                   href=csv_string,
                   target="_blank")
        ])
