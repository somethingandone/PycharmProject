import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from scipy.stats.stats import pearsonr


# 统计MEDV数据分布情况
def make_histogram(boston_df):
    sns.set(rc={'figure.figsize': (11.7, 8.27)})
    sns.distplot(boston_df['MEDV'], bins=30, color='blue')


# 生成关系热力图，并且对三个个特征进行生成相关点阵
def make_heatmap(boston_df):
    fig = plt.figure(figsize=(16, 12))
    fig.add_subplot(111)
    sns.heatmap(boston_df.corr(), annot=True, cmap='plasma')
    sns.pairplot(boston_df[["LSTAT", "RM", "MEDV"]])


# 进行单个特征的回归生成
def make_corr_var(boston_df):
    MEDV = boston_df['MEDV']
    boston_feature = boston_df[['LSTAT', 'RM']]
    data = boston_df[['LSTAT', 'RM', 'MEDV']]
    for feature in boston_feature:
        fig = plt.figure()
        ax = plt.subplot(111)
        corr, _ = pearsonr(boston_feature[feature], MEDV)
        fit = np.polyfit(boston_feature[feature], MEDV, deg=1)
        plt.title('{} vs MEDV, corr = {}'.format(feature, round(corr, 2)))
        hb = ax.hexbin(data[feature], MEDV, cmap='plasma')
        ax.plot(boston_feature[feature], fit[0] * boston_feature[feature] + fit[1], color='white', linewidth=3)
        plt.xlabel(feature)
        plt.ylabel('MEDV')
        cb = fig.colorbar(hb, ax=ax)
        cb.set_label('counts')
        # plt.show()


# 分割训练集和测试集
def make_test_corr(boston_df, flag):
    if flag == "feature":
        x, y = boston_df[['LSTAT', 'RM']], boston_df['MEDV']
    else:
        x, y = boston_df[boston_df.columns.delete(-1)], boston_df['MEDV']

    x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp = train_test_split(x, y, test_size=0.3, random_state=3)
    return x_train_tmp, x_test_tmp, y_train_tmp, y_test_tmp


# 打印相关结果，r2系数反应回归效果
def print_res(x_train_tmp, y_test_tmp, y_pred_tmp):
    print('R^2: ', metrics.r2_score(y_test_tmp, y_pred_tmp))
    print('Adjusted R^2:',
          1 - (1 - metrics.r2_score(y_test_tmp, y_pred_tmp)) * (len(y_test_tmp) - 1) / (len(y_test_tmp) - x_train_tmp.shape[1] - 1))
    print('MAE:', metrics.mean_absolute_error(y_test_tmp, y_pred_tmp))
    print('MSE:', metrics.mean_squared_error(y_test_tmp, y_pred_tmp))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test_tmp, y_pred_tmp)))


if __name__ == '__main__':
    boston = pd.read_csv('./HousingData.csv')
    # 将nan替换成0
    boston.replace(np.nan, 0, inplace=True)
    # 数据可视化过程
    # make_histogram(boston)
    # make_heatmap(boston)
    # make_corr_var(boston)
    # 模式辨别，else为所有特征一起上
    flags = ["feature", "else"]
    x_train, x_test, y_train, y_test = make_test_corr(boston, flags[1])
    # 模型训练
    model = SVR()
    model.fit(x_train, y_train)
    # 预测
    y_pred = model.predict(x_test)
    print_res(x_train, y_test, y_pred)
