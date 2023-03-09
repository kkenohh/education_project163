import geopandas as gpd
import pandas as pd


def clean_edu_data() -> pd.DataFrame:
    edu_data = pd.read_csv('educational_attainment.csv')
    edu_data = edu_data.drop(columns=['StdDev'])
    edu_data = edu_data.rename(columns={
      'year': 'Year',
      'F_age_cat': 'Age range',
      'F_puma_recode_code': 'Puma Code',
      'F_puma_recode_label': 'Puma Label',
      'schl_recode_label': 'Attainment Label',
      'schl_recode_code': 'Attainment Code',
      'rac1p_recode_label': 'Race',
      'rac1p_recode_code': 'Race Code',
      'Population Estimate (Count)*': 'Estimate Population'
    })

    clean_edu_data = edu_data.dropna()
    return clean_edu_data


def clean_income_data() -> pd.DataFrame:
    income = pd.read_csv('median_income.csv')
    income = income.dropna()
    return income
