import pandas as pd
import copy
import filter
import preprocess as pp
import visualize
import MLWork


credit_or_star = 'star'


def form_csv_path(file_name):
    return '.\\data\\' + credit_or_star + '\\' + credit_or_star + '_' + file_name + '.csv'


# 读取 train_set.csv 文件
train_set = pd.read_csv(form_csv_path('train'))

# 1.2 数据盘点
describe_file = form_csv_path('train_describe')
train_set.describe().to_csv(describe_file)
visualize.visualize_describe(describe_file, credit_or_star)

# 2.1 缺失值处理
# 计算文件每一列的缺失值比例并保存至 star_train_missing.csv 文件
train_set.isnull().mean().to_csv(form_csv_path('train_missing'))
# 去除缺失值比例大于 0.7 的列
train_set = train_set.loc[:, train_set.isnull().mean() < 0.7]
# 填充缺失值
train_set = pp.handle_missing_knn(train_set)

catelist = []
colist = []
for i in train_set.columns:
    colist.append(i)
    if train_set[i].dtype == 'object':
        catelist.append(i)
colist.remove(credit_or_star + '_level')
colist.remove('uid')
catelist.remove('uid')
numlist = [i for i in colist if i not in catelist]

# 2.2 异常值处理
train_set = pp.replace_data(train_set)
train_set.to_csv(form_csv_path('train_handled'), index=False, encoding='utf_8_sig')

# 2.3 数据转换
train_set = pp.encode(train_set, catelist)
train_set.to_csv(form_csv_path('train_trans'), index=False, encoding='utf_8_sig')

# 2.4 数据标准化
train_set = pp.standardize(train_set, colist)
train_set.to_csv(form_csv_path('train_std'), index=False)

# 3 特征工程
print('特征工程开始......')
# 3.1 计算变量相关性
# 计算变量相关性并保存至 star_train_corr.csv 文件
train_set[colist].corr().to_csv(form_csv_path('train_corr'))
# 剔除相关性大于阈值的变量
colist = filter.forward_delete_corr(train_set[colist], colist, 0.9)

# 3.2 计算多重共线性
# 计算多重共线性并剔除相关性大于 10 的变量
colist = filter.get_low_vif_cols(train_set[colist])

# 3.3 通过岭回归法判断多重共线性
colist = filter.remove_high_collinearity(train_set[colist])

# 3.4 过滤与等级相关性低的属性
train_set_without_uid = copy.deepcopy(train_set).drop('uid', axis=1)
colist = filter.filter_out_low_corr(train_set_without_uid, colist, 0.1, credit_or_star)

catelist = [i for i in catelist if i in colist]
numlist = [i for i in numlist if i in colist]
print('特征工程处理完毕！')
train_set[colist].corr().to_csv(form_csv_path('train_corr_after'))

# 4 训练模型
print('=============================')
model = MLWork.model(train_set, colist, credit_or_star)
model.train()

# 5 模型评估
model.evaluate()

# 6 模型应用
print('=============================')
print('开始应用')
test_set = pd.read_csv(form_csv_path('test'))

test_set.isnull().mean().to_csv(form_csv_path('test_missing'))

test_set = test_set.loc[:, test_set.isnull().mean() < 0.7]

test_set = pp.handle_missing_knn(test_set)

test_set = pp.replace_data(test_set)

test_set = pp.encode(test_set, catelist)

test_set = pp.standardize(test_set, colist)

y_pred = model.predict_test(test_set, colist)

test_set[credit_or_star + '_level'] = y_pred

test_set.to_csv(form_csv_path('test_predict'), index=False, encoding='utf_8_sig')


print('=============================')
print('数据处理完成！')

