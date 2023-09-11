import re
import ast
##正则处理文件
f=open("new 3.txt",'r',encoding='utf-8')
strFile=f.readlines()
strFile=str(strFile)
strA='AA 处理文件 11'


def numBrackets(matched):
    value = (matched.group('value'))
    return str('('+value+')')

strRe=re.sub('(?P<value>\d+)', numBrackets, strFile)
#  ?P<name>对返回的值进行命名
filename='re0.txt'
#orgin_str=ast.literal_eval(strRe)
#orgin_str=str(orgin_str)
with  open(filename, 'w') as file_object:
    file_object.write(strRe)