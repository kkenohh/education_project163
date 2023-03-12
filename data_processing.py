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
    clean income dataset
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
        'Cowlitz, Pacific & Wahkiakum Counties PUMA; \
          Washington!!Total!!Estimate':
        'Cowlitz, Pacific & Wahkiakum Counties',
        'Grant & Kittitas Counties PUMA, Washington!!Total!!Estimate':
        'Grant & Kittitas Counties',
        'Grays Harbor & Mason Counties PUMA, Washington!!Total!!Estimate':
        'Grays Harbor & Mason Counties',
        'Lewis, Klickitat & Skamania Counties PUMA; \
          Washington!!Total!!Estimate':
        'Lewis, Klickitat & Skamania Counties',
        'Skagit, Island & San Juan Counties PUMA; Washington!!Total!!Estimate':
        'Skajit, Island & San Juan Counties',
        'Stevens, Okanogan, Pend Oreille & Ferry Counties PUMA; \
          Washington!!Total!!Estimate':
        'Stevens, Okanogan, Pend Oreille & Ferry Counties',
        'Whatcom County--Bellingham City PUMA, Washington!!Total!!Estimate':
        'Whatcom County--Bellingham City',
        'Whitman, Asotin, Adams, Lincoln, Columbia & Garfield Counties PUMA; \
          Washington!!Total!!Estimate':
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
          'Benton & Franklin Counties--Pasco, Richland (North) & \
            West Richland Cities PUMA; Washington!!Total!!Estimate',
          'Benton County (East Central)--Kennewick & Richland (South) \
            Cities PUMA, Washington!!Total!!Estimate',
          'Walla Walla, Benton (Outer) & Franklin (Outer) Counties PUMA; \
            Washington!!Total!!Estimate'
        ])

    data['Benton, Franklin, Kennewick, Richland & Walla Walla Counties'] \
        = sample['Benton, Franklin, Kennewick, Richland & \
                 Walla Walla Counties']
    data = data.drop(
        columns=[
          'Benton & Franklin Counties--Pasco, Richland (North) \
            & West Richland Cities PUMA; Washington!!Total!!Estimate',
          'Benton County (East Central)--Kennewick & Richland (South) \
            Cities PUMA, Washington!!Total!!Estimate',
          'Walla Walla, Benton (Outer) & Franklin (Outer) Counties PUMA; \
            Washington!!Total!!Estimate'
        ])

    # clark
    clark = data[data.filter(like='Clark').columns]
    new = clark.copy()
    new['sum'] = new.sum(axis=1)

    data['Clark County'] = new['sum']
    data = data.drop(
        columns=[
          'Clark County (Southwest)--Vancouver City (West & Central) PUMA,\
              Washington!!Total!!Estimate',
          'Clark County (West Central)--Salmon Creek & Hazel Dell PUMA, \
            Washington!!Total!!Estimate',
          'Clark County (Southeast)--Vancouver (East), Camas & Washougal \
            Cities PUMA; Washington!!Total!!Estimate',
          'Clark County (North)--Battle Ground City & Orchards PUMA, \
            Washington!!Total!!Estimate'
        ])

    # king
    king = data[data.filter(like='King').columns]
    new = king.copy()
    new['sum'] = new.sum(axis=1)

    data['King County'] = new['sum']
    data = data.drop(
        columns=[
          'King County (Northwest)--Shoreline, Kenmore & Bothell (South) \
            Cities PUMA; Washington!!Total!!Estimate',
          'King County (Northwest)--Redmond, Kirkland Cities, Inglewood & \
            Finn Hill PUMA; Washington!!Total!!Estimate',
          'King County (Northwest Central)--Greater Bellevue City PUMA, \
            Washington!!Total!!Estimate',
          'King County (Central)--Sammamish, Issaquah, Mercer Island & \
            Newcastle Cities PUMA; Washington!!Total!!Estimate',
          'King County (Central)--Renton City, Fairwood, Bryn Mawr & \
            Skyway PUMA; Washington!!Total!!Estimate',
          'King County (West Central)--Burien, SeaTac, Tukwila Cities \
            & White Center PUMA; Washington!!Total!!Estimate',
          'King County (Far Southwest)--Federal Way, Des Moines Cities \
            & Vashon Island PUMA; Washington!!Total!!Estimate',
          'King County (Southwest Central)--Kent City PUMA, \
            Washington!!Total!!Estimate',
          'King County (Southwest)--Auburn City & Lakeland PUMA, \
            Washington!!Total!!Estimate',
          'King County (Southeast)--Maple Valley, Covington & Enumclaw Cities \
            PUMA; Washington!!Total!!Estimate',
          'King County (Northeast)--Snoqualmie City, Cottage Lake, Union Hill \
            & Novelty Hill PUMA; Washington!!Total!!Estimate'
        ])

    # kitsap
    kitsap = data[data.filter(like='Kitsap').columns]
    new = kitsap.copy()
    new['sum'] = new.sum(axis=1)

    data['Kitsap County'] = new['sum']
    data = data.drop(
        columns=[
          'Kitsap County (North)--Bainbridge Island City & Silverdale PUMA, \
            Washington!!Total!!Estimate',
          'Kitsap County (South)--Bremerton & Port Orchard Cities PUMA, \
            Washington!!Total!!Estimate'
        ])

    # pierce
    pierce = data[data.filter(like='Pierce').columns]
    new = pierce.copy()
    new['sum'] = new.sum(axis=1)

    data['Pierce County'] = new['sum']
    data = data.drop(
        columns=[
          'Pierce County (Central)--Tacoma City (Central) PUMA, \
            Washington!!Total!!Estimate',
          'Pierce County (Northwest)--Peninsula Region & Tacoma \
            City (West) PUMA, Washington!!Total!!Estimate',
          'Pierce County (West Central)--Lakewood City & Joint \
            Base Lewis-McChord PUMA, Washington!!Total!!Estimate',
          'Pierce County (South Central)--Tacoma City (South), \
            Parkland & Spanaway PUMA; Washington!!Total!!Estimate',
          'Pierce County (North Central)--Tacoma (Port) & Bonney \
            Lake (Northwest) Cities PUMA, Washington!!Total!!Estimate',
          'Pierce County (East Central)--Puyallup City & South \
            Hill PUMA, Washington!!Total!!Estimate',
          'Pierce County (Southeast)--Graham, Elk Plain & Prairie \
            Ridge PUMA; Washington!!Total!!Estimate'
        ])

    # spokane
    spokane = data[data.filter(like='Spokane').columns]
    new = spokane.copy()
    new['sum'] = new.sum(axis=1)

    data['Spokane County'] = new['sum']
    data = data.drop(
        columns=[
          'Spokane County (North Central)--Spokane City (North) PUMA, \
            Washington!!Total!!Estimate',
          'Spokane County (South Central)--Spokane City (South) PUMA, \
            Washington!!Total!!Estimate',
          'Spokane County (East Central)--Greater Spokane Valley City PUMA, \
            Washington!!Total!!Estimate',
          'Spokane County (Outer)--Cheney City PUMA, \
            Washington!!Total!!Estimate'
        ])

    # snohomish
    snohomish = data[data.filter(like='Snohomish').columns]
    new = snohomish.copy()
    new['sum'] = new.sum(axis=1)

    data['Snohomish County'] = new['sum']
    data = data.drop(
        columns=[
          'Snohomish County (South Central)--Bothell (North), \
            Mill Creek Cities & Silver Firs PUMA; Washington!!Total!!Estimate',
          'Snohomish County (Central & Southeast)--Lake Stevens & \
            Monroe Cities PUMA, Washington!!Total!!Estimate',
          'Snohomish County (North)--Marysville & Arlington Cities PUMA, \
            Washington!!Total!!Estimate',
          'Snohomish County (Southwest)--Edmonds, Lynnwood & Mountlake \
            Terrace Cities PUMA; Washington!!Total!!Estimate',
          'Snohomish County (West Central)--Mukilteo & Everett (Southwest) \
            Cities PUMA, Washington!!Total!!Estimate',
          'Snohomish County (Central)--Everett City (Central & East) & \
            Eastmont PUMA, Washington!!Total!!Estimate'
        ])

    # thurston
    thurston = data[data.filter(like='Thurston').columns]
    new = thurston.copy()
    new['sum'] = new.sum(axis=1)

    data['Thurston County'] = new['sum']
    data = data.drop(
        columns=[
          'Thurston County (Central)--Olympia, Lacey & Tumwater Cities PUMA; \
            Washington!!Total!!Estimate',
          'Thurston County (Outer) PUMA, Washington!!Total!!Estimate'
        ])

    # yakima
    yakima = data[data.filter(like='Yakima').columns]
    new = yakima.copy()
    new['sum'] = new.sum(axis=1)

    data['Yakima County'] = new['sum']
    data = data.drop(
        columns=[
          'Yakima County (Central)--Greater Yakima City PUMA, \
            Washington!!Total!!Estimate',
          'Yakima County (Outer)--Sunnyside & Grandview Cities PUMA, \
            Washington!!Total!!Estimate',
        ])

    # drop unnecessary columns
    data = data.drop(
        columns=[
          'Seattle City (Northwest) PUMA, Washington!!Total!!Estimate',
          'Seattle City (Northeast) PUMA, Washington!!Total!!Estimate',
          'Seattle City (Downtown)--Queen Anne & Magnolia PUMA, \
            Washington!!Total!!Estimate',
          'Seattle City (Southeast)--Capitol Hill PUMA, \
            Washington!!Total!!Estimate',
          'Seattle City (West)--Duwamish & Beacon Hill PUMA, \
            Washington!!Total!!Estimate'
        ])

    # clean data
    result = data
    result = result.T
    result.columns = result.iloc[0]
    result = result.reset_index()
    result = result.drop(0)

    name = filename.split('.')[0].split('/')[2].split('_')[2]
    result.columns = ['Region', 'Total Population', 'Less than High School',
                      'High school', 'College', 'Bachelor', 'Graduate', 'Year']

    # add a year column
    result['Year'] = name

    new_file = 'income_' + name + '.csv'
    result.to_csv(new_file, index=False)


def merge_income_data(files) -> pd.DataFrame:
    '''
    Merge income data for each year into one dataset
    '''
    directory = './data/income'
    filenames = os.listdir(directory)

    income = pd.concat([pd.read_csv(os.path.join(directory, f))
                        for f in filenames], ignore_index=True)

    income = income.set_index(['Region', 'Year'])

    # convert crosstable to stacked dataframe
    income_df = income.stack(level=0)
    income_df = income_df.to_frame()
    income_df.reset_index()
    income_df.columns = ['Region', 'Year', 'Educational Attainment',
                         'Median Income']

    return income_df


def main():
    # create income files
    create_income_dataset('median_income_2013.csv')
    create_income_dataset('median_income_2014.csv')
    create_income_dataset('median_income_2015.csv')
    create_income_dataset('median_income_2016.csv')
    create_income_dataset('median_income_2017.csv')


if __name__ == '__main__':
    main()

