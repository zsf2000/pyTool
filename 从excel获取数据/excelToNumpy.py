
# 指定Excel文件路径
excel_file = "C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\MaSteel.xlsx"  # 替换为你的Excel文件路径
result_excel_file='C:\\Users\\zsf\\Desktop\\pythonTool\\类线性关系拟合\\updated_excel_file.xlsx'
# 使用pandas读取Excel数据
df = pd.read_excel(result_excel_file)
#指定某一列
selected_colunm=df['差值']
# 将数据转换为NumPy数组
selected_colunm = selected_colunm.to_numpy()