# -*- coding:utf-8 -*-

a = [25, 2, 39, 11, 24, 49, 32, 28]

print "排序前的列表为："
print a

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp


print "排序后的列表为："
print a