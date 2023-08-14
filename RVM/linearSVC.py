import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score


def make_heatmap(cancer_df):
    fig = plt.figure(figsize=(16, 12))
    fig.add_subplot(111)
    sns.heatmap(cancer_df.corr(), annot=True, cmap='plasma')
    # sns.pairplot(cancer_df)
    # plt.show()


def make_test_corr1(cancer_df):
    remain_feature = ["radius_mean", "perimeter_mean", "area_mean",
                      "concavity_mean", "concave points_mean"]
    x, y = cancer_df[remain_feature], cancer_df['diagnosis']
    x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp = train_test_split(x, y, test_size=0.3, random_state=5)
    return x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp


def make_test_corr2(cancer_df):
    features_remain = ['radius_mean', 'texture_mean', 'perimeter_mean',
                       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
                       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
                       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
                       'fractal_dimension_se', 'radius_worst', 'texture_worst',
                       'perimeter_worst', 'area_worst', 'smoothness_worst',
                       'compactness_worst', 'concavity_worst', 'concave points_worst',
                       'symmetry_worst', 'fractal_dimension_worst']
    x, y = cancer_df[features_remain], cancer_df['diagnosis']
    x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp = train_test_split(x, y, test_size=0.3, random_state=5)
    return x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp


def make_test_corr3(cancer_df):
    features_pick = ['perimeter_mean', 'concave points_mean', 'radius_worst', 'concave points_mean']
    x, y = cancer_df[features_pick], cancer_df['diagnosis']
    x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp = train_test_split(x, y, test_size=0.3, random_state=5)
    return x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp


if __name__ == '__main__':
    cancer = pd.read_csv("./brest_cancer_data.csv")
    target = cancer['diagnosis']
    cancer_tmp = cancer.columns[1: 12]
    target.replace('M', 0, inplace=True)
    target.replace('B', 1, inplace=True)
    # make_heatmap(cancer[cancer_tmp])
    x_train, x_test, y_train, y_test = make_test_corr3(cancer)
    # 进行训练集数据格式化，格式化为均值为0方差为1
    ss = StandardScaler()
    train_x = ss.fit_transform(x_train)
    test_x = ss.transform(x_test)

    model = LinearSVC()
    model.fit(train_x, y_train)
    prediction = model.predict(test_x)
    print('准确率: {:.4%}'.format(accuracy_score(y_test, prediction)))
    print('召回率: {:.4%}'.format(recall_score(y_test, prediction)))
