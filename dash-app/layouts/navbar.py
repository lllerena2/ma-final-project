import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href="/")),
        dbc.NavItem(dbc.NavLink("Modelo", href="/page2")),
        dbc.NavItem(dbc.NavLink("Predicción", href="/page3")),
    ],
    brand="ROD en Gasoductos",
    brand_href="/",
    color="primary",
    dark=True,
)