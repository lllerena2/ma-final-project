import dash_bootstrap_components as dbc
from dash import html

layout_page1 = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Bienvenido a Mi Aplicación Dash"),
            html.P("Esta es una descripción del problema y del modelo xyz"),
            html.P("En esta aplicación podrás hacer predicciones manuales y por lotes."),
        ], width=8),
        dbc.Col([
            html.Img(src="/assets/image.png", className="img-fluid")
        ], width=4)
    ])
])