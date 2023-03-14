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

        The questions we are trying to answer with these graphs are: **How has
        education attainment level changed over time? What factors could be
        contributing to this pattern, if there is one?**

        We made the first graph to show the education attainment level over
        time. Then, we decided to explore how income impacts the education
        attainment level so we added a graph that shows how median income
        changes over time. The first region that we looked at was King
        County because we live there and it also has the highest population
        count in Washington. We found that there doesn't seem to be much
        correlation between income and education attainment. Income steadily
        increases over time, while the number of people who don't achieve
        a high school degree go up and down, not matching the pattern of
        the income graph. 

        The second region we looked at was Clark County because it has the
        fifth highest population count, and it's also in a different part
        of Washington. We found that while income was steadily increasing,
        the number of people who didn't achieve a high school degree
        increased, and then decreased. So once again we can't draw any
        conclusions from this.

        After look at a lot of other regions, we were able to conclude that
        there doesn't seem to be any correlation between income level and
        the number of people who don't achieve a high school diploma. This
        is surprising because we thought that lower income would decrease
        education quality because of less resources and quality teachers.
        ''', className='markdown')
    ], className='question')
], className='whole-page')


# Top Graph
@callback(
    Output(component_id='graph2', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value')
)
def degree_over_time(region):
    '''
    Takes a list of regions and produces a line plot showing the level
    of education attained over time grouped by PUMA region.
    Parameters:
        region - a list of regions
    Returns:
        a line plot
    '''
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
def income_over_time(region):
    '''
    Takes a list of regions and produces a line plot showing the median
    income over time grouped by PUMA region.
    Parameters:
        region - a list of regions
    Returns:
        a line plot
    '''
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
