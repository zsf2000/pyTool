import pandas as pd
import numpy as np
import openpyxl
# 指定Excel文件路径
excel_file = "C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\MaSteel.xlsx"  # 替换为你的Excel文件路径

# 使用pandas读取Excel数据
df = pd.read_excel(excel_file)
#指定某一列
selected_colunm=df['AVGTFELASER']
# 将数据转换为NumPy数组
selected_colunm = selected_colunm.to_numpy()

# 打印NumPy数组
print(selected_colunm)