# # Setup
# import dash
# from dash import Dash, html, dcc, Input, Output, callback
# import pandas as pd
# import data_processing as dp
# import plotly.express as px
# import numpy as np
# pd.options.plotting.backend = "plotly"

# dash.register_page(__name__, name='Question 2')

# # Datasets
# EDU_DF = dp.clean_edu_data()
# INCOME_DF = pd.read_csv('./data/median_income.csv')

# # Helpful Global Variables
# EDU_RACES = np.insert(EDU_DF["Race"].sort_values().unique(), 0, 'Select All')
# EDU_DEGREES = np.insert(EDU_DF['Attainment Label'].sort_values().unique(),
#                         0, 'Select All')


# # Create Dropdown menus
# race_dropdown = dcc.Dropdown(options=EDU_RACES, value=[],
#                              placeholder='Select a Race',
#                              className='dropdown', multi=True)
# degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=[],
#                                placeholder='Select a Degree',
#                                className='dropdown', multi=True)

# # Create layout for this page
# layout = html.Div(children=[
#     html.H1(children='Education Attainment Over Time, \
#             per Race (in Washington)', className='graph-header'),
#     html.Div(children=[
#         html.Div([
#             race_dropdown,
#             dcc.Graph(id='graph1'),
#             dcc.Graph(id='graph2')
#         ], className='graphs'),
#         dcc.Markdown('''
#         # What did we find?
#         ''', className='markdown')
#     ], className='question-one')
# ], className='whole-page')


# # input, output graph 1
# @callback(
#     Output(component_id='graph1', component_property='figure'),
#     Input(component_id=race_dropdown, component_property='value')
# )
# def attainment_over_time(race):
#     pass
