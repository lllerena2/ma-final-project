import dash
import dash_bootstrap_components as dbc
from dash import html


dash.register_page(__name__, path="/404")

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(className='bi bi-emoji-frown'),
                        dbc.Row(["404"], className= "flex-fill bigtextgray"),
                        dbc.Row(["Where is my dash?"], className= "flex-fill ")
                    ],
                className="d-flex display-4 align-self-center flex-column"),
            ]
        )
    ],
    style={
        "padding": "50px 50px 50px 300px",
    }
)
