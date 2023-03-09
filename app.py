# !!! IF YOU WANT TO RUN DASH, PASTE http://127.0.0.1:8050/ IN WEB BROWSER !!!


from dash import Dash, html, dcc, Input, Output
import pandas as pd
import data_processing as dp
import plotly.express as px
pd.options.plotting.backend = "plotly"

# Datasets
EDU_DF = dp.clean_edu_data()
INCOME_DF = dp.clean_income_data()

# Helpful Global Variables
EDU_RACES = EDU_DF["Race"].sort_values().unique()
EDU_DEGREES = EDU_DF['Attainment Label'].sort_values().unique()

# Create Dash app
app = Dash(__name__)

# Create Dropdown menus
race_dropdown = dcc.Dropdown(options=EDU_RACES, value=EDU_RACES[0],
                             className='dropdown')
degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=EDU_DEGREES[0])

# dcc.Markdown('./README.md')

# Create layout for this page
app.layout = html.Div(children=[
    html.H1(children='Education Attainment Over Time, \
            per Race (in Washington)'),
    race_dropdown,
    dcc.Graph(id='attainment')
], className='whole-page')


# input, output graph 1
@app.callback(
    Output(component_id='attainment', component_property='figure'),
    Input(component_id=race_dropdown, component_property='value')
)
def attainment_over_time(race):
    df = EDU_DF[['Year', 'Race', 'Estimate Population', 'Attainment Label']]
    race_mask = df['Race'] == race
    degree_mask = df['Attainment Label'] != 'Some college, no degree'
    df = df[race_mask & degree_mask]
    df = df.groupby(['Year', 'Attainment Label'],
                    as_index=False)['Estimate Population'].sum()
    chart = px.line(df, x='Year', y='Estimate Population',
                    color='Attainment Label', markers=True)
    return chart


if __name__ == '__main__':
    app.run_server(debug=True)