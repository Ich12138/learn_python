# 编写学生选课功能

# 定义学校类型以及功能
# 辽宁石油化工大学
# 辽宁省抚顺市望花区辽宁石油化工大学
class School:

    # 初始化学校, 初始化学校名称，学校地址和班级列表
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.classes = []

    # 关联班级
    def related_class(self, class_obj):
        self.classes.append(class_obj)

    # 打印学校信息和班级信息
    def class_info(self):
        print('学校名称: {}, 学校地址: {}'.format(self.school_name, self.school_addr))
        print('班级: ')
        for class_name in self.classes:
            print(class_name)
        print('\n')
