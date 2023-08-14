import pandas as pd
import numpy as np
import copy
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import warnings
warnings.filterwarnings("ignore")


# 过滤掉与等级相关性低的属性（此处train_set为整个数据集）
def filter_out_low_corr(train_set, colist, threshold, credit_or_star):
    corr_mat = train_set.corr()
    level_coname = credit_or_star + '_level'
    remaining_colist = copy.deepcopy(colist)
    level_corr_list = corr_mat[level_coname][colist]
    for column in colist:
        if abs(level_corr_list[column]) < threshold:
            remaining_colist.remove(column)

    return remaining_colist


# 找出一个矩阵中包含大于阈值相关系数最多的行
def my_find(corr_mat, colist, limit):
    n = len(colist)
    target = '-1'
    max_count = 0
    for i in range(n):
        row = colist[i]
        count = 0
        for j in range(i + 1, n):
            column = colist[j]
            if abs(corr_mat.loc[row, column]) > limit:
                count += 1
        if count > max_count:
            target = row
            max_count = count

    return target


def forward_delete_corr(train_set, colist, threshold):
    corr_mat = train_set.corr()
    drop_target = my_find(corr_mat, colist, threshold)
    remaining_colist = copy.deepcopy(colist)

    while drop_target != '-1':
        remaining_colist.remove(drop_target)
        drop_target = my_find(corr_mat, remaining_colist, threshold)

    return remaining_colist


# 通过方差膨胀系数判断多重共线性,保留系数小于10的属性
def get_low_vif_cols(train_set):

    VIF = cal_vif(train_set)
    remaining_colist = VIF[VIF['VIF'] <= 10]['feature'].tolist()
    return remaining_colist


# 通过岭回归法判断多重共线性
def remove_high_collinearity(train_set):
    # Separate input features and target variable
    X = train_set.iloc[:, :-1]  # All columns except the last one
    y = train_set.iloc[:, -1]  # Last column

    # Standardize input features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(X)

    # Create Ridge regression model
    ridge = Ridge(alpha=0.1)

    # Fit Ridge model to the data
    ridge.fit(scaled_data, y)

    # Get feature importances
    feature_importances = abs(ridge.coef_)

    # Sort and get the most important features
    selected_features = [f for _, f in sorted(zip(feature_importances, train_set.columns[:-1]), reverse=True)]

    return selected_features


# 计算vif
def cal_vif(train_set):
    mat = copy.deepcopy(train_set)

    zero_variance_cols = mat.columns[mat.var() == 0]
    mat = mat.drop(zero_variance_cols, axis=1)
    # 截距项
    mat['c'] = 1
    # 计算vif
    name = mat.columns
    x = np.matrix(mat)
    VIF_list = [variance_inflation_factor(x, i) for i in range(x.shape[1])]
    VIF = pd.DataFrame({'feature': name, "VIF": VIF_list})
    VIF.drop(VIF[VIF['feature'] == 'c'].index, inplace=True)
    return VIF
