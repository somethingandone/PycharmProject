import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score


def plot_confusion_matrix(y_test, y_pred, class_names, save_path):
    # 5.2 混淆矩阵
    # 计算混淆矩阵并保存为图片
    # 假设 y_true, y_pred, class_names 已经定义
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=class_names, yticklabels=class_names,
           title='Confusion matrix',
           ylabel='True label',
           xlabel='Predicted label')

    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    fig.tight_layout()
    # plt.show()
    plt.savefig(save_path)


def count_accuracy_and_more(y_test, y_pred):
    # 5.1 计算准确率
    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    print('模型的准确率为：', accuracy)
    # 5.3 计算精确率和召回率
    precision = precision_score(y_test, y_pred, average='macro')  # 计算宏平均精确率
    recall = recall_score(y_test, y_pred, average='macro')  # 计算宏平均召回率
    # 打印出来
    print("精确率为: ", precision)
    print("召回率为: ", recall)
    # 5.4 计算F1分数
    f1 = f1_score(y_test, y_pred, average='macro')  # 计算宏平均F1分数
    print("F1分数为: ", f1)
    # 计算Cohen's Kappa系数
    kappa = cohen_kappa_score(y_test, y_pred)
    print("Cohen's Kappa系数为: ", kappa)
