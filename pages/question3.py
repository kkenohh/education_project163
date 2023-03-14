# Setup
import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import data_processing as dp
import plotly.express as px
import numpy as np
pd.options.plotting.backend = "plotly"

dash.register_page(__name__,
                   name='Educational Attainment vs Employment Status')

# Dataset
JOINED_EMPLOYMENT_DF = dp.get_joined_employment_data()
EMPLOYMENT_DF = dp.get_employment_data()

# Helpful Global Variables
EDU_DEGREES = JOINED_EMPLOYMENT_DF['Attainment'].sort_values().unique()
REGIONS = JOINED_EMPLOYMENT_DF["Regions"].sort_values().unique()


# Create Dropdown menus
degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=[],
                               placeholder='Select a Degree',
                               className='dropdown-two', multi=True)
region_dropdown = dcc.Dropdown(options=REGIONS, value=None,
                               placeholder='Select a Region',
                               className='dropdown-two')

# Create layout for this page
layout = html.Div(children=[
    html.H1(children='Employment Status by Educational Attainment \
            per PUMA Regions (Washington State) from 2013 to 2017',
            className='graph-header'),
    html.Div(children=[
        html.Div([
            region_dropdown,
            dcc.Graph(id='graph3'),
            degree_dropdown,
            dcc.Graph(id='graph4'),
            html.Div(id='total')
        ], className='graphs'),
        dcc.Markdown('''
        # What did we find?

        [Add analysis].
        ''', className='markdown')
    ], className='question')
], className='whole-page')


# Top Graph
@callback(
    Output(component_id='graph3', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value')
)
def employment_status_by_attainment(region):
    unemployed_rate = JOINED_EMPLOYMENT_DF[['Regions', 'Attainment', 'Year',
                                            'Unemployed Rate']]
    region_mask = unemployed_rate['Regions'] == region
    unemployed_rate = unemployed_rate[region_mask]
    fig = px.line(unemployed_rate, x='Year', y='Unemployed Rate',
                  color='Attainment', markers=True,
                  title='Unemployed Rate vs Educational ' +
                  'Attainment by Region 2013 - 2017',
                  labels={'Year': 'Year',
                          'Regions': 'Region'})
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom',
                                  y=-.5, xanchor='left', x=0))
    fig.update_layout(title_xanchor='center', title_x=.5)
    return fig


# Bottom Graph
@callback(
    Output(component_id='graph4', component_property='figure'),
    Input(component_id=degree_dropdown, component_property='value')
)
def in_work_force_ratio(attainment):
    df = JOINED_EMPLOYMENT_DF[['Attainment', 'Year', 'Estimate Population',
                               'Total in labor force']]
    degree_mask = df['Attainment'].isin(list(attainment))
    df = df[degree_mask]
    df = df.groupby(['Year', 'Attainment'], as_index=False).sum()
    fig = px.bar(df, x='Year', y='Total in labor force',
                 barmode='group', color='Attainment',
                 title='Number of People in Labor Force per Attainment')
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom',
                                  y=-.5, xanchor='left', x=0))
    fig.update_layout(title_xanchor='center', title_x=.5)
    return fig


# Bottom text
@callback(
    Output(component_id='total', component_property='children'),
    Input(component_id=degree_dropdown, component_property='value')
)
def workforce_ratio(attainment):
    df = JOINED_EMPLOYMENT_DF[['Attainment', 'Year', 'Estimate Population',
                               'Total in labor force']]
    degree_mask = df['Attainment'].isin(list(attainment))
    df = df[degree_mask]
    df = df.groupby(['Year'], as_index=False).sum()
    print(df.head)
    return f'Out of {df["Estimate Population"].mean()}\
            average people per year.'
