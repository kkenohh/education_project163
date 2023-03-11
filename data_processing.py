import geopandas as gpd
import pandas as pd


def clean_edu_data() -> pd.DataFrame:
    edu_data = pd.read_csv('educational_attainment.csv')
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


def clean_income_data(data) -> pd.DataFrame:
    data = data.drop([0, 21, 22])
    data = data.drop(range(2, 15))
    cols = data.columns.drop('Label (Grouping)')
    data[cols] = data[cols].apply(lambda x: x.str.replace(',', '').astype(float))

    # rename columns
    data = data.rename(columns={
        'Chelan & Douglas Counties PUMA, Washington!!Total!!Estimate': 'Chelan & Douglas Counties',
        'Clallam & Jefferson Counties PUMA, Washington!!Total!!Estimate': 'Clallam & Jefferson Counties',
        'Cowlitz, Pacific & Wahkiakum Counties PUMA; Washington!!Total!!Estimate': 'Cowlitz, Pacific & Wahkiakum Counties',
        'Grant & Kittitas Counties PUMA, Washington!!Total!!Estimate': 'Grant & Kittitas Counties',
        'Grays Harbor & Mason Counties PUMA, Washington!!Total!!Estimate': 'Grays Harbor & Mason Counties',
        'Lewis, Klickitat & Skamania Counties PUMA; Washington!!Total!!Estimate': 'Lewis, Klickitat & Skamania Counties',
        'Skagit, Island & San Juan Counties PUMA; Washington!!Total!!Estimate': 'Skajit, Island & San Juan Counties',
        'Stevens, Okanogan, Pend Oreille & Ferry Counties PUMA; Washington!!Total!!Estimate': 'Stevens, Okanogan, Pend Oreille & Ferry Counties',
        'Whatcom County--Bellingham City PUMA, Washington!!Total!!Estimate': 'Whatcom County--Bellingham City',
        'Whitman, Asotin, Adams, Lincoln, Columbia & Garfield Counties PUMA; Washington!!Total!!Estimate': 'Whitman, Asotin, Adams, Lincoln, Columbia & Garfield Counties',
        'Label (Grouping)': 'Label',
        'Washington!!Total!!Estimate': 'Washington'
    })

    # benton
    benton = data[data.filter(like='Benton').columns]
    sample = benton.copy()
    sample['Benton, Franklin, Kennewick, Richland & Walla Walla Counties'] = sample.sum(axis=1)
    sample = sample.drop(columns=['Benton & Franklin Counties--Pasco, Richland (North) & West Richland Cities PUMA; Washington!!Total!!Estimate',
                                  'Benton County (East Central)--Kennewick & Richland (South) Cities PUMA, Washington!!Total!!Estimate',
                                  'Walla Walla, Benton (Outer) & Franklin (Outer) Counties PUMA; Washington!!Total!!Estimate'])

    data['Benton, Franklin, Kennewick, Richland & Walla Walla Counties'] = sample['Benton, Franklin, Kennewick, Richland & Walla Walla Counties']
    data = data.drop(columns=['Benton & Franklin Counties--Pasco, Richland (North) & West Richland Cities PUMA; Washington!!Total!!Estimate',
                                  'Benton County (East Central)--Kennewick & Richland (South) Cities PUMA, Washington!!Total!!Estimate',
                                  'Walla Walla, Benton (Outer) & Franklin (Outer) Counties PUMA; Washington!!Total!!Estimate'])

    # clark
    clark = data[data.filter(like='Clark').columns]
    new = clark.copy()
    new['sum'] = new.sum(axis=1)

    data['Clark County'] = new['sum']
    data = data.drop(columns=['Clark County (Southwest)--Vancouver City (West & Central) PUMA, Washington!!Total!!Estimate',
                                            'Clark County (West Central)--Salmon Creek & Hazel Dell PUMA, Washington!!Total!!Estimate',
                                            'Clark County (Southeast)--Vancouver (East), Camas & Washougal Cities PUMA; Washington!!Total!!Estimate',
                                            'Clark County (North)--Battle Ground City & Orchards PUMA, Washington!!Total!!Estimate'])

    # king
    king = data[data.filter(like='King').columns]
    new = king.copy()
    new['sum'] = new.sum(axis=1)

    data['King County'] = new['sum']
    data = data.drop(columns=['King County (Northwest)--Shoreline, Kenmore & Bothell (South) Cities PUMA; Washington!!Total!!Estimate',
                                            'King County (Northwest)--Redmond, Kirkland Cities, Inglewood & Finn Hill PUMA; Washington!!Total!!Estimate',
                                            'King County (Northwest Central)--Greater Bellevue City PUMA, Washington!!Total!!Estimate',
                                            'King County (Central)--Sammamish, Issaquah, Mercer Island & Newcastle Cities PUMA; Washington!!Total!!Estimate',
                                            'King County (Central)--Renton City, Fairwood, Bryn Mawr & Skyway PUMA; Washington!!Total!!Estimate',
                                            'King County (West Central)--Burien, SeaTac, Tukwila Cities & White Center PUMA; Washington!!Total!!Estimate',
                                            'King County (Far Southwest)--Federal Way, Des Moines Cities & Vashon Island PUMA; Washington!!Total!!Estimate',
                                            'King County (Southwest Central)--Kent City PUMA, Washington!!Total!!Estimate',
                                            'King County (Southwest)--Auburn City & Lakeland PUMA, Washington!!Total!!Estimate',
                                            'King County (Southeast)--Maple Valley, Covington & Enumclaw Cities PUMA; Washington!!Total!!Estimate',
                                            'King County (Northeast)--Snoqualmie City, Cottage Lake, Union Hill & Novelty Hill PUMA; Washington!!Total!!Estimate'])

    # kitsap
    kitsap = data[data.filter(like='Kitsap').columns]
    new = kitsap.copy()
    new['sum'] = new.sum(axis=1)

    data['Kitsap County'] = new['sum']
    data = data.drop(columns=['Kitsap County (North)--Bainbridge Island City & Silverdale PUMA, Washington!!Total!!Estimate',
                                            'Kitsap County (South)--Bremerton & Port Orchard Cities PUMA, Washington!!Total!!Estimate'])

    # pierce
    pierce = data[data.filter(like='Pierce').columns]
    new = pierce.copy()
    new['sum'] = new.sum(axis=1)

    data['Pierce County'] = new['sum']
    data = data.drop(columns=['Pierce County (Central)--Tacoma City (Central) PUMA, Washington!!Total!!Estimate',
                                            'Pierce County (Northwest)--Peninsula Region & Tacoma City (West) PUMA, Washington!!Total!!Estimate',
                                            'Pierce County (West Central)--Lakewood City & Joint Base Lewis-McChord PUMA, Washington!!Total!!Estimate',
                                            'Pierce County (South Central)--Tacoma City (South), Parkland & Spanaway PUMA; Washington!!Total!!Estimate',
                                            'Pierce County (North Central)--Tacoma (Port) & Bonney Lake (Northwest) Cities PUMA, Washington!!Total!!Estimate',
                                            'Pierce County (East Central)--Puyallup City & South Hill PUMA, Washington!!Total!!Estimate',
                                            'Pierce County (Southeast)--Graham, Elk Plain & Prairie Ridge PUMA; Washington!!Total!!Estimate'])

    # spokane
    spokane = data[data.filter(like='Spokane').columns]
    new = spokane.copy()
    new['sum'] = new.sum(axis=1)

    data['Spokane County'] = new['sum']
    data = data.drop(columns=['Spokane County (North Central)--Spokane City (North) PUMA, Washington!!Total!!Estimate',
                                            'Spokane County (South Central)--Spokane City (South) PUMA, Washington!!Total!!Estimate',
                                            'Spokane County (East Central)--Greater Spokane Valley City PUMA, Washington!!Total!!Estimate',
                                            'Spokane County (Outer)--Cheney City PUMA, Washington!!Total!!Estimate'])

    # snohomish
    snohomish = data[data.filter(like='Snohomish').columns]
    new = snohomish.copy()
    new['sum'] = new.sum(axis=1)

    data['Snohomish County'] = new['sum']
    data = data.drop(columns=['Snohomish County (South Central)--Bothell (North), Mill Creek Cities & Silver Firs PUMA; Washington!!Total!!Estimate',
                                            'Snohomish County (Central & Southeast)--Lake Stevens & Monroe Cities PUMA, Washington!!Total!!Estimate',
                                            'Snohomish County (North)--Marysville & Arlington Cities PUMA, Washington!!Total!!Estimate',
                                            'Snohomish County (Southwest)--Edmonds, Lynnwood & Mountlake Terrace Cities PUMA; Washington!!Total!!Estimate',
                                            'Snohomish County (West Central)--Mukilteo & Everett (Southwest) Cities PUMA, Washington!!Total!!Estimate',
                                            'Snohomish County (Central)--Everett City (Central & East) & Eastmont PUMA, Washington!!Total!!Estimate'])

    # thurston
    thurston = data[data.filter(like='Thurston').columns]
    new = thurston.copy()
    new['sum'] = new.sum(axis=1)

    data['Thurston County'] = new['sum']
    data = data.drop(columns=['Thurston County (Central)--Olympia, Lacey & Tumwater Cities PUMA; Washington!!Total!!Estimate',
                                            'Thurston County (Outer) PUMA, Washington!!Total!!Estimate'])

    # yakima
    yakima = data[data.filter(like='Yakima').columns]
    new = yakima.copy()
    new['sum'] = new.sum(axis=1)

    data['Yakima County'] = new['sum']
    data = data.drop(columns=['Yakima County (Central)--Greater Yakima City PUMA, Washington!!Total!!Estimate',
                                            'Yakima County (Outer)--Sunnyside & Grandview Cities PUMA, Washington!!Total!!Estimate',
                                            ])

    # drop unnecessary columns
    data = data.drop(columns=['Seattle City (Northwest) PUMA, Washington!!Total!!Estimate',
            'Seattle City (Northeast) PUMA, Washington!!Total!!Estimate',
            'Seattle City (Downtown)--Queen Anne & Magnolia PUMA, Washington!!Total!!Estimate',
            'Seattle City (Southeast)--Capitol Hill PUMA, Washington!!Total!!Estimate',
            'Seattle City (West)--Duwamish & Beacon Hill PUMA, Washington!!Total!!Estimate'])

    #clean data
    cleaned = data
    cleaned = cleaned.T
    cleaned.columns = cleaned.iloc[0]
    cleaned = cleaned.reset_index()
    cleaned = cleaned.drop(0)
    cleaned = cleaned.rename(columns={'index': 'Region'})
    return cleaned


'''
Clean health outcomes datasets
'''
def clean_health_data(data):
    no_nan = data.dropna()

    # drop unneeded columns
    df = no_nan[['County', 'Count', 'Population', 'Percentage']]

    # convert percentage column to float
    regex = {r"\(NR\)": ""}
    df['Percentage'] = df['Percentage'].replace(regex, regex=True).astype(float)


    df = df.reindex([3, 11, 36, 4, 9, 5, 16, 6, 8, 25, 35, 13, 19, 14, 23,
                             17, 18, 21, 20, 30, 27, 29, 15, 28, 31, 32, 33, 24, 26,
                             10, 34, 37, 38, 2, 1, 22, 7, 12, 39])
    df = df.reset_index(drop=True)

    # create a new dataFrame with info by PUMA region code
    by_puma = pd.DataFrame(columns=['County', 'Count', 'Population', 'Percentage'])

    #benton
    benton = df.iloc[1:2].sum()

    by_puma = by_puma.append(benton.transpose(), ignore_index=True)

    #chelan
    chelan = df.iloc[3:4].sum()

    by_puma = by_puma.append(chelan.transpose(), ignore_index=True)

    #clallam
    clallam = df.iloc[5:6].sum()

    by_puma = by_puma.append(clallam.transpose(), ignore_index=True)

    # clark
    by_puma.loc[len(by_puma.index)] = df.loc[7]

    #pacific
    pacific = df.iloc[8:10].sum()

    by_puma = by_puma.append(pacific.transpose(), ignore_index=True)

    #grant
    grant = df.iloc[11:12].sum()

    by_puma = by_puma.append(grant.transpose(), ignore_index=True)

    #grays harbor
    grays = df.iloc[13:14].sum()

    by_puma = by_puma.append(grays.transpose(), ignore_index=True)

    # king and kitsap
    by_puma.loc[len(by_puma.index)] = df.loc[15]
    by_puma.loc[len(by_puma.index)] = df.loc[16]

    #lewis
    lewis = df.iloc[17:19].sum()

    by_puma = by_puma.append(lewis.transpose(), ignore_index=True)

    #pierce
    by_puma.loc[len(by_puma.index)] = df.loc[20]

    #skagit
    skagit = df.iloc[21:23].sum()

    by_puma = by_puma.append(skagit.transpose(), ignore_index=True)

    # snohomish and spokane
    by_puma.loc[len(by_puma.index)] = df.loc[24]
    by_puma.loc[len(by_puma.index)] = df.loc[25]

    # stevens
    stevens = df.iloc[26:29].sum()

    by_puma = by_puma.append(stevens.transpose(), ignore_index=True)

    # thurston and whatcom
    by_puma.loc[len(by_puma.index)] = df.loc[30]
    by_puma.loc[len(by_puma.index)] = df.loc[31]

    #whitman
    whitman = df.iloc[32:37].sum()

    by_puma = by_puma.append(whitman.transpose(), ignore_index=True)

    #yakima
    by_puma.loc[len(by_puma.index)] = df.loc[38]

    #rename county column
    regions = [
       'Benton, Franklin, Kennewick, Richland & Walla Walla Counties',
       'Chelan & Douglas Counties', 'Clallam & Jefferson Counties',
       'Clark County', 'Cowlitz, Pacific & Wahkiakum Counties',
       'Grant & Kittitas Counties', 'Grays Harbor & Mason Counties',
       'King County', 'Kitsap County',
       'Lewis, Klickitat & Skamania Counties', 'Pierce County',
       'Skagit, Island & San Juan Counties', 'Snohomish County',
       'Spokane County',
       'Stevens, Okanogan, Pend Oreille & Ferry Counties',
       'Thurston County', 'Whatcom County--Bellingham City',
       'Yakima County',
       'Whitman, Asotin, Adams, Lincoln, Columbia & Garfield Counties']

    county = by_puma['County'].unique()
    by_puma['County'] = by_puma['County'].replace(county, regions)

    #change column's name
    by_puma = by_puma.rename(columns={'County': 'Regions'})


    return by_puma

