import pandas as pd

def delte():
    # 指定Excel文件路径
    excel_file = "C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\MaSteel.xlsx"  # 替换为你的Excel文件路径

    # 使用pandas读取Excel数据
    df = pd.read_excel(excel_file)
    # 删除满足条件的行，假设删除'A'列中值为3的行
    df = df[df['A'] != 3]
    # 保存更新后的数据回Excel文件
    df.to_excel("C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx", index=False)  # 替换为你要保存的Excel文件路径



# 指定Excel文件路径
input_excel_file = "input_excel_file.xlsx"  # 替换为你的Excel文件路径
output_excel_file = "output_excel_file.xlsx"  # 新Excel文件路径，用于保存删除行后的数据

# 使用pandas读取Excel数据
df = pd.read_excel(input_excel_file)

# 定义要删除的多个条件
condition1 = (df['Column1'] == 'Value1')  # 例如，删除'Column1'列中值等于'Value1'的行
condition2 = (df['Column2'] > 10)  # 例如，删除'Column2'列中值大于10的行

# 使用条件筛选删除满足多个条件的行
df = df[~(condition1 & condition2)]

# 将更新后的数据写回到新的Excel文件
df.to_excel(output_excel_file, index=False)

print(f"已删除Excel文件中满足多个条件的行，并保存到新文件 {output_excel_file} 中。")