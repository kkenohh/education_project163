import dash
from dash import html, dcc

dash.register_page(__name__, name='Final Thoughts')

layout = html.Div(children=[
    dcc.Markdown('''
    # Conclusion

    ''', className='markdown home'),
    dcc.Markdown('''
    # Machine Learning Results

    ''', className='markdown home')
], className='home-div')