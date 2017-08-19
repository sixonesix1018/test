# -*- coding:utf-8 -*-

studentOfPython = ['张三','李四','王五','旺财','小明','小红','小刚']
studentOfPyhtonWeb = ['小王','小明','张三','李明']
result1 = []
result2 = []

# for student in studentOfPython:
#     if student in studentOfPyhtonWeb:
#         result1.append(student)
#     else:
#         result2.append(student)
result1 = [student for student in studentOfPython if student in studentOfPyhtonWeb]
result2 = [student for student in studentOfPython if student not in studentOfPyhtonWeb]



print "python和Python web都学的学生数量为%d，名字为：" % len(result1)
for student in result1:
    print student

print "只学习python的学生数量为%d，名字为：" % len(result2)
for student in result2:
    print student

