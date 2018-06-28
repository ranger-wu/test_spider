'''
插入排序总结：
当前需要排序的元素(array[i])，跟已经排序好的最后一个元素比较(array[i-1])，
如果满足条件继续执行后面的程序，否则循环到下一个要排序的元素。
缓存当前要排序的元素的值，以便找到正确的位置进行插入。
排序的元素跟已经排序号的元素比较，比它大的向后移动(升序)。
要排序的元素，插入到正确的位置。

array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

# insert_sort
for i in range(1, len(array)):
    if array[i - 1] > array[i]:
        temp = array[i]     # 当前需要排序的元素
        index = i           # 用来记录排序元素需要插入的位置
        while index > 0 and array[index - 1] > temp:
            array[index] = array[index - 1]     # 把已经排序好的元素后移一位，留下需要插入的位置
            index -= 1
        array[index] = temp # 把需要排序的元素，插入到指定位置

# print sort result.
print(array)  '''

R = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
def direct_insert_sort(R):
    num = len(R)
    print("第 1 次：", R[1:])
    for i in range(2, num):
        R[0] = R[i]
        if R[i-1] <= R[0]:
            R[i] = R[0]
        else:
            for t in range(i):
                j = i-t
                if R[j] > R[0]:
                    R[j+1] = R[j]
                if R[j-1] <= R[0]:
                    R[j] = R[0]
                    break
        print ("第", i, "次：", R[1:])
    return R