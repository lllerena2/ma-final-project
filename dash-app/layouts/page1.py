import dash_bootstrap_components as dbc
from dash import html

layout_page1 = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H4("Oportunidad:"),
            html.P([
                "El problema propuesto busca explicar y predecir el Rate of Drop (ROD) de la presión ",
                "en gasoductos. Entender y calibrar este parámetro es crucial para la garantizar la seguridad y continuidad de la operación."
            ]),
            html.P([
                "Para esto se analizan relaciones entre variables como el ",
                html.Strong("diámetro de una escape, distancia hasta el punto de medición, presión de entrada, flujo a través de la tubería, ROD, flujo de fuga")
            ]),
            html.H4("Objetivo:"),
            html.P([
                "Establecer valores adecuados de ROD para configurar protecciones en las líneas de transporte.",
                "Contar con una herramienta como esta permite responder preguntas específicas sobre la detección de fugas, robusteciendo la continuidad de la operación y ",
                " reduciendo su impacto ambiental"
            ]),
            html.H4("Resultados:"),
            html.P([
                "Se exploraron los datos utilizandos diferentes tecnicas como clusterización y correlación. Además, se evaluaron ",
                html.Strong("modelos de regresión lineal (diferentres restricciones y grados), árboles de regresión, bosques aleatorios de regresión y SVR. "),
                "Con lo obtenido, es posible generalizar y preveer el ROD en diferentes escenarios, con un error medio de 0.95 psig/min (RMSE)",
            ]),
            html.H6("Integrantes: Andrés Correa - Luis llerena"),
            html.H6("Modelos analíticos"),
        ], width=6),
        dbc.Col([
            html.Img(src="/assets/mapa-gas.png", className="img-fluid", style={'width': '100%'}),  # Aquí se ajusta el tamaño de la imagen
            html.Img(src="/assets/rod.png", className="img-fluid", style={'width': '100%'})
        ], width=6)
    ])
])
