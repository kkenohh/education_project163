import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    dcc.Markdown('''
    # Introduction

    For our project, we decided to explore education attainment level in
    Washington state and demographics that may relate to it or cause the
    levels to be how they are. Our team members are Ken Oh, Allison Ho,
    and Willis Liang. 
    ''', className='markdown home'),
    dcc.Markdown('''
    # Research Questions

    1. Is there large disparity between any of the levels of education
    attained? Between which degrees? What could be causing this disparity?

    2. How has education attainment level changed over time? Are there any
    factors that are contributing to this pattern? If so, what?

    3. 
    ''', className='markdown home'),
    dcc.Markdown('''
    # Motivation

    
    ''', className='markdown home'),
    dcc.Markdown('''
    # Datasets

    
    ''', className='markdown home')
], className='home-div')
