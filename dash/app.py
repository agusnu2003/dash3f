import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Inicializa la aplicación
app = dash.Dash(__name__)

# Datos de ejemplo
df = px.data.gapminder()

# Gráfico de ejemplo
fig = px.line(df[df['continent'] == 'Europe'], x='year', y='gdpPercap', color='country')

# Layout del dashboard
app.layout = html.Div(
    style={'backgroundColor': '#1e1e2e', 'padding': '20px'},
    children=[
        html.H1(
            children='Dashboard Elegante en Naranja',
            style={
                'textAlign': 'center',
                'color': '#ffa500'
            }
        ),
        html.Div(
            children='Este es un dashboard simple utilizando Dash y Plotly.',
            style={
                'textAlign': 'center',
                'color': '#ffffff'
            }
        ),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ]
)

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
