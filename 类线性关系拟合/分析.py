import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import pandas as pd
# # 生成虚拟数据
# np.random.seed(0)
# X = np.linspace(0, 1, 100)
# y = 2 * X + 1 + np.random.normal(0, 0.2, 100)

# # 划分数据集为训练集和测试集
# X_train, X_test = X[:80], X[80:]
# y_train, y_test = y[:80], y[80:]

# 指定Excel文件路径
excel_file = "C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\MaSteel.xlsx"  # 替换为你的Excel文件路径
result_excel_file='C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx'
# 使用pandas读取Excel数据
df = pd.read_excel(result_excel_file)
#指定某一列
selected_colunm1=df['AVGTFELASER']
selected_colunm2=df['VALUE']
# 将数据转换为NumPy数组
selected_colunm1 = selected_colunm1.to_numpy()
selected_colunm2 = selected_colunm2.to_numpy()
X=selected_colunm1 
y=selected_colunm2
# 划分数据集为训练集和测试集
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]
# 构建神经网络模型
model = keras.Sequential([
    keras.layers.Dense(1, input_dim=1)  # 一个输入特征和一个输出
])

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
history = model.fit(X_train, y_train, epochs=100, verbose=0)

# 评估模型
mse = model.evaluate(X_test, y_test)
print(f"Mean Squared Error on Test Data: {mse}")

# 绘制数据和模型拟合曲线
plt.scatter(X_test, y_test, label='Test Data')
y_pred = model.predict(X_test)
plt.plot(X_test, y_pred, color='red', label='Model Fit')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Data and Model Fit')
plt.show()