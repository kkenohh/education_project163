from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd


def predict_income(data: pd.DataFrame):
    # one-hot encoding educational attainment and region
    features = data.loc[:, data.columns != 'Median Income']
    features = pd.get_dummies(features)
    labels = data['Median Income']

    # create training and testing set
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3)

    # build the model
    model = DecisionTreeRegressor()

    # train on the training set
    model.fit(features_train, labels_train)

    # assess the model
    train_predict = model.predict(features_train)
    train_acc = mean_squared_error(labels_train, train_predict)
    print('train', train_acc)

    test_predict = model.predict(features_test)
    test_acc = mean_squared_error(labels_test, test_predict)
    print('test', test_acc)


def predict_attainment(data: pd.DataFrame):
    # one-hot encoding educational attainment and region
    features = data.loc[:, data.columns != 'Educational Attainment']
    features = pd.get_dummies(features)
    labels = data['Educational Attainment']

    # create training and testing set
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3)

    # build the model
    model = DecisionTreeClassifier()

    # train on the training set
    model.fit(features_train, labels_train)

    # assess the model
    train_predict = model.predict(features_train)
    train_acc = accuracy_score(labels_train, train_predict)
    print('train', train_acc)

    test_predict = model.predict(features_test)
    test_acc = accuracy_score(labels_test, test_predict)
    print('test', test_acc)


def main():
    income = pd.read_csv('data/median_income.csv')
    predict_income(income)
    predict_attainment(income)


if __name__ == '__main__':
    main()
