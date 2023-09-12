import pandas as pd
import numpy as np
import openpyxl
#************************************************************************************
#函数名称：OutlierDataFilter
#函数功能：离群数据过滤
#************************************************************************************
def OutlierDataFilter(npTemp,npRes):
    # 生成示例数据，这里用随机数据代替
    data = np.random.randn(100)

    # 计算均值和标准差
    mean = np.mean(npTemp)
    std_dev = np.std(npTemp)

    # 设置阈值，通常可以选择1.96，这对应于95%置信度
    threshold = 1.96

    # 计算每个数据点的Z分数
    z_scores = np.abs((npTemp - mean) / std_dev)

    # 找到超过阈值的数据点
    outliers = np.where(z_scores > threshold)
    npRes=npTemp[outliers]
    # 打印离群数据点
    print("离群数据点：")
    print(npRes)
    return npRes

#************************************************************************************
#函数名称：delete
#函数功能：
#************************************************************************************ 
def delte():
    # 指定Excel文件路径
    excel_file = "C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\MaSteel.xlsx"  # 替换为你的Excel文件路径

    # 使用pandas读取Excel数据
    df = pd.read_excel(excel_file)
    # 删除满足条件的行，假设删除'A'列中值为3的行
    df = df[df['AVGTFELASER'] != 3]
    # 保存更新后的数据回Excel文件
    df.to_excel("C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx", index=False)  # 替换为你要保存的Excel文件路径



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
npRes=np.empty((1,10))
npRes=OutlierDataFilter(selected_colunm,npRes)
# 定义要删除的多个条件
df.to_excel("C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx", index=False)
dfTemp = pd.read_excel("C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx")
for x in  npRes.T:
    print(x)
    dfTemp = pd.read_excel("C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx")
    condition1 = (dfTemp['AVGTFELASER'] == x)  # 例如，删除'Column1'列中值等于'Value1'的行
    dfTemp = dfTemp[~(condition1)]
    #将更新后的数据写回到新的Excel文件
    dfTemp.to_excel("C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx", index=False)
