import os
def delete():
    # 指定要删除的文件路径
    file_to_delete = "example.txt"  # 替换为你要删除的文件路径

    # 检查文件是否存在
    if os.path.exists(file_to_delete):
        # 删除文件
        os.remove(file_to_delete)
        print(f"文件 '{file_to_delete}' 已成功删除。")
    else:
        print(f"文件 '{file_to_delete}' 不存在，无法删除。")

def create():
        # 指定要查询的文件路径
    file_path = "example.txt"  # 替换为你的文件路径

    # 查询文件是否存在
    if not os.path.exists(file_path):
        # 如果文件不存在，则创建文件并写入内容
        with open(file_path, 'w') as file:
            file.write("这是一个示例文件。")

        print(f"文件 '{file_path}' 不存在，已创建文件并写入内容。")
    else:
        print(f"文件 '{file_path}' 已存在，无需创建。")