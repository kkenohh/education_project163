import pandas as pd
import data_processing as dp


def main():
    edu_df = dp.clean_edu_data()
    income_df = dp.clean_income_data()


if __name__ == '__main__':
    main()