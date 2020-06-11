def shell_sort(li):
    # 希尔排序
    gap = len(li) // 2
    while gap >= 1:
        for j in range(gap, len(li)):
            i = j
            while (i-gap) >= 0:
                if li[i] < li[i - gap]:
                    li[i], li[i - gap] = li[i - gap], li[i]
                    i -= gap
                else:
                    break
        gap = int(gap//2)


if __name__ == '__main__':
    example = [26,22,33,54,89,61,325,65,45,55]
    print(example)
    shell_sort(example)
    print(example)