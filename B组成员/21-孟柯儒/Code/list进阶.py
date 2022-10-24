
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list1.append('g') # 在末尾添加元素
print(list1)
list1.insert(2, 'ooo')  # 在指定位置添加元素，如果指定的下标不存在，那么就是在末尾添加
print(list1)
print("\n")

list2 = ['z','y','x']
list1.extend(list2) # 合并两个list   list2中仍有元素
print(list1)
print(list2)


list1 = ['a','b','a','d','a','f']
print(list1.pop(3))
print(list1)
list1.remove('a')
print(list1)
print("\n")

print("----列表生成项-----")
# 如何让列表每一项加一
list_1 = [1,2,3,4,5]
for i in range(len(list_1)):
    list_1[i] += 1
print(list_1)

# pythonic的方法，简洁等效的方法
list_1 = [n+1 for n in list_1]
print(list_1)

# 1-10所有数平方
sum = [(n+1)**2 for n in range(10)]
print(sum)

# 1-10的奇数
numbers = [x for x in range(0,11) if x%2 != 0]
print(numbers)

app = ['app_%s'%n for n in range(5)]
print(app)

# 取两个列表的交集
list4 = [s for s in list1 if s in list_1]
print(list4)


list_A = [1,3,6,7,32,65,12]
list_B = [2,6,3,5,12]
list_A = [s for s in list_A if s not in list_B]
print(list_A)

listC =[m + n for m in 'ABC' for n in 'XYZ']
print(listC)