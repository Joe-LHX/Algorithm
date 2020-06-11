def select_sort(li):
    # 选择排序
    for j in range(len(li) - 1):
        minsize = j
        for i in range(j+1, len(li)):
            if li[minsize] > li[i]:
                minsize = i
        if j != minsize:
            li[j], li[minsize] = li[minsize], li[j]


if __name__ == '__main__':
    example = [26, 22, 33, 54, 89, 61, 325, 65, 45, 55]
    print(example)
    select_sort(example)
    print(example)