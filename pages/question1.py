# Setup
import dash
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import data_processing as dp
import plotly.express as px
import numpy as np
pd.options.plotting.backend = "plotly"

dash.register_page(__name__, name='Race vs Degree')

# Datasets
EDU_DF = dp.clean_edu_data()
# INCOME_DF = dp.clean_income_data()

# Helpful Global Variables
EDU_RACES = np.insert(EDU_DF["Race"].sort_values().unique(), 0, 'Select All')
EDU_DEGREES = np.insert(EDU_DF['Attainment Label'].sort_values().unique(),
                        0, 'Select All')


# Create Dropdown menus
race_dropdown = dcc.Dropdown(options=EDU_RACES, value=[],
                             placeholder='Select a Race',
                             className='dropdown', multi=True)
degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=[],
                               placeholder='Select a Degree',
                               className='dropdown', multi=True)

# Create layout for this page
layout = html.Div(children=[
    html.H1(children='Education Attainment Over Time, \
            per Race (in Washington)', className='graph-header'),
    html.Div(children=[
        html.Div([
            html.Div([
                race_dropdown,
                degree_dropdown
            ], className='dropdowns'),
            dcc.Graph(id='attainment')
        ]),
        dcc.Markdown('''
        # What did we find?

        The thing that stood out the most after looking at the graphs is the
        most prominent degree among all races is less than high school. One thing to note is that while
        white has a really high number of people who have less than high school, the proportion of those
        people vs those who have a high school diploma are similar to the other races. The most concerning
        thing about the graphs is that Hispanic/Latino have a the biggest disparity between "less than
        high school" and any degree higher than that, averaging a gap of around 700k people.
        ''', className='markdown')
    ], className='question-one')
], className='whole-page')


# input, output graph 1
@callback(
    Output(component_id='attainment', component_property='figure'),
    Input(component_id=race_dropdown, component_property='value'),
    Input(component_id=degree_dropdown, component_property='value')
)
def attainment_over_time(race, degree):
    df = EDU_DF[['year', 'Race', 'Estimate Population', 'Attainment Label']]
    if 'Select All' not in race:
        race_mask = df['Race'].isin(list(race))
        df = df[race_mask]
    if 'Select All' not in degree:
        degree_mask = df['Attainment Label'].isin(list(degree))
        df = df[degree_mask]
    df = df.groupby(['year', 'Attainment Label', 'Race'],
                    as_index=False)['Estimate Population'].sum()
    if 'Select All' in race:
        chart = px.line(df, x='year', y='Estimate Population',
                        color='Race', line_group='Attainment Label',
                        markers=True)
    else:
        chart = px.line(df, x='year', y='Estimate Population',
                        color='Attainment Label', line_group='Race',
                        markers=True)
    return chart
