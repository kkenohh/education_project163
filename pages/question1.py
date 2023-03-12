# Setup
import dash
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import data_processing as dp
import plotly.express as px
pd.options.plotting.backend = "plotly"

dash.register_page(__name__, name='Race vs Degree')

# Datasets
EDU_DF = dp.clean_edu_data()
# INCOME_DF = dp.clean_income_data()

# Helpful Global Variables
EDU_RACES = EDU_DF["Race"].sort_values().unique()
EDU_DEGREES = EDU_DF['Attainment Label'].sort_values().unique()


# Create Dropdown menus
race_dropdown = dcc.Dropdown(options=EDU_RACES, value=EDU_RACES[0],
                             className='dropdown')
degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=EDU_DEGREES[0])

# Create layout for this page
layout = html.Div(children=[
    html.H1(children='Education Attainment Over Time, \
            per Race (in Washington)', className='graph-header'),
    html.Div(children=[
        html.Div([
            race_dropdown,
            dcc.Graph(id='attainment')
        ]),
        dcc.Markdown('''
        # What did we find?

        The thing that stood out the most after looking at the graphs is that
        the majority of most races don't achieve a high school degree.
        ''', className='markdown')
    ], className='question-one')
], className='whole-page')


# input, output graph 1
@callback(
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
