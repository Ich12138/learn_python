# 1、九九乘法表

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{i} * {j} = {res}".format(i=i, j=j, res=i * j), end="      ")
#     print()


# 2、打印金字塔
# 数学表达式
# 空格数 = max_level - current_level
# *号数 = 2 * current_level - 1
max_level = 5
for current_level in range(max_level):
    for k in range(max_level - current_level):
        print(" ", end="")
    for j in range(2 * current_level - 1):
        print("*", end="")
    print()
