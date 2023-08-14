import pandas as pd
import matplotlib.pyplot as plt


def visualize_describe(file_name, credit_or_star):
    save_path = '.\\data\\' + credit_or_star + '\\' + credit_or_star + '_describe_visualization\\'
    describe = pd.read_csv(file_name, index_col=0)
    # 遍历每一列，绘制箱线图并保存为图片
    for column in describe.columns:
        count = describe.loc['count', column]
        if count == 0:
            continue
        std = describe.loc['std', column]
        mean = describe.loc['mean', column]
        min_value = describe.loc['min', column]
        q1 = describe.loc['25%', column]
        q2 = describe.loc['50%', column]
        q3 = describe.loc['75%', column]
        max_value = describe.loc['max', column]
        iqr = q3 - q1  # 四分位距（IQR）
        lower_bound = q1 - 5 * iqr  # 下边界
        upper_bound = q3 + 5 * iqr  # 上边界
        x_min = max(min_value, min(mean, q1) - 5 * iqr)
        x_max = min(max_value, max(mean, q3) + 5 * iqr)
        if iqr > 0:
            x_min = max(x_min, lower_bound)
            x_max = min(x_max, upper_bound)

        # 绘制箱线图
        fig, ax = plt.subplots()
        ax.boxplot([[]], positions=[0], widths=0.5, vert=False)  # 创建一个空的箱线图
        ax.scatter(mean, 0, color='red', marker='o', label='Mean')  # 绘制均值点
        ax.plot([min_value, max_value], [0, 0], color='black', linewidth=1)  # 绘制中轴线
        if min_value >= lower_bound:
            ax.plot([min_value, min_value], [-0.2, 0.2], color='black', linewidth=2)
        if max_value <= upper_bound:
            ax.plot([max_value, max_value], [-0.2, 0.2], color='black', linewidth=2)
        ax.plot([q1, q1], [-0.3, 0.3], color='black', linewidth=1)  # 绘制Q1
        ax.plot([q2, q2], [-0.3, 0.3], color='red', linewidth=1)  # 绘制Q2（中位数）
        ax.plot([q3, q3], [-0.3, 0.3], color='black', linewidth=1)  # 绘制Q3
        ax.plot([q1, q3], [0.3, 0.3], color='black', linewidth=1)
        ax.plot([q1, q3], [-0.3, -0.3], color='black', linewidth=1)
        # 在图上显示对应的值
        ax.annotate('mean:' + get_annotate(mean), (min(mean, x_max), 0), xytext=(min(mean, x_max), 0.1), color='red', ha='center')
        ax.annotate('min:' + get_annotate(min_value), (max(min_value, x_min), 0), xytext=(max(min_value, x_min), -0.2), ha='center')
        ax.annotate('25%:' + get_annotate(q1), (q1, 0), xytext=(q1, -0.25), ha='center')
        ax.annotate('50%:' + get_annotate(q2), (q2, 0), xytext=(q2, -0.3), color='red', ha='center')
        ax.annotate('75%:' + get_annotate(q3), (q3, 0), xytext=(q3, -0.35), ha='center')
        ax.annotate('max:' + get_annotate(max_value), (min(max_value, x_max), 0), xytext=(min(max_value, x_max), -0.2), ha='center')

        ax.set_xlim(x_min - iqr * 0.1 - 1, x_max + iqr * 0.1 + 1)  # 设置X轴范围
        ax.set_ylim(-0.5, 0.5)  # 设置Y轴范围
        ax.set_yticks([])  # 隐藏Y轴刻度
        ax.legend(loc='best')  # 显示图例
        ax.set_title(column)

        # 添加计数和标准差的文本
        text = f'Count: {count}\nStd: {std}'
        ax.text(0.05, 0.95, text, transform=ax.transAxes, verticalalignment='top')

        plt.savefig(f'{save_path}{column}_boxplot.png')
        plt.show()
        plt.close()
    print('数据盘点可视化完成！')


def get_annotate(val):
    s = str(val)
    dot_pos = s.find('.')
    decimal_places = len(s[dot_pos + 1:])
    if dot_pos != -1 and decimal_places > 2:
        return '{:.2f}'.format(val)
    else:
        return str(val)
