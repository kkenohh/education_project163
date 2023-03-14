'''
This program implements tests for functions convert_string, sum_puma,
calc_people, and clean_col_values
'''
import data_processing as dp
import pandas as pd
from cse163_utils import assert_equals


def test_string_conversion() -> None:
    '''
    Test convert_string
    '''
    result = pd.read_csv('./data/test_files/result_convert.csv')
    test = pd.read_csv('./data/test_files/test_employment_file.csv')
    test_df = dp.convert_string(test)
    assert_equals(result, test_df)


def test_combine_cols() -> None:
    '''
    Test sum_puma
    '''
    res_combine = pd.read_csv('./data/test_files/result_combine.csv')
    test_combine = pd.read_csv('./data/test_files/test_combine.csv')
    test_combine = dp.convert_string(test_combine)

    status = ['Total', 'Employ', 'Unemploy']
    combined = pd.DataFrame()
    dp.sum_puma('King', status, combined, test_combine)
    assert_equals(res_combine, combined)


def test_calc_people() -> None:
    '''
    Test calc_people
    '''
    test_file = pd.read_csv('./data/test_files/test_combine.csv')
    test_file = dp.convert_string(test_file)
    res_calc = pd.read_csv('./data/test_files/res_calc.csv')

    test_file = dp.calc_people(test_file)
    assert_equals(res_calc, test_file)


def test_clean_col_values() -> None:
    '''
    Test clean_col_values
    '''
    test_rename = pd.DataFrame({
        'Attainment':
            ['\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Bachelor\'s degree or higher',
             '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0Less than high school',
             '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0crying',
             '\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0blahblah']})

    res_rename = pd.DataFrame({'Attainment': ['Bachelor\'s degree or higher',
                                              'Less than high school',
                                              'crying',
                                              'blahblah']})

    test_rename = dp.clean_col_values(test_rename)
    assert_equals(res_rename, test_rename)


def main():
    test_string_conversion()
    test_combine_cols()
    test_calc_people()
    test_clean_col_values()


if __name__ == '__main__':
    main()

