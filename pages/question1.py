# Setup
import dash
from dash import html, dcc, Input, Output, callback
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
        ], className='graphs'),
        dcc.Markdown('''
        # What did we find?

        The question we are trying to answer with this graph is:
        **Is there a large disparity between any two degrees? Which ones?
        What could be causing this? Is it different among different races?**

        The thing that stood out the most after looking at the graphs is the
        most prominent degree among all races is "less than high school".
        If you look at each race individually, the line that shows up at the
        top is "less than high school".
        One thing to note is that even though the number of people who attained
        a certain degree is higher in a certain race, we must look at the
        proportion instead of count. The most concerning thing we noticed is
        that Hispanic/Latino have the biggest disparity between "less than
        high school" and the second highest degree attained, a ratio of 10:3
        to the second highest degree. For reference, the ratio for
        White is around 23:21, Asian is 33:28, and Black is 17:11.
        These are all significantly smaller than Hispanic/Latino.

        So we found that the highest degree attained among all races
        is "less than high school", but what is causing the disparity to be
        so large among Hispanic/Latino? My first thought went to immigration.
        Because most Hispanics move to America not knowing much English, they
        probably have a hard time getting work, which leads to lower income,
        and living in poorer neighborhoods. Poorer neighborhoods means worse
        education, and the environment a student is in is a huge factor
        in how well they do in school. If they're poorly influenced by
        peers and teachers don't teach with care and efficiency, they may end
        up dropping out or just never graduating. Along with this, there
        may be pressure to work from a young age in order to support
        their family, which takes away necessary time for studying and
        doing well in school.

        All in all, we found that there is a large disparity between "less
        than high school" and the second highest degree for any given race,
        however, the disparity is much larger among Hispanic/Latino.
        ''', className='markdown')
    ], className='question ')
], className='whole-page')


# input, output graph 1
@callback(
    Output(component_id='attainment', component_property='figure'),
    Input(component_id=race_dropdown, component_property='value'),
    Input(component_id=degree_dropdown, component_property='value')
)
def attainment_over_time(race, degree):
    '''
    Takes a list of races and list of degrees and produces a line plot
    that showing the number of people who achieved a certain education
    level over time grouped by race or degree.
    Parameters:
        race - a list of races
        degree - a list of degrees
    Returns:
        a line plot
    '''
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
                        markers=True, labels={'year': 'Year'})
    else:
        chart = px.line(df, x='year', y='Estimate Population',
                        color='Attainment Label', line_group='Race',
                        markers=True, labels={'year': 'Year'})
    return chart
