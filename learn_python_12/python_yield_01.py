# yield的表达式形式1
# x = yield 返回值
# 例子1
# def dog(name):
#     print("道哥 {} 准备吃东西了".format(name))
#     while True:
#         # x拿到的是yield接收到的值, 跟None没有关系
#         #  x = '一根骨头'
#         x = yield
#         print("道哥{} 吃了 {}".format(name, x))
#
#
# g = dog("asdasd")
# g.send(None)  # 等同于next(g)
#
# g.send('一根骨头')
# g.send('123')
# g.send('qwe')
# g.send('asd')
#
# g.close()  # 关闭之后无法传值
# g.send("asdadadasasd")
