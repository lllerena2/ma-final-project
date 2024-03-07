import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State

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

@callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is not None:
        # Cargar los datos del archivo
        df = parse_data(contents, filename)
        return html.Div([
            html.H5(filename),
            html.Hr(),
            dbc.Button("Procesar Datos", id="btn-process-data", color="primary", className="mt-3")
        ])

@callback(
    Output('output-prediction-batch', 'children'),
    Input('btn-process-data', 'n_clicks'),
    State('output-data-upload', 'children')
)
def process_data(n_clicks, data_upload):
    if n_clicks is not None:
        # Realizar las predicciones por lotes
        predictions = model.predict_batch(df)

        # Agregar las predicciones al DataFrame
        df['prediction'] = predictions

        # Generar un archivo CSV con las predicciones
        csv_data = df.to_csv(index=False)

        # Crear un objeto de descarga para el archivo CSV
        csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_data)
        return html.Div([
            html.A('Descargar Predicciones',
                   id='download-predictions',
                   download="predicciones.csv",
                   href=csv_string,
                   target="_blank")
        ])