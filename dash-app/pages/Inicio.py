# Libraries
import dash
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from datetime import datetime

from components.others.filters import filter_card
from components.figures.card import Card
from components.figures.bar_chart import BarChart
from components.figures.sunburst import Sunburst
from components.figures.sankey import Sankey
from components.maps.heatmap import Heatmap
from components.dfs.dataframes import df_inicio


dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row(html.H1("Estado general de los PQRS"), style={"text-align": "center"}),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(filter_card(), md=4),
                dbc.Col(
                    [
                        dbc.Row([
                           dbc.Col(Card("Total PQRS", len(df_inicio)).display(),)
                        ]),
                        dbc.Row([
                            dbc.Col(Card("Caracterizadas manualmente", 951).display(),)
                        ]),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Row([
                           dbc.Col(Card("Por caracterizar", 1050).display()),
                        ]),
                        dbc.Row([
                            dbc.Col(Card("Caracterizadas automáticamente", 1725).display(),)
                        ]),
                    ]
                )
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                BarChart(
                                    title='Estado de los PQRS',
                                    x=df_inicio['glb_estado_id'].value_counts(),
                                    y=df_inicio['glb_estado_id'].value_counts().index,
                                    orientation='h',
                                ).display()
                            ],
                            id='id_estado_PQRS'
                        )
                    ],
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                Sunburst(
                                    title='Tiempos de respuesta',
                                    df=df_inicio.groupby(
                                        ['estado_respuesta',
                                         'estado_tiempo']).size().reset_index(name="PQRS"),
                                    path=['estado_respuesta', 'estado_tiempo'],
                                    values='PQRS',
                                    color=None,
                                ).display()
                            ],
                            id='id_tiempo_respuesta'
                        )
                    ],
                    className='h-100',
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                Sankey(
                                    title="PQRS por dependencia vs Estado y Tiempo de Respuesta",
                                    df=df_inicio,
                                    left="glb_dependencia_id",
                                    mid="estado_tiempo",
                                    right="estado_respuesta",
                                    count="amisalud_id",
                                ).display()
                            ],
                            id='id_estado_sankey'
                        )
                    ]
                )
            ]

        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                Heatmap(df=df_inicio,
                                        title='Mapa de calor de los PQRS',
                                        lon=df_inicio['Longitud'],
                                        lat=df_inicio['Latitud'],
                                        ).display()
                            ],
                            id='id_heatmap_PQRS'
                        )
                    ]
                )
            ]
        ),

    ],
    fluid=True,
    style={"padding": "50px 50px 50px 300px",}
)

@callback(
    [Output('id_estado_PQRS', 'children'),
     Output('id_tiempo_respuesta', 'children'),
     Output('id_estado_sankey', 'children'),
     Output('id_heatmap_PQRS', 'children'),
     ],
    [State('id_date', 'start_date'),
     State('id_date', 'end_date'),
     Input("id_filtro", "n_clicks"),
     ],
    # prevent_initial_call=True,
    # suppress_callback_exceptions=True
)
def update_figures(fecha_inicio, fecha_fin, nclicks):
    df_inicio_filtrado = df_inicio.copy()

    # Filtro de fechas
    if fecha_fin is not None:
        fecha_fin = fecha_fin.split('T')[0]
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        df_inicio_filtrado = df_inicio_filtrado.loc[df_inicio_filtrado['fecha_radicacion'] <= fecha_fin]

    if fecha_inicio is not None:
        fecha_inicio = fecha_inicio.split('T')[0]
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        df_inicio_filtrado = df_inicio_filtrado.loc[df_inicio_filtrado['fecha_radicacion'] >= fecha_inicio]

    # Actulizar Estado de PQRS
    nuevo_bar_chart = BarChart(
        title='Estado de los PQRS',
        x=df_inicio_filtrado['glb_estado_id'].value_counts(),
        y=df_inicio_filtrado['glb_estado_id'].value_counts().index,
        orientation='h',
    ).display()

    # Actualizar Tiempos de respuesta
    nuevo_sunburst = Sunburst(
        title='Tiempos de respuesta',
        df=df_inicio_filtrado.groupby(
        ['estado_respuesta',
        'estado_tiempo']).size().reset_index(name="PQRS"),
        path=['estado_respuesta', 'estado_tiempo'],
        values='PQRS',
        color=None,
    ).display()

    # Actualizar gráfico de barras de categoría específica
    nuevo_sankey_inicio = Sankey(
        title="PQRS por dependencia vs Estado y Tiempo de Respuesta",
        df=df_inicio_filtrado,
        left="glb_dependencia_id",
        mid="estado_tiempo",
        right="estado_respuesta",
        count="glb_estado_id",
    ).display()

    nuevo_heatmap = Heatmap(df=df_inicio_filtrado,
                            title='Mapa de calor de los PQRS',
                            lon=df_inicio_filtrado['Longitud'],
                            lat=df_inicio_filtrado['Latitud'],
                            ).display()

    return [
        nuevo_bar_chart,
        nuevo_sunburst,
        nuevo_sankey_inicio,
        nuevo_heatmap
    ]
