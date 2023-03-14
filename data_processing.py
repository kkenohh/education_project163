import pandas as pd
import os


def clean_edu_data() -> pd.DataFrame:
    edu_data = pd.read_csv('data/educational_attainment.csv')
    edu_data = edu_data.drop(columns=['StdDev'])
    edu_data = edu_data.rename(columns={
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


def create_income_dataset(filename):
    '''
    clean income dataset and create new csv files
    '''
    data = pd.read_csv(filename)

    if len(data.index) == 23:
        data = data.drop([21, 22])
    data = data.drop(range(0, 16))
    cols = data.columns.drop('Label (Grouping)')
    data[cols] = data[cols].apply(lambda x:
                                  x.str.replace(',', '').astype(float))

    # rename columns
    data = data.rename(
      columns={
        'Chelan & Douglas Counties PUMA, Washington!!Total!!Estimate':
        'Chelan & Douglas Counties',
        'Clallam & Jefferson Counties PUMA, Washington!!Total!!Estimate':
        'Clallam & Jefferson Counties',
        'Cowlitz, Pacific & Wahkiakum Counties PUMA; ' +
        'Washington!!Total!!Estimate':
        'Cowlitz, Pacific & Wahkiakum Counties',
        'Grant & Kittitas Counties PUMA, Washington!!Total!!Estimate':
        'Grant & Kittitas Counties',
        'Grays Harbor & Mason Counties PUMA, Washington!!Total!!Estimate':
        'Grays Harbor & Mason Counties',
        'Lewis, Klickitat & Skamania Counties PUMA; Washington!!Total!!Estimate':
        'Lewis, Klickitat & Skamania Counties',
        'Skagit, Island & San Juan Counties PUMA; Washington!!Total!!Estimate':
        'Skajit, Island & San Juan Counties',
        'Stevens, Okanogan, Pend Oreille & Ferry Counties PUMA; Washington!!Total!!Estimate':
        'Stevens, Okanogan, Pend Oreille & Ferry Counties',
        'Whatcom County--Bellingham City PUMA, Washington!!Total!!Estimate':
        'Whatcom County--Bellingham City',
        'Whitman, Asotin, Adams, Lincoln, Columbia & Garfield Counties PUMA; Washington!!Total!!Estimate':
        'Whitman, Asotin, Adams, Lincoln, Columbia & Garfield Counties',
        'Label (Grouping)': 'Label',
        'Washington!!Total!!Estimate': 'Washington'
      })

    # benton
    benton = data[data.filter(like='Benton').columns]
    sample = benton.copy()
    sample['Benton, Franklin, Kennewick, Richland & Walla Walla Counties'] \
        = sample.sum(axis=1)
    sample = sample.drop(
        columns=[
          'Benton & Franklin Counties--Pasco, Richland (North) & West Richland Cities PUMA; Washington!!Total!!Estimate',
          'Benton County (East Central)--Kennewick & Richland (South) Cities PUMA, Washington!!Total!!Estimate',
          'Walla Walla, Benton (Outer) & Franklin (Outer) Counties PUMA; Washington!!Total!!Estimate'
        ])

    data['Benton, Franklin, Kennewick, Richland & Walla Walla Counties'] \
        = sample['Benton, Franklin, Kennewick, Richland & Walla Walla Counties']
    data = data.drop(
        columns=[
          'Benton & Franklin Counties--Pasco, Richland (North) & West Richland Cities PUMA; Washington!!Total!!Estimate',
          'Benton County (East Central)--Kennewick & Richland (South) Cities PUMA, Washington!!Total!!Estimate',
          'Walla Walla, Benton (Outer) & Franklin (Outer) Counties PUMA; Washington!!Total!!Estimate'
        ])

    # clark
    clark = data[data.filter(like='Clark').columns]
    new = clark.copy()
    new['sum'] = new.sum(axis=1)

    data['Clark County'] = new['sum']
    data = data.drop(
        columns=[
          'Clark County (Southwest)--Vancouver City (West & Central) PUMA, Washington!!Total!!Estimate',
          'Clark County (West Central)--Salmon Creek & Hazel Dell PUMA, Washington!!Total!!Estimate',
          'Clark County (Southeast)--Vancouver (East), Camas & Washougal Cities PUMA; Washington!!Total!!Estimate',
          'Clark County (North)--Battle Ground City & Orchards PUMA, Washington!!Total!!Estimate'
        ])

    # king
    king = data[data.filter(like='King').columns]
    new = king.copy()
    new['sum'] = new.sum(axis=1)

    data['King County'] = new['sum']
    data = data.drop(
        columns=[
          'King County (Northwest)--Shoreline, Kenmore & Bothell (South) Cities PUMA; Washington!!Total!!Estimate',
          'King County (Northwest)--Redmond, Kirkland Cities, Inglewood & Finn Hill PUMA; Washington!!Total!!Estimate',
          'King County (Northwest Central)--Greater Bellevue City PUMA, Washington!!Total!!Estimate',
          'King County (Central)--Sammamish, Issaquah, Mercer Island & Newcastle Cities PUMA; Washington!!Total!!Estimate',
          'King County (Central)--Renton City, Fairwood, Bryn Mawr & Skyway PUMA; Washington!!Total!!Estimate',
          'King County (West Central)--Burien, SeaTac, Tukwila Cities & White Center PUMA; Washington!!Total!!Estimate',
          'King County (Far Southwest)--Federal Way, Des Moines Cities & Vashon Island PUMA; Washington!!Total!!Estimate',
          'King County (Southwest Central)--Kent City PUMA, Washington!!Total!!Estimate',
          'King County (Southwest)--Auburn City & Lakeland PUMA, Washington!!Total!!Estimate',
          'King County (Southeast)--Maple Valley, Covington & Enumclaw Cities PUMA; Washington!!Total!!Estimate',
          'King County (Northeast)--Snoqualmie City, Cottage Lake, Union Hill & Novelty Hill PUMA; Washington!!Total!!Estimate'
        ])

    # kitsap
    kitsap = data[data.filter(like='Kitsap').columns]
    new = kitsap.copy()
    new['sum'] = new.sum(axis=1)

    data['Kitsap County'] = new['sum']
    data = data.drop(
        columns=[
          'Kitsap County (North)--Bainbridge Island City & Silverdale PUMA, Washington!!Total!!Estimate',
          'Kitsap County (South)--Bremerton & Port Orchard Cities PUMA, Washington!!Total!!Estimate'
        ])

    # pierce
    pierce = data[data.filter(like='Pierce').columns]
    new = pierce.copy()
    new['sum'] = new.sum(axis=1)

    data['Pierce County'] = new['sum']
    data = data.drop(
        columns=[
          'Pierce County (Central)--Tacoma City (Central) PUMA, Washington!!Total!!Estimate',
          'Pierce County (Northwest)--Peninsula Region & Tacoma City (West) PUMA, Washington!!Total!!Estimate',
          'Pierce County (West Central)--Lakewood City & Joint Base Lewis-McChord PUMA, Washington!!Total!!Estimate',
          'Pierce County (South Central)--Tacoma City (South), Parkland & Spanaway PUMA; Washington!!Total!!Estimate',
          'Pierce County (North Central)--Tacoma (Port) & Bonney Lake (Northwest) Cities PUMA, Washington!!Total!!Estimate',
          'Pierce County (East Central)--Puyallup City & South Hill PUMA, Washington!!Total!!Estimate',
          'Pierce County (Southeast)--Graham, Elk Plain & Prairie Ridge PUMA; Washington!!Total!!Estimate'
        ])

    # spokane
    spokane = data[data.filter(like='Spokane').columns]
    new = spokane.copy()
    new['sum'] = new.sum(axis=1)

    data['Spokane County'] = new['sum']
    data = data.drop(
        columns=[
          'Spokane County (North Central)--Spokane City (North) PUMA, Washington!!Total!!Estimate',
          'Spokane County (South Central)--Spokane City (South) PUMA, Washington!!Total!!Estimate',
          'Spokane County (East Central)--Greater Spokane Valley City PUMA, Washington!!Total!!Estimate',
          'Spokane County (Outer)--Cheney City PUMA, Washington!!Total!!Estimate'
        ])

    # snohomish
    snohomish = data[data.filter(like='Snohomish').columns]
    new = snohomish.copy()
    new['sum'] = new.sum(axis=1)

    data['Snohomish County'] = new['sum']
    data = data.drop(
        columns=[
          'Snohomish County (South Central)--Bothell (North), Mill Creek Cities & Silver Firs PUMA; Washington!!Total!!Estimate',
          'Snohomish County (Central & Southeast)--Lake Stevens & Monroe Cities PUMA, Washington!!Total!!Estimate',
          'Snohomish County (North)--Marysville & Arlington Cities PUMA, Washington!!Total!!Estimate',
          'Snohomish County (Southwest)--Edmonds, Lynnwood & Mountlake Terrace Cities PUMA; Washington!!Total!!Estimate',
          'Snohomish County (West Central)--Mukilteo & Everett (Southwest) Cities PUMA, Washington!!Total!!Estimate',
          'Snohomish County (Central)--Everett City (Central & East) & Eastmont PUMA, Washington!!Total!!Estimate'
        ])

    # thurston
    thurston = data[data.filter(like='Thurston').columns]
    new = thurston.copy()
    new['sum'] = new.sum(axis=1)

    data['Thurston County'] = new['sum']
    data = data.drop(
        columns=[
          'Thurston County (Central)--Olympia, Lacey & Tumwater Cities PUMA; Washington!!Total!!Estimate',
          'Thurston County (Outer) PUMA, Washington!!Total!!Estimate'
        ])

    # yakima
    yakima = data[data.filter(like='Yakima').columns]
    new = yakima.copy()
    new['sum'] = new.sum(axis=1)

    data['Yakima County'] = new['sum']
    data = data.drop(
        columns=[
          'Yakima County (Central)--Greater Yakima City PUMA, Washington!!Total!!Estimate',
          'Yakima County (Outer)--Sunnyside & Grandview Cities PUMA, Washington!!Total!!Estimate',
        ])

    # drop unnecessary columns
    data = data.drop(
        columns=[
          'Seattle City (Northwest) PUMA, Washington!!Total!!Estimate',
          'Seattle City (Northeast) PUMA, Washington!!Total!!Estimate',
          'Seattle City (Downtown)--Queen Anne & Magnolia PUMA, Washington!!Total!!Estimate',
          'Seattle City (Southeast)--Capitol Hill PUMA, Washington!!Total!!Estimate',
          'Seattle City (West)--Duwamish & Beacon Hill PUMA, Washington!!Total!!Estimate'
        ])

    # clean data
    result = data
    result = result.T
    result.columns = result.iloc[0]
    result = result.reset_index()
    result = result.drop(0)

    name = filename.split('.')[0].split('/')[1].split('_')[2]
    result = result.rename(columns={'index': 'Region'})

    # add a year column
    result['Year'] = name

    new_file = 'data/income_og/income_' + name + '.csv'
    result.to_csv(new_file, index=False)

def concat_files(dir, file_type):
    filenames = os.listdir(dir)
    file_2013, file_2014, file_2015, file_2016, file_2017 = \
        [pd.read_csv(os.path.join(dir, f)) for f in filenames]

    concat_file = pd.concat([file_2013, file_2014, file_2015, file_2016, file_2017],
                      ignore_index=True)

    if(file_type == 'income'):
        concat_file = concat_file.set_index(['Region', 'Year'])

        # convert crosstable to stacked dataframe
        income_df = concat_file.stack(level=0)
        income_df = income_df.to_frame()
        income_df = income_df.reset_index()
        income_df.columns = ['Region', 'Year', 'Educational Attainment',
                            'Median Income']
        income_df.to_csv('data/income/median_income.csv', index=False)
    else:
        concat_file.to_csv('data/employment/employment_status.csv', index=False)


def get_income_data() -> pd.DataFrame:
    return pd.read_csv('./data/income/median_income.csv')


def clean_employment_data(file):
    data = pd.read_csv(file)

    # drop unneeded rows
    if len(data.index) == 41:
        data = data.drop(range(0, 37))
    else:
        data = data.drop(range(0, 31))
        data = data.drop([35, 36])

    data = convert_string(data)

    # rename columns
    data = rename_cols('Total', data)
    data = rename_cols('Employ', data)
    data = rename_cols('Unemploy', data)

    # calculate the actual number of people who is employed / unemployed
    for i in range(1, len(data.columns) - 1, 3):
        pop = data.columns[i]
        employed = data.columns[i+1]
        unemployed = data.columns[i+2]

        data[employed] = round(data[pop].astype(float) * data[employed])
        data[unemployed] = round(data[pop].astype(float) * data[unemployed])

    # rename cols for each PUMA regions
    # benton
    benton = data[data.filter(like='Benton').columns]
    benton_total = benton[benton.filter(like='Total').columns].copy()
    benton_total['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Total'] = benton_total.sum(axis=1)

    benton = data[data.filter(like='Benton').columns]
    benton_employ = benton[benton.filter(like='Employ').columns].copy()
    benton_employ['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Employ'] = benton_employ.sum(axis=1)

    benton = data[data.filter(like='Benton').columns]
    benton_unemploy = benton[benton.filter(like='Unemploy').columns].copy()
    benton_unemploy['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Unemploy'] = benton_unemploy.sum(axis=1)

    # create a new df
    employment_status = pd.DataFrame()
    employment_status['Attainment'] = data['Label (Grouping)']
    status = ['Total', 'Employ', 'Unemploy']

    employment_status['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Total'] = benton_total['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Total']
    employment_status['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Employ'] = benton_employ['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Employ']
    employment_status['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Unemploy'] = benton_unemploy['Benton, Franklin, Kennewick, Richland & Walla Walla Counties Unemploy']

    sum_puma('Clark', status, employment_status, data)
    sum_puma('Kitsap', status, employment_status, data)
    sum_puma('King', status, employment_status, data)
    sum_puma('Pierce', status, employment_status, data)
    sum_puma('Spokane', status, employment_status, data)
    sum_puma('Snohomish', status, employment_status, data)
    sum_puma('Thurston', status, employment_status, data)
    sum_puma('Yakima', status, employment_status, data)

    # add other cols
    other_puma = data[data.filter(regex='Label|Chelan|Clallam|Cowlitz|Grant|Grays|Klickitat|Skagit|Okanogan|Whatcom|Whitman').columns]
    employment_status = pd.merge(employment_status, other_puma,
                                 left_on='Attainment',
                                 right_on='Label (Grouping)')

    # reformat df
    stacked = employment_status.set_index('Attainment')
    new_format = stacked.stack(level=0)
    new_format = new_format.to_frame()
    new_format = new_format.reset_index()
    new_format.columns = ['Attainment', 'Regions', 'Count']
    new_format['Status'] = new_format['Regions'].apply(lambda x:
                                                       x.split(' ')[-1])
    new_format['Regions'] = new_format['Regions'].apply(lambda x:
                                                        x.rsplit(' ', 1)[0])

    new_df = new_format.pivot(index=['Attainment', 'Regions'],
                              columns='Status', values='Count')
    new_df = new_df.reset_index()
    new_df = new_df.drop(new_df.columns[2], axis=1)
    new_df = new_df.rename(columns={'Total': 'Total in labor force'})

    # clean attainment columns values
    pattern = r'.*\xa0(.*)'
    replacement = r'\1'
    new_df['Attainment'] = new_df['Attainment'].str.replace(pattern,
                                                            replacement,
                                                            regex=True)

    name = file.split('.')[0].split('/')[1].split('_')[1]

    # add a year column
    new_df['Year'] = name

    new_file = 'data/employment_og/employment_status_' + name + '.csv'
    new_df.to_csv(new_file, index=False)
    print('Successfully written to CSV file')

def convert_string(data) -> pd.DataFrame:
    # update the dataframe with float values for columns with percentage
    change_cols = data.filter(regex=r'([a-zA-z]+|\W+)ploy').columns
    data[change_cols] = data[change_cols].apply(lambda num: num.str.rstrip('%').astype('float') / 100.0)

    # update the dataframe with float values for columns with string numbers
    num_cols = data.filter(regex=r'([a-zA-z]+|\W+)Total').columns
    data[num_cols] = data[num_cols].apply(lambda num: num.str.replace(',', '').astype(float))
    return data

def sum_puma(region, status, new_df, old_df):
    puma = old_df[old_df.filter(like=region).columns]
    for word in status:
        puma_status = puma[puma.filter(like=word).columns].copy()
        puma_status[region + ' County ' + word] = puma_status.sum(axis=1)

        new_df[region + ' County ' + word] = puma_status[region +
                                                         ' County ' + word]


def rename_cols(col, df):
    old_cols = df.filter(like=col)
    regions = old_cols.columns.str.extract(r'^(.*?(?= PUMA))', expand=False)
    regions = list(regions)

    new_cols = [r + ' ' + col for r in regions]
    df = df.rename(columns={old_col: new_col for old_col,
                            new_col in zip(list(old_cols.columns), new_cols)})
    return df


def merge_data() -> pd.DataFrame:
    edu = clean_edu_data()
    employment = pd.read_csv('./data/employment/employment_status.csv')

    edu['Attainment Label'] = edu['Attainment Label'].replace(
        ['Some college, no degree', 'Associate degree'],
        'Some college or associate\'s degree')
    edu['Attainment Label'] = edu['Attainment Label'].replace(
        ['Bachelor\'s degree', 'Master\'s degree',
         'Professional or Doctorate degree'],
        'Bachelor\'s degree or higher')
    edu_data = edu[['Attainment Label', 'Puma Label', 'year',
                    'Estimate Population']]
    edu_data = edu_data.rename(columns={'Attainment Label': 'Attainment',
                                        'Puma Label': 'Regions',
                                        'year': 'Year'})

    employment['Attainment'] = employment['Attainment'].replace(
        'Less than high school graduate', 'Less than high school')
    employment['Attainment'] = employment['Attainment'].replace(
        'High school graduate (includes equivalency)',
        'High school or equivalent')
    employment['Attainment'] = employment['Attainment'].replace(
        'Less than high school graduate', 'Less than high school')

    edu_data = edu_data.groupby(['Attainment', 'Regions', 'Year']).sum()

    employ_data = employment.groupby(['Attainment', 'Regions',
                                      'Year']).sum()

    joined_data = pd.merge(edu_data, employ_data,
                           on=['Attainment', 'Regions', 'Year'])
    joined_data = joined_data.reset_index()
    joined_data['Unemployed Rate'] = \
        (joined_data['Unemploy'] / joined_data['Total in labor force']) * 100

    # write to CSV
    new_file = 'data/employment/joined_employment_status.csv'
    joined_data.to_csv(new_file, index=False)


def get_joined_employment_data() -> pd.DataFrame:
    return pd.read_csv('data/employment/joined_employment_status.csv')


def get_employment_data() -> pd.DataFrame:
    return pd.read_csv('data/employment/employment_status.csv')


# cleaning smoking.csv
def clean_smoking_data() -> pd.DataFrame:
    data = pd.read_csv('data/smoking.csv')
    smoking_data = data.drop(columns=['Lower CI', 'Upper CI'])
    # "**"" = data supression, "--"" = no data, "NR" = not reliable
    NR_smoking_data = smoking_data[smoking_data['Percentage'].str.contains("NR") == False]
    NR_smoking_data = NR_smoking_data.rename(columns={'Count': 'Smoking Count', 'Percentage': 'Percentage Smoking'})
    """
    contains_data = NR_smoking_data[NR_smoking_data['Percentage'].str.contains("--") == False]
    clean_smoking_data = contains_data[contains_data['Percentage'].str.contains("**") == False]
    """
    return NR_smoking_data


# cleaning poor_mental_health.csv
def clean_mental_health_data() -> pd.DataFrame:
    data = pd.read_csv('data/poor_mental_health.csv')
    mental_health_data = data.drop(columns=['Lower CI', 'Upper CI'])
    # "**"" = data supression, "--"" = no data, "NR" = not reliable
    NR_mental_health_data = mental_health_data[mental_health_data['Percentage'].str.contains("NR") == False]
    NR_mental_health_data = NR_mental_health_data.rename(columns={'Count': 'Poor Mental Health Count', 'Percentage': 'Percentage Poor Mental Health'})
    """
    contains_data = NR_smoking_data[NR_smoking_data['Percentage'].str.contains("--") == False]
    clean_smoking_data = contains_data[contains_data['Percentage'].str.contains("**") == False]
    """
    return NR_mental_health_data


# cleaning diabetes.csv
def clean_diabetes_data() -> pd.DataFrame:
    data = pd.read_csv('data/diabetes.csv')
    diabetes_data = data.drop(columns=['Lower CI', 'Upper CI'])
    # "**"" = data supression, "--"" = no data, "NR" = not reliable
    NR_diabetes_data = diabetes_data[diabetes_data['Percentage'].str.contains("NR") == False]
    NR_diabetes_data = NR_diabetes_data.rename(columns={'Count': 'Diabetes Count', 'Percentage': 'Percentage Diabetes'})
    """
    contains_data = NR_smoking_data[NR_smoking_data['Percentage'].str.contains("--") == False]
    clean_smoking_data = contains_data[contains_data['Percentage'].str.contains("**") == False]
    """
    return NR_diabetes_data


# cleaning binge_drinking.csv
def clean_binge_drinking_data() -> pd.DataFrame:
    data = pd.read_csv('data/binge_drinking.csv')
    binge_drinking_data = data.drop(columns=['Lower CI', 'Upper CI'])
    # "**"" = data supression, "--"" = no data, "NR" = not reliable
    NR_binge_drinking_data = binge_drinking_data[binge_drinking_data['Percentage'].str.contains("NR") == False]
    NR_binge_drinking_data = NR_binge_drinking_data.rename(columns={'Count': 'Binge Drinking Count', 'Percentage': 'Binge Drinking Percentage'})
    """
    contains_data = NR_smoking_data[NR_smoking_data['Percentage'].str.contains("--") == False]
    clean_smoking_data = contains_data[contains_data['Percentage'].str.contains("**") == False]
    """
    return NR_binge_drinking_data


# merging smoking and binge drinking
def merge_smoking_drinking() -> pd.DataFrame:
    smoking = clean_smoking_data()
    drinking = clean_binge_drinking_data()
    merged_smoking_drinking = pd.merge(smoking, drinking, on=['County'])
    merged_smoking_drinking['Average Population'] = (merged_smoking_drinking['Population_x'] + merged_smoking_drinking['Population_y']) / 2
    merged_smoking_drinking = merged_smoking_drinking.drop(columns=['Population_x', 'Population_y'])
    return merged_smoking_drinking


# merging mental health and diabetes
def merge_mental_diabetes() -> pd.DataFrame:
    mental_health = clean_mental_health_data()
    diabetes = clean_diabetes_data()
    merged_mental_diabetes = pd.merge(mental_health, diabetes, on=['County'])
    merged_mental_diabetes['Average Population'] = (merged_mental_diabetes['Population_x'] + merged_mental_diabetes['Population_y']) / 2
    merged_mental_diabetes = merged_mental_diabetes.drop(columns=['Population_x', 'Population_y'])
    return merged_mental_diabetes


# merging merged sets
def merge_health() -> pd.DataFrame:
    smoking_drinking = merge_smoking_drinking()
    mental_diabetes = merge_mental_diabetes()
    merged = pd.merge(smoking_drinking, mental_diabetes, on=['County'])
    merged['Average Population'] = (merged['Average Population_x'] + merged['Average Population_y']) / 2
    merged = merged.drop(columns=['Average Population_x', 'Average Population_y'])
    return merged


def main():
    # create income files
    create_income_dataset('data/median_income_2013.csv')
    create_income_dataset('data/median_income_2014.csv')
    create_income_dataset('data/median_income_2015.csv')
    create_income_dataset('data/median_income_2016.csv')
    create_income_dataset('data/median_income_2017.csv')

    '''
    merge_income_data('/data/income')
    '''

    print('Merged Smoking Drinking:')
    print(merge_smoking_drinking().columns)
    print('Merged Mental Diabetes:')
    print(merge_mental_diabetes().columns)
    print('Merged health sets:')
    print(merge_health().columns)

    # create employment files
    clean_employment_data('data/employment_2013.csv')
    clean_employment_data('data/employment_2014.csv')
    clean_employment_data('data/employment_2015.csv')
    clean_employment_data('data/employment_2016.csv')
    clean_employment_data('data/employment_2017.csv')

    concat_files('data/income_og', 'income')
    concat_files('data/employment_og', 'employment')
    merge_data()


if __name__ == '__main__':
    main()
