# Setup
import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import data_processing as dp
import plotly.express as px
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
        The questions we are trying to answer with this graph are:

        ***- Is there any correlation between educational attainment and
        the unemployment rate in the 5 years interval 2013-2017? Especially
        does having higher educational attainment result in lower unemployment
        rate?***

        To answer the first question, we can look at the first graph. When
        looking at each PUMA region individually, we observed that
        people with "Less than high school graduate" degree consistently
        had the highest unemployment rate out of the four educational
        attainment levels, whereas those with "Bachelor's degree or higher"
        had the lowest unemployment rate across all PUMA regions in Washington
        State between 2013 and 2017.

        Looking at King County specifically, we found that the unemployment
        rate for individuals with "Less than high school graduate" degree saw
        a sharp decline, followed by a gradual increase from 2014 to 2016, and
        then another significant decrease from 2016 to 2017. The trend for the
        unemployment rate for individuals with "High school or equivalent"
        degree and "Some college or associate's degree" was similar during
        this time interval, with a slight decrease from 2013 to 2014 and 2015
        to 2016, and a slight increase in 2014-2015 and 2016-2017. Conversely,
        the unemployment rate for individuals with "Bachelor's degree or
        higher" steadily decreased throughout the 5-year period. Although there
        are some big changes in unemployment rate for each educational
        attainment, the general trend still matches with the general trends
        across all PUMA regions in Washington State.

        All in all, looking at our graph, we predict that there might be a
        relationship between education and unemployment rate, where people
        with higher educational attainment tend to have lower unemployment
        rate than those with less than high school attainment level.

        ***- Which educational attainment has the highest ratio of people
        in the labor force?***

        By examining the second graph, it is noticeable that the number of
        individuals who have attained a "Less than high school" degree is the
        smallest when compared to the other three educational attainment levels
        from 2013 to 2017. This could be due to the fact that individuals with
        a "Bachelor's degree or higher" may choose to continue their education,
        thus causing this low ratio. On the other hand, the ratios for the
        other three educational attainment levels are relatively similar, where
        all three are much higher than the number of people with "Less than
        a high school" degree.
        ''', className='markdown')
    ], className='question')
], className='whole-page')


# Top Graph
@callback(
    Output(component_id='graph3', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value')
)
def employment_status_by_attainment(region):
    '''
    Takes a list of regions and produces a line plot showing the
    unemployment rate over time grouped by attainment level.
    Parameters:
        region - a list of regions
    Returns:
        a line plot
    '''
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
    Input(component_id=degree_dropdown, component_property='value'),
    Input(component_id=region_dropdown, component_property='value')
)
def in_work_force_ratio(attainment, region):
    '''
    Takes a list of degree levels and produces a line plot
    showing the number of people who are employed grouped by the level
    of degree.
    Parameters:
        attainment - a list of degree levels
    Returns:
        a line plot
    '''
    df = JOINED_EMPLOYMENT_DF[['Regions', 'Attainment', 'Year',
                               'Estimate Population', 'Total in labor force']]
    region_mask = df['Regions'] == region
    df = df[region_mask]
    degree_mask = df['Attainment'].isin(list(attainment))
    df = df[degree_mask]
    df = df.groupby(['Year', 'Attainment'],
                    as_index=False)[list(['Estimate Population',
                                    'Total in labor force'])].sum()
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
    Input(component_id=degree_dropdown, component_property='value'),
    Input(component_id=region_dropdown, component_property='value')
)
def workforce_ratio(attainment, region):
    '''
    Takes a list of degrees and finds the average total population over
    the years of people who attained the degrees.
    Parameters:
        attainment - a list of degree levels
    Returns:
        a str of the result
    '''
    df = JOINED_EMPLOYMENT_DF[['Regions', 'Attainment', 'Year',
                               'Estimate Population', 'Total in labor force']]
    region_mask = df['Regions'] == region
    df = df[region_mask]
    degree_mask = df['Attainment'].isin(list(attainment))
    df = df[degree_mask]
    df = df.groupby(['Year'], as_index=False)['Estimate Population'].sum()
    return f'Out of around {df["Estimate Population"].mean()} people.'
