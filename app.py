from dash import Dash, html, dcc, Input, Output
import pandas as pd
import data_processing as dp
import plotly.express as px
pd.options.plotting.backend = "plotly"

# Datasets
EDU_DF = dp.clean_edu_data()
INCOME_DF = dp.clean_income_data()

# Helpful Global Variables
EDU_RACES = EDU_DF["Race"].sort_values().unique()
EDU_DEGREES = EDU_DF['Attainment Level'].sort_values().unique()

# Dash app stuff {
app = Dash(__name__)

race_dropdown = dcc.Dropdown(options=EDU_RACES, value=EDU_RACES[0])
degree_dropdown = dcc.Dropdown(options=EDU_DEGREES, value=EDU_DEGREES[0])

dcc.Markdown('./README.md')

app.layout = html.Div(children=[
    html.H1(children='Education Attainment Over Time, per Race'),
    race_dropdown,
    dcc.Graph(id='attainment')
], className='whole-page')


@app.callback(
    Output(component_id='attainment', component_property='figure'),
    Input(component_id=race_dropdown, component_property='value')
)
def attainment_over_time(race, degree):
    df = EDU_DF[['year', 'Race', 'Estimate Population', 'Attainment Label']]
    df = df[df['Race'] == race]
    df = df.groupby(['year', 'Attainment Label'], as_index=False)['Estimate Population'].sum()
    chart = px.line(df, x='year', y='Estimate Population', color='Attainment Label')
    return chart


if __name__ == '__main__':
    app.run_server(debug=True)