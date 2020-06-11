def insert_sort(li):
    # 插入排序
    for j in range(1, len(li)):
        for i in range(j,0,-1):
            if li[i] < li[i - 1]:
                li[i], li[i - 1] = li[i - 1], li[i]
            else:
                break


if __name__ == '__main__':
    example = [26, 22, 22, 54, 89, 61, 325, 65, 45, 55]
    print(example)
    insert_sort(example)
    print(example)