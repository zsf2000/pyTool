import numpy as np
from scipy import stats
import pandas as pd
#************************************************************************************
#函数名称：OutlierDataFilter
#函数功能：离群数据过滤
#************************************************************************************
def OutlierDataFilter():
    # 生成示例数据，这里用随机数据代替
    data = np.random.randn(100)

    # 计算均值和标准差
    mean = np.mean(data)
    std_dev = np.std(data)

    # 设置阈值，通常可以选择1.96，这对应于95%置信度
    threshold = 1.96

    # 计算每个数据点的Z分数
    z_scores = np.abs((data - mean) / std_dev)

    # 找到超过阈值的数据点
    outliers = np.where(z_scores > threshold)

    # 打印离群数据点
    print("离群数据点：")
    print(data[outliers])

#************************************************************************************
#函数名称：FilterNegative
#函数功能：过滤负相关数据
#************************************************************************************
def FilterNegative():


# 创建一个示例DataFrame，替换为你的数据
    data = {'X': [1, 2, 3, 4, 5],
            'Y': [2, 3, -1, 6, -2]}

    df = pd.DataFrame(data)

    # 计算X和Y之间的相关性
    correlation = df['X'].corr(df['Y'])

    # 如果相关性是正的，保留数据
    if correlation > 0:
        positive_correlation = df
    else:
        positive_correlation = pd.DataFrame()  # 创建一个空的DataFrame

    # 打印结果
    print(positive_correlation)
    print(df)

OutlierDataFilter()