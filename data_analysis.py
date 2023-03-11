import data_processing as dp

EDU_DF = dp.clean_edu_data()


def create_health_dataset(smoking, diabetes, drinking, mental_health):
    '''
    Join 4 datasets on 4 different health behaviors
    '''
    data = smoking.merge(diabetes, on='Regions').\
        merge(drinking, on='Regions').\
        merge(mental_health, on='Regions')
    return data


def health_behaviors_by_attainment(health):
    '''
    Compare the trends of health behaviors for each educational attainment from
    2013 - 2017
    '''
    edu_data = EDU_DF[['Puma Label', 'Attainment Label',
                       'Estimate Population']]
    by_attainment = edu_data.groupby('Puma Label', 'Attainment Label').sum()

    data = by_attainment.merge(health, left_on='Puma Label',
                               right_on='Regions', how='left')
    return data


def main():
    smoking = dp.clean_health_data('data/smoking.csv')
    diabetes = dp.clean_health_data('data/diabetes.csv')
    drinking = dp.clean_health_data('data/binge_drinking.csv')
    mental_health = dp.clean_health_data('data/poor_mental_health.csv')

    create_health_dataset(smoking, diabetes, drinking, mental_health)


if __name__ == '__main__':
    main()
