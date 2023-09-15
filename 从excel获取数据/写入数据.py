import pandas as pd

# 创建一个示例的DataFrame（数据表）
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# 指定要写入的Excel文件路径
excel_file = "output_data.xlsx"  # 替换为你要写入的Excel文件路径
# 创建ExcelWriter对象以允许格式化
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
# 将DataFrame写入Excel文件
df.to_excel(excel_writer, index=False, sheet_name='Sheet1')
# 获取ExcelWriter的工作簿和工作表对象
workbook = excel_writer.book
worksheet = excel_writer.sheets['Sheet1']
# 设置数据格式
double_format = workbook.add_format({'num_format': '0.000'})
worksheet.set_column('B:B', None, double_format)
# 保存Excel文件
excel_writer.save()
print(f"数据已成功写入Excel文件 '{excel_file}'。")