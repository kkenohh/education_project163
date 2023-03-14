# Setup
import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import data_processing as dp
import plotly.express as px
import numpy as np
pd.options.plotting.backend = "plotly"

dash.register_page(__name__, name='Education vs Health')

# Datasets
EDU_DF = dp.clean_edu_data()
HEALTH_DF = dp.merge_health()
# Dropdown options
COUNTIES = np.insert(HEALTH_DF['County'].sort_values().unique(), 0,
                     'Select All')

# Create dropdowns
region_dropdown = dcc.Dropdown(options=COUNTIES, value=[],
                               placeholder='Select a Region',
                               className='dropdown-two', multi=True)

# Create layout for this page
layout = html.Div(children=[
    html.H1(children='Education Attainment Over Time, \
            Compared to Health', className='graph-header'),
    html.Div(children=[
        html.Div([
            region_dropdown,
            dcc.Graph(id='graph1')
        ], className='graphs'),
        dcc.Markdown('''
        # What did we find?

        ''', className='markdown')
    ], className='question')
], className='whole-page')

# Top graph
def health_to_county(county):
    '''
    Takes in a list of counties and displays a bar graph showing the
    percentage of people within the given counties that reported a given
    health condition.
    Parameters:

    Returns:
    '''
    df = HEALTH_DF
    display_values = ['Smoking Count', 'Binge Drinking Count',
                      'Poor Mental Health Count', 'Diabetes Count']
    if 'Select All' not in county:
        county_mask = df['County'].isin(list(county))
        df = df[county_mask]
        graph = px.bar(df[county_mask], x='County', y=display_values)
    else:
        graph = px.bar(df, x='County', y=display_values)
    return graph
