# Setup
import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import data_processing as dp
import plotly.express as px
import numpy as np
pd.options.plotting.backend = "plotly"

dash.register_page(__name__, name='Income vs No HS Diploma')

# Datasets
EDU_DF = dp.clean_edu_data()
INCOME_DF = dp.get_income_data()

# Helpful Global Variables
REGIONS = np.delete(INCOME_DF["Region"].sort_values().unique(), 16)


# Create Dropdown menus
region_dropdown = dcc.Dropdown(options=REGIONS, value=[],
                               placeholder='Select a Region',
                               className='dropdown-two', multi=True)

# Create layout for this page
layout = html.Div(children=[
    html.H1(children='Median Income Over Time per County\
            (in Washington)', className='graph-header'),
    html.Div(children=[
        html.Div([
            region_dropdown,
            dcc.Graph(id='graph2'),
            dcc.Graph(id='graph1')
        ], className='graphs'),
        dcc.Markdown('''
        # What did we find?

        In this analysis, we looked at the correlation between median income
        of a region, and the number of people who attained "less than high
        school".
        ''', className='markdown')
    ], className='question')
], className='whole-page')


# Top Graph
@callback(
    Output(component_id='graph2', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value')
)
def income_over_time(region):
    df = EDU_DF[['Puma Label', 'year', 'Estimate Population',
                 'Attainment Label']]
    region_mask = df['Puma Label'].isin(list(region))
    df = df[region_mask]
    degree_mask = df['Attainment Label'] == 'Less than high school'
    df = df[degree_mask]
    df = df.groupby(['Puma Label', 'year'],
                    as_index=False)['Estimate Population'].sum()
    fig = px.line(df, x='year', y='Estimate Population', color='Puma Label',
                  markers=True,
                  title='Population With "Less Than High School" Over Time',
                  labels={'year': 'Year',
                          'Puma Label': 'Region'})
    y = len(region) * -.07 + -.2
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom',
                                  y=y, xanchor='left', x=0))
    fig.update_layout(title_xanchor='center', title_x=.5)
    return fig


# Bottom Graph
@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value')
)
def degree_over_time(region):
    df = INCOME_DF[['Region', 'Year', 'Median Income']]
    region_mask = df['Region'].isin(list(region))
    df = df[region_mask]
    df = df.groupby(['Region', 'Year'], as_index=False)['Median Income'].mean()
    fig = px.line(df, x='Year', y='Median Income', color='Region',
                  markers=True, title='Median Income Over Time')
    y = len(region) * -.07 + -.2
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom',
                                  y=y, xanchor='left', x=0))
    fig.update_layout(title_xanchor='center', title_x=.5)
    return fig
