from dash import Dash, html, dcc, Input, Output
import pandas as pd
import data_processing as dp
pd.options.plotting.backend = "plotly"

# Datasets
EDU_DF = dp.clean_edu_data()
INCOME_DF = dp.clean_income_data()

# Helpful Global Variables
EDU_RACES = EDU_DF["Race"].sort_values().unique()

app = Dash()

race_dropdown = dcc.Dropdown(options=EDU_RACES, value=EDU_RACES[0])


def attainment_over_time(df: pd.DataFrame):
    pass


def main():
    print(EDU_RACES)
    # attainment_over_time(EDU_DF)


if __name__ == '__main__':
    main()