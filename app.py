# !!! IF YOU WANT TO RUN DASH, PASTE http://127.0.0.1:8050/ IN WEB BROWSER !!!

from dash import Dash, html, dcc, Input, Output
import dash
import pandas as pd
import data_processing as dp
import plotly.express as px
pd.options.plotting.backend = "plotly"


# Create Dash app
app = Dash(__name__, use_pages=True)

app.layout = html.Div(children=[
    html.H1('Welcome to our mini website!'),
    html.Div(children=[
        dcc.Link(f"{page['name']}", href=page['relative_path'],
                 className='nav-buttons')
        for page in dash.page_registry.values()
    ], className='navbar'),
    dash.page_container
], className='whole-page')

# dcc.Markdown('./README.md')


if __name__ == '__main__':
    app.run_server(debug=True)