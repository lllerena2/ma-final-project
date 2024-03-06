import dash
import dash_bootstrap_components as dbc
from dash import Output, Input, html
import dash_core_components as dcc


# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Importar los layouts de las páginas
from layouts.page1 import layout_page1
from layouts.page2 import layout_page2
from layouts.page3 import layout_page3
from layouts.navbar import navbar

# Definir el layout principal de la aplicación
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # Agrega este componente
    navbar,
    dbc.Container(id='page-content', className='mt-4')
])

# Callback para actualizar el contenido de la página
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/':
        return layout_page1
    elif pathname == '/page2':
        return layout_page2
    elif pathname == '/page3':
        return layout_page3
    # Si la ruta no coincide, redirigir a la página de inicio
    return layout_page1

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)