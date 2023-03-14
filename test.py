import data_processing as dp
import pandas as pd
import cse163_utils as util

def test_string_conversion():
    result = pd.read_csv('./data/test_files/result_convert.csv')

    #read test file
    test = pd.read_csv('./data/test_files/test_employment_file.csv')
    test_df = dp.convert_string(test)

    if (result.values == test_df.values).all():
        print('Convert numbers successfully!')
    else:
        print('Failed to convert')


def main():
    test_string_conversion()


if __name__ == '__main__':
    main()
