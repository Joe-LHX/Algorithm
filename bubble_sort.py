def bubble_sort(li):
    # 冒泡排序
    a = len(li)
    for j in range(len(li) - 1):
        for i in range(0,a-1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        a -= 1


if __name__ == '__main__':
    example = [26, 22, 33, 54, 89, 61, 325, 65, 45, 55]
    print(example)
    bubble_sort(example)
    print(example)