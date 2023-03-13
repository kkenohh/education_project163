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

# Datasets
EDU_DF = dp.clean_edu_data()
EMPLOYMENT_DF = dp.get_employment_data()

# Helpful Global Variables
EDU_DEGREES = np.insert(EDU_DF['Attainment Label'].sort_values().unique(),
                        0, 'Select All')
REGIONS = np.delete(EMPLOYMENT_DF["Regions"].sort_values().unique(), 16)


# Create Dropdown menus
degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=[],
                               placeholder='Select a Degree',
                               className='dropdown', multi=True)
region_dropdown = dcc.Dropdown(options=REGIONS, value=[],
                               placeholder='Select a Region',
                               className='dropdown-two', multi=True)

# Create layout for this page
layout = html.Div(children=[
    html.H1(children='Employment Status by Educational Attainment \
            per PUMA Regions (Washington State) from 2013 to 2017',
            className='graph-header'),
    html.Div(children=[
        html.Div([
            region_dropdown,
            dcc.Graph(id='graph3'),
            dcc.Graph(id='graph4')
        ], className='graphs'),
        dcc.Markdown('''
        # What did we find?

        [Add analysis].
        ''', className='markdown')
    ], className='question-one')
], className='whole-page')


# Top Graph
@callback(
    Output(component_id='graph3', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value')
)
def employment_status_by_attainment(region):
    EDU_DF['Attainment Label'] = EDU_DF['Attainment Label'].replace(
        ['Some college, no degree', 'Associate degree'],
        'Some college or associate\'s degree')
    EDU_DF['Attainment Label'] = EDU_DF['Attainment Label'].replace(
        ['Bachelor\'s degree', 'Master\'s degree',
         'Professional or Doctorate degree'],
        'Bachelor\'s degree or higher')
    edu_data = EDU_DF[['Attainment Label', 'Puma Label', 'year',
                       'Estimate Population']]
    edu_data = edu_data.rename(columns={'Attainment Label': 'Attainment',
                                        'Puma Label': 'Regions',
                                        'year': 'Year'})

    EMPLOYMENT_DF['Attainment'] = EMPLOYMENT_DF['Attainment'].replace(
        'Less than high school graduate', 'Less than high school')
    EMPLOYMENT_DF['Attainment'] = EMPLOYMENT_DF['Attainment'].replace(
        'High school graduate (includes equivalency)',
        'High school or equivalent')
    EMPLOYMENT_DF['Attainment'] = EMPLOYMENT_DF['Attainment'].replace(
        'Less than high school graduate', 'Less than high school')

    edu_data = edu_data.groupby(['Attainment', 'Regions', 'Year']).sum()

    employ_data = EMPLOYMENT_DF.groupby(['Attainment', 'Regions',
                                         'Year']).sum()

    joined_data = pd.merge(edu_data, employ_data,
                           on=['Attainment', 'Regions', 'Year'])
    joined_data = joined_data.reset_index()
    joined_data['Unemployed Rate'] = \
        (joined_data['Unemploy'] / joined_data['Total in labor force']) * 100

    unemployed_rate = joined_data[['Regions', 'Attainment', 'Year',
                                   'Unemployed Rate']]

    region_mask = unemployed_rate['Regions'].isin(list(region))
    unemployed_rate = unemployed_rate[region_mask]
    fig = px.line(unemployed_rate, x='Year', y='Unemployed Rate',
                  color='Regions', markers=True,
                  title='Unemployed Rate vs Educational Attainment 2013 - 2017',
                  labels={'Year': 'Year',
                          'Regions': 'Region'})
    y = len(region) * -.07 + -.2
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom',
                                  y=y, xanchor='left', x=0))
    fig.update_layout(title_xanchor='center', title_x=.5)
    return fig

# Bottom Graph
@callback(
    Output(component_id='graph4', component_property='figure'),
    Input(component_id=region_dropdown, component_property='value'),
    Input(component_id=degree_dropdown, component_property='value')
)
def in_work_force_ratio(attainment):
    df = EMPLOYMENT_DF[['Regions', 'Year', 'Estimate Population',
                        'Total in labor force']]
    degree_mask = df['Attainment'].isin(list(attainment))
    df = df[degree_mask]
    df = df.groupby(['Regions', 'Year'],
                    as_index=False)['Estimate Population',
                                    'Total in labor force'].apply(
                                    lambda col: col.sum())
    fig = px.bar(df, x='Year', y=['Estimate Population',
                                  'Total in labor force'],
                 color='Attainment',
                 markers=True,
                 title='Ratio of population in Labor Force per Attainment')
    y = len(attainment) * -.07 + -.2
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom',
                                  y=y, xanchor='left', x=0))
    fig.update_layout(title_xanchor='center', title_x=.5)
    return fig
