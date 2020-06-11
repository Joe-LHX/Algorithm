# @author lhx


def fast_sort(
        ex, start, end
):
    # 快速排序
    if start >= end:
     return
    mid =ex[start]
    left = start
    right = end
    while left < right:
        while left < right and ex[right] >= mid:
            right -= 1
        ex[left] = ex[right]
        while left < right and ex[left] <= mid:
            left += 1
        ex[right] = ex[left]
    # 从循环退出后及left=right，然后赋值
    ex[left] = mid
    fast_sort(ex, start, left - 1)
    fast_sort(ex, left + 1, end)


if __name__ == '__main__':
    example = [26,22,33,54,89,61,325,65,45,55]
    print(example)
    fast_sort(example, 0, len(example) - 1)
    print(example)