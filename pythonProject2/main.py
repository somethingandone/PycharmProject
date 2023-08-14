import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv(r'C:/Users/86181/Desktop/report_strip.csv')
plt.plot(data.during_time,
         data.avg_score,
         linestyle='-',
         color='steelblue',
         label='mut_score')

plt.ylabel('mut_score')
plt.xlabel('runtime, min')
plt.show()
