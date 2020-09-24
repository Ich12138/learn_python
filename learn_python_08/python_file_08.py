# 1、通用文件copy工具实现
src_file_path = input("请输入源文件路径: ")
target_file_path = input("请输入源文件路径: ")
with open(src_file_path, mode='rb') as src_file, \
        open(target_file_path, mode='wb') as target_file:
    while True:
        file_byte = src_file.read(1024)
        if len(file_byte) == 0:
            break
        target_file.write(file_byte)
