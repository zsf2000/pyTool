import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 生成一组示例数据
data = np.random.normal(loc=0, scale=1, size=1000)

# # 绘制直方图
# plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram of Data')

# 添加正态分布拟合曲线
mu, std = np.mean(data), np.std(data)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2, label='Fit results')

plt.legend()
plt.show()

# 进行Shapiro-Wilk正态性检验
shapiro_test_statistic, shapiro_p_value = stats.shapiro(data)
print(f'Shapiro-Wilk Test Statistic: {shapiro_test_statistic}')
print(f'P-value: {shapiro_p_value}')

# 解释检验结果
alpha = 0.05
if shapiro_p_value > alpha:
    print('数据看起来服从正态分布')
else:
    print('数据不服从正态分布')

# 绘制Q-Q图
stats.probplot(data, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.show()