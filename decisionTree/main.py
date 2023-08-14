import csv
from sklearn import metrics
import pandas as pd


# 计算基尼系数
def gini(test_data):
    prob_square_sum = 0
    nums = [0, 0, 0, 0, 0]
    for line in test_data:
        for i in range(1, 6):
            if line['rating'] == i:
                nums[i - 1] += 1
    for num in nums:
        prob_square_sum = (float(num) / float(len(test_data))) ** 2
    return 1 - prob_square_sum


# 计算出现次数最多的rating，并返回rating值
def get_most_label(test_data):
    label_count = {}
    for line in test_data:
        if line['rating'] not in label_count:
            label_count[line['rating']] = 1
        else:
            label_count[line['rating']] += 1
    labels = sorted(label_count.items(), key=lambda x: x[1], reverse=True)
    return labels[0][0]


# 计算方差
def cal_variance(test_data, tmp):
    res = 0
    mean = float(tmp) / len(test_data)
    for line in test_data:
        res += (line["usefulCount"] - mean) ** 2
    return res


# 判断是否可以删去usefulCount特征
def judge_useful_count_stop(test_data, tmp):
    threshold = 0.1
    variance = cal_variance(test_data, tmp)
    if variance < threshold:
        return True
    else:
        return False


# 获取最佳特征点和特征值
def get_best_feature(test_data):
    useful_counts, side_effects = set(), set()
    colum_table = {count: useful_counts, effect: side_effects}
    tmp = 0
    for line in test_data:
        useful_counts.add(line[count])
        side_effects.add(line[effect])
        tmp += line[count]
    useful_count_stop_flag = judge_useful_count_stop(test_data, tmp)
    if useful_count_stop_flag:
        del colum_table[count]
    if len(side_effects) == 1:
        del colum_table[effect]
    if len(colum_table) == 0:
        return -1, -1

    best_feature = ""
    best_feature_value = 0
    best_gini = 1
    for feature, values in colum_table.items():
        for value in values:
            left_data, right_data = spilt_set_by_value(test_data, feature, value)
            if len(left_data) == 0 or len(right_data) == 0:
                continue

            left_c = len(left_data) / float(len(test_data))
            right_c = len(right_data) / float(len(test_data))
            gini_res = gini(left_data) * left_c + gini(right_data) * right_c
            if gini_res <= best_gini:
                best_gini = gini_res
                best_feature = feature
                best_feature_value = value
    return best_feature, best_feature_value


def spilt_set_by_value(test_data, best_feature, value):
    left_data, right_data = [], []
    for line in test_data:
        if line[best_feature] < value:
            left_data.append(line)
        else:
            right_data.append(line)
    return left_data, right_data


def create_tree(test_data):
    out_flag = True  # 结束标志
    label = test_data[0]['rating']  # 第一个数据的rating
    for line in test_data:
        if line['rating'] != label:
            out_flag = False
    if out_flag:  # 如果rating均相等，结束创建
        return label
    best_feature, best_feature_value = get_best_feature(test_data)
    if best_feature == -1:
        return get_most_label(test_data)
    left_data, right_data = spilt_set_by_value(test_data, best_feature, best_feature_value)
    tree = {(best_feature, best_feature_value): []}
    tree[(best_feature, best_feature_value)].append(create_tree(left_data))
    tree[(best_feature, best_feature_value)].append(create_tree(right_data))
    return tree


def predict(tree, test_data):
    if type(tree) == int:
        return tree
    feature = list(tree.items())[0][0][0]
    point = list(tree.items())[0][0][1]
    right_tree = list(tree.items())[0][1][0]
    left_tree = list(tree.items())[0][1][1]
    if test_data[feature] < point:
        return predict(right_tree, test_data)
    else:
        return predict(left_tree, test_data)


# 进行文件读取，将数据以特定形式存储并返回
def read_file_return_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for r in reader:
            if r[rating] == '':
                data.append({count: int(r[count]),
                             effect: side_effects_table.index(r[effect]),
                             rating: 0})
            else:
                data.append({count: int(r[count]),
                             effect: side_effects_table.index(r[effect]),
                             rating: int(r[rating])})
    return data


if __name__ == '__main__':
    # 初始全局变量定义
    side_effects_table = ['No Side Effects', 'Moderate Side Effects', 'Mild Side Effects', 'Severe Side Effects',
                          'Extremely Severe Side Effects']
    count = "usefulCount"
    effect = "sideEffects"
    rating = "rating"
    train_data_path = "./data/training.csv"
    validation_data_path = './data/validation.csv'
    test_data_path = './data/testing.csv'
    test_res_path = './data/testing_res.csv'
    # 初始数据获取
    train_data = read_file_return_data(train_data_path)
    validation_data = read_file_return_data(validation_data_path)
    test_datas = read_file_return_data(test_data_path)

    res_tree = create_tree(train_data)
    # 预测结果生成
    validation_predict = []
    validation_true = []
    for data_line in validation_data:
        validation_predict.append(predict(res_tree, data_line))
        validation_true.append(data_line[rating])
    # 计算两个得分并打印
    micro_f1_score = metrics.f1_score(validation_true, validation_predict, labels=[1, 2, 3, 4, 5], average='micro')
    macro_f1_score = metrics.f1_score(validation_true, validation_predict, labels=[1, 2, 3, 4, 5], average='macro')
    print('micro_f1_score: ')
    print(micro_f1_score)
    print('macro_f1_score: ')
    print(macro_f1_score)
    # 预测结果生成
    test_predict = []
    for test_line in test_datas:
        test_predict.append(predict(res_tree, test_line))
    # 写入对于路径表中
    test_datas_re = pd.read_csv(test_data_path)
    test_datas_re[rating] = test_predict
    test_datas_re.to_csv(test_res_path, index=False, sep=',')
