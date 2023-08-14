import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler


def get_numeric_columns(data):
    return data.select_dtypes(include='number').columns


def get_categorical_columns(data):
    return data.select_dtypes(include=['object', 'category']).columns


# 对于类别型变量，用众数填充缺失值
def handle_missing_object(data):
    # 选择类别型列
    categorical_columns = get_categorical_columns(data)
    # 使用众数填充类别型列的缺失值
    data.loc[:, categorical_columns] = data.loc[:, categorical_columns].fillna(data[categorical_columns].mode().iloc[0])
    return data


# 基础缺失值处理方法：用中位数填充数值型缺失值；用众数填充类别型缺失值
def handle_missing_base(data):
    # 对于数值型变量，用中位数填充缺失值
    # 选择数值型列
    numeric_columns = get_numeric_columns(data)
    # 使用中位数填充数值型列的缺失值
    data.loc[:, numeric_columns] = data.loc[:, numeric_columns].fillna(data[numeric_columns].median())

    data = handle_missing_object(data)
    print('缺失值处理完毕！')
    return data


def handle_missing_knn(data):
    numeric_columns = get_numeric_columns(data)
    # 使用KNN插补填充数值型缺失值
    imputer = KNNImputer(n_neighbors=5)
    data[numeric_columns] = imputer.fit_transform(data[numeric_columns])
    # 类别型缺失值仍用众数填充
    data = handle_missing_object(data)

    print('缺失值处理完毕！')
    return data


# <5%和>95%的使用5%和95%的数据替换
def replace_data_base(train_set):
    numeric_columns = get_numeric_columns(train_set)
    # 计算5%和95%的分位数
    lower_quantile = train_set[numeric_columns].quantile(0.05)
    upper_quantile = train_set[numeric_columns].quantile(0.95)

    # 将小于5%分位数的值替换为5%分位数的值
    train_set[numeric_columns] = train_set[numeric_columns].mask(train_set[numeric_columns] < lower_quantile,
                                                                 lower_quantile, axis=0)
    # 将大于95%分位数的值替换为95%分位数的值
    train_set[numeric_columns] = train_set[numeric_columns].mask(train_set[numeric_columns] > upper_quantile,
                                                                 upper_quantile, axis=0)
    print('异常值处理完毕！')
    return train_set


# 使用箱线图进行异常值处理
def replace_data(train_set):
    numeric_columns = get_numeric_columns(train_set)
    # 将原本的0值替换为NaN
    train_set.replace(0, np.nan, inplace=True)
    for column in numeric_columns:
        # 绘制箱线图
        plt.figure()
        train_set.boxplot(column=column)
        plt.title(column)
        # 计算异常值阈值
        q1 = train_set[column].quantile(0.25)  # 第一四分位数
        if math.isnan(q1):
            continue
        q3 = train_set[column].quantile(0.75)  # 第三四分位数
        iqr = q3 - q1  # 四分位距（IQR）
        lower_bound = q1 - 1.5 * iqr  # 下边界
        upper_bound = q3 + 1.5 * iqr  # 上边界
        # 处理异常值，将超出边界值的数值设为边界值
        train_set[column] = np.where(train_set[column].isnull(), np.nan,
                                     train_set[column].clip(lower=lower_bound, upper=upper_bound))
        # 关闭plt
        plt.close()
    # 将NaN值改回为0
    train_set.replace(np.nan, 0, inplace=True)
    print('异常值处理完毕！')
    return train_set


def encode(data, catelist):
    le = LabelEncoder()
    data[catelist] = data[catelist].apply(le.fit_transform)
    print('数据转换完成！')
    return data


def standardize(data, colist):
    scaler = StandardScaler()
    data[colist] = scaler.fit_transform(data[colist])
    print('数据标准化完成！')
    return data
