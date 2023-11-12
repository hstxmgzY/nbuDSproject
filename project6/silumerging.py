def merge(a, b, s, mid1, mid2, mid3, e):
    # 初始化指针和临时数组索引
    i = s
    j = mid1 + 1
    k = mid2 + 1
    l = mid3 + 1
    t = i

    # 合并四个有序子数组
    while i <= mid1 and j <= mid2 and k <= mid3 and l <= e:
        if a[i] <= a[j] and a[i] <= a[k] and a[i] <= a[l]:
            b[t] = a[i]
            i += 1
        elif a[j] <= a[k] and a[j] <= a[l]:
            b[t] = a[j]
            j += 1
        elif a[k] <= a[l]:
            b[t] = a[k]
            k += 1
        else:
            b[t] = a[l]
            l += 1
        t += 1

    # 处理剩余的情况
    while i <= mid1 and j <= mid2 and k <= mid3:
        if a[i] <= a[j] and a[i] <= a[k]:
            b[t] = a[i]
            i += 1
        elif a[j] <= a[k]:
            b[t] = a[j]
            j += 1
        else:
            b[t] = a[k]
            k += 1
        t += 1

    while j <= mid2 and k <= mid3 and l <= e:
        if a[j] <= a[k] and a[j] <= a[l]:
            b[t] = a[j]
            j += 1
        elif a[k] <= a[l]:
            b[t] = a[k]
            k += 1
        else:
            b[t] = a[l]
            l += 1
        t += 1

    while k <= mid3 and l <= e and i <= mid1:
        if a[k] <= a[l] and a[k] <= a[i]:
            b[t] = a[k]
            k += 1
        elif a[l] <= a[i]:
            b[t] = a[l]
            l += 1
        else:
            b[t] = a[i]
            i += 1
        t += 1

    while i <= mid1 and j <= mid2:
        if a[i] <= a[j]:
            b[t] = a[i]
            i += 1
        else:
            b[t] = a[j]
            j += 1
        t += 1

    while j <= mid2 and k <= mid3:
        if a[j] <= a[k]:
            b[t] = a[j]
            j += 1
        else:
            b[t] = a[k]
            k += 1
        t += 1

    while k <= mid3 and l <= e:
        if a[k] <= a[l]:
            b[t] = a[k]
            k += 1
        else:
            b[t] = a[l]
            l += 1
        t += 1

    while l <= e and i <= mid1:
        if a[l] <= a[i]:
            b[t] = a[l]
            l += 1
        else:
            b[t] = a[i]
            i += 1
        t += 1

    # 处理剩余的子数组
    while i <= mid1:
        b[t] = a[i]
        i += 1
        t += 1

    while j <= mid2:
        b[t] = a[j]
        j += 1
        t += 1

    while k <= mid3:
        b[t] = a[k]
        k += 1
        t += 1

    while l <= e:
        b[t] = a[l]
        l += 1
        t += 1


def mergeSort(a, b, s, e):
    if s < e:
        # 计算中点位置
        mid1 = s + (e - s) // 4
        mid2 = s + (e - s) // 2
        mid3 = s + (3 * (e - s)) // 4

        # 递归地对四个子数组进行排序
        mergeSort(a, b, s, mid1)
        mergeSort(a, b, mid1 + 1, mid2)
        mergeSort(a, b, mid2 + 1, mid3)
        mergeSort(a, b, mid3 + 1, e)

        # 合并四个子数组
        merge(a, b, s, mid1, mid2, mid3, e)

        # 将结果复制回原数组
        for i in range(s, e + 1):
            a[i] = b[i]


n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)

numbers = input().split()
for i in range(1, n + 1):
    a[i] = int(numbers[i - 1])

# 调用归并排序算法
mergeSort(a, b, 1, n)

# 输出排序结果
print(a[1], end='')
for i in range(2, n + 1):
    print(' ', a[i], end='')

print()
