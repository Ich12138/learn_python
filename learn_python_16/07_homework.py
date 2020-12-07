# 编写学生选课功能

# p361 定义学校类型以及功能
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


# 1、创建学校
lsh_school = School('辽宁石油化工大学', '辽宁省抚顺市望花区辽宁石油化工大学')
tute_school = School('天津职业技术师范大学', '天津市津南区大沽南路1310号')

# 2、为学校开设班级
# 辽宁石油化工大学 05班、15班
lsh_school.related_class('辽宁石油化工大学 05班')
lsh_school.related_class('辽宁石油化工大学 15班')

# 天津职业技术师范大学 1班、2班
tute_school.related_class('天津职业技术师范大学 1班')
tute_school.related_class('天津职业技术师范大学 2班')

# 需求: 查看学校信息和班级信息
# School.class_info(lsh_school)
# School.class_info(tute_school)


# p363 班级类定义及使用
class Class:
    def __init__(self, class_name):
        self.class_name = class_name
        self.course_name = None

    # 关联课程
    def related_course(self, course_name):
        self.course_name = course_name

    # 打印班级和课程信息
    def print_course_info(self):
        print('班级: {}, 课程: {}'.format(self.class_name, self.course_name))


lsh_class1 = Class('研21 05班')
lsh_class2 = Class('研21 15班')

lsh_class1.related_course('python学习')
lsh_class2.related_course('神经网路与人工智能')

# print(lsh_class1.print_course_info())
# print(lsh_class2.print_course_info())
