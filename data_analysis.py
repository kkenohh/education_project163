import data_processing as dp


def createHealthDataset(smoking, diabetes, drinking, mental_health):
    '''
    Join 4 datasets on 4 different health behaviors
    '''
    data = smoking.merge(diabetes, on='Regions').\
        merge(drinking, on='Regions').\
        merge(mental_health, on='Regions')
    return data


def main():
    smoking = dp.clean_health_data('data/smoking.csv')
    diabetes = dp.clean_health_data('data/diabetes.csv')
    drinking = dp.clean_health_data('data/binge_drinking.csv')
    mental_health = dp.clean_health_data('data/poor_mental_health.csv')

    createHealthDataset(smoking, diabetes, drinking, mental_health)


if __name__ == '__main__':
    main()
