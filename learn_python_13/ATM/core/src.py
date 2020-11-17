# 核心代码逻辑

# 登录功能
def login():
    print("登录功能")


# 注册功能
def register():
    print("注册功能")


# 提现功能
def withdraw():
    print("提现功能")


# 转账功能
def transfer():
    print("转账功能")


# 函数字典
func_dic = {
    '0': ['退出', exit],
    '1': ['登录', login],
    '2': ['注册', register],
    '3': ['提现', withdraw],
    '4': ['转账', transfer],
}


# 项目启动入口
def run():
    while True:
        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input("请输入指令编号: ").strip()
        if choice in func_dic:
            func_dic[choice][1]()
        else:
            print("请重新输入")
